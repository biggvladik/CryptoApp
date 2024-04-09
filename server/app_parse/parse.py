import aiohttp
import redis
import requests


async def get_current_price(money_id: int) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://api.coinlore.net/api/ticker/?id={money_id}') as response:
            res = await response.json()
            return res


def create_redis_conn():
    pub = redis.Redis(host='localhost', port=6379)
    return pub


res = requests.get('https://stat2matchtv.khl.ru/')
print(res.content)
