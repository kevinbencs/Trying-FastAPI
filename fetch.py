import requests
import numpy as np
import psycopg2
from psycopg2.extras import execute_values

url = "https://www.thecocktaildb.com/api/json/v1/1/list.php?c=list"
url2 = "https://www.thecocktaildb.com/api/json/v1/1/filter.php?c="
url3 = "https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i="

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
else:
    categories = np.array([item["strCategory"] for item in data["drinks"]])


idDrink = np.array([])

for j in categories:
    try:
        response = requests.get(url2 + j, timeout=5)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    else:
        idDrink = np.concatenate((idDrink, np.array([item["idDrink"] for item in data["drinks"]])))
        



for i in idDrink:
    try:
        response = requests.get(url3 + i, timeout=5)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    else:
        item = [item for item in data["drinks"]]
        print(item)



def create_tables(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS drinks (
            id_drink INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT,
            alcoholic TEXT,
            glass TEXT,
            instructions TEXT,
            thumbnail TEXT
        );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS drink_ingredients (
            id SERIAL PRIMARY KEY,
            id_drink INTEGER REFERENCES drinks(id_drink) ON DELETE CASCADE,
            ingredient TEXT NOT NULL,
            measure TEXT
        );
    """)


def insert_drinks(cur, drinks):
    drink_rows = [
        (
            int(d["idDrink"]),
            d.get("strDrink"),
            d.get("strCategory"),
            d.get("strAlcoholic"),
            d.get("strGlass"),
            d.get("strInstructions"),
            d.get("strDrinkThumb"),
        )
        for d in drinks
    ]

    execute_values(
        cur,
        """
        INSERT INTO drinks (id_drink, name, category, alcoholic, glass, instructions, thumbnail)
        VALUES %s
        ON CONFLICT (id_drink) DO UPDATE SET
            name = EXCLUDED.name,
            category = EXCLUDED.category,
            alcoholic = EXCLUDED.alcoholic,
            glass = EXCLUDED.glass,
            instructions = EXCLUDED.instructions,
            thumbnail = EXCLUDED.thumbnail;
        """,
        drink_rows,
    )

    ingredient_rows = []
    for d in drinks:
        for ing in extract_ingredients(d):
            ingredient_rows.append((int(d["idDrink"]), ing["name"], ing["measure"]))

    if ingredient_rows:
        ids = list({r[0] for r in ingredient_rows})
        cur.execute("DELETE FROM drink_ingredients WHERE id_drink = ANY(%s)", (ids,))
        execute_values(
            cur,
            "INSERT INTO drink_ingredients (id_drink, ingredient, measure) VALUES %s",
            ingredient_rows,
        )