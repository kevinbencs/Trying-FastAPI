from fastapi import APIRouter,Depends,status,HTTPException

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)


@router.get('/')
def read():
    return {"Get": "Blogs"}


@router.post('/', status_code=status.HTTP_201_CREATED)
def new_item(item: str):
    if item == 'aaa':
        raise HTTPException(status_code=status.HTTP_200_OK, detail=f'{item} is exist')
    return {"Item": item}