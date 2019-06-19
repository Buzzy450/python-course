import requests
import random
import time
from random import *

begin = time.time()

response = requests.get("https://bitbay.net/API/Public/BTCPLN/ticker.json")
data = response.json()
best_bid=data['bid']
best_ask=data['ask']
print('bid:',best_bid,'ask:',best_ask)

i = 100
osoby = []
while len(osoby) < i:
    try:
        response = requests.get("https://randomuser.me/api/?inc=id,name,login")
        data = response.json()
        ide = data["results"][0]['id']['value']
        username = data["results"][0]['login']['username']
        first = data["results"][0]['name']['first']
        last = data["results"][0]['name']['last']
        btc = round(random() * 10,2)
        pln = round(uniform(5000,150000),2)
        
        osoby.append(first)
        osoby.append(last)
        osoby.append(username)
        osoby.append(ide)
        osoby.append(btc)
        osoby.append(pln)

    except:
        pass
osoby = list(osoby)
for k in range(len(osoby)):
    print(osoby[k])

zliczanie_wymian = 0

while zliczanie_wymian < i:

    rand = choice(osoby)
    rand2 = choice(osoby)

    while rand == rand2:
        rand2 = choice(osoby)
    
    a = uniform(0.2,0.7)
    value = rand[4]
    btc_ex = value * a
    pln_ex = value * a * best_bid
    
    if pln_ex <= rand2[5]:
        zliczanie_wymian += 1
        rand2[4] = rand2[4] + btc_ex
        rand2[5] = rand2[5] - pln_ex
        rand[5] = rand[5] + pln_ex
        rand[4] = rand[4] - btc_ex

        print(rand[2], 'exchanged', btc_ex, 'BTC for', pln_ex, 'PLN with', rand2[2])
    else:
        pass

for k in range(len(osoby)):
    print(osoby[k])

end = time.time()
print('time:', end - begin)
