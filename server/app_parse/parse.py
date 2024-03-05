import aiohttp

async def get_current_price(money_id:int)->dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://api.coinlore.net/api/ticker/?id={money_id}') as response:
            res = await response.json()
            return res

