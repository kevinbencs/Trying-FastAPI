from fastapi import APIRouter,Depends,status,HTTPException

router = APIRouter(
    prefix="/book",
    tags=['Books']
)

@router.get("/")
def read():
    return {"Get":"books"}


@router.post("/",status_code=status.HTTP_201_CREATED)
def new_item(item: str):
    if item == "":
        return HTTPException(status_code=status.HTTP_200_OK, detail=f'{item} is exist')
    return {"Item": item}