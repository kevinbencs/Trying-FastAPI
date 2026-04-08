from fastapi import APIRouter,Depends,status,HTTPException

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)


@router.get('/')
def read():
    return {"Get": "Blogs"}