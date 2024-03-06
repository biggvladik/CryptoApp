from fastapi import APIRouter
from .parse import get_current_price,create_redis_conn
import json
router = APIRouter()
redis_cache = create_redis_conn()

@router.get("/get_price{id}", response_description= "get price crypto by id")
async def get_price(money_id:int):
   data =  redis_cache.get(str(money_id))
   if data:
      return json.loads(data)
   else:
      res = await get_current_price(money_id)
      text_res = json.dumps(res)
      redis_cache.set(f'{money_id}',text_res,ex=5)
      return res

