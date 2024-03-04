import requests

def get_money(money_id:int)->dict:
    res = requests.get(f'https://api.coinlore.net/api/ticker/?id={money_id}')
    return res.json()


print(get_money(90))