from fastapi import APIRouter
from .parse import get_current_price
import asyncio

router = APIRouter()
@router.get("/get_price{id}", response_description= "get price crypto by id")
async def get_price(money_id:int):
   res = await get_current_price(money_id)
   return res

