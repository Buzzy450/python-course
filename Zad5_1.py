import requests

def get_BTC(x):
    response = requests.get(x)
    data_BTC = response.json()
    return data_BTC


response = requests.get("https://bitbay.net/API/Public/BTCPLN/ticker.json")
data_BTC = response.json()
response = requests.get("https://www.bitmarket.pl/json/BTCPLN/ticker.json")
data_BTC_2 = response.json()

bid1 = data_BTC['bid']
bid2 = data_BTC_2['bid']

print('Selling:')

if bid1 > bid2:
    print('Bitbay is better for selling')
else:
    print('Bitmarket is better for selling')

print('Buying:')

if bid1 < bid2:
    print('Bitbay is better for buying')
else:
    print('Bitmarket is better for buying')
