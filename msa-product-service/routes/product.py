from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Product(BaseModel):
    name: str
    desc: str
    price: str
    maker: str
    regdate: str
@router.post('/product')
async def new_user(product: Product):
    print(product)

    return {'msg': 'ok'}
