import requests
import numpy as np

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