import requests
from random import *
import time

begin = time.time()

k = 0
z = 50
wszyscy=[]

for i in range(0,z):
    try:
        
        uzytkownicy=[]
        response = requests.get('https://randomuser.me/api/?inc=id,name,login')
        uzytkownik = response.json()

        username = uzytkownik['results'][0]['login']['username']
        first = uzytkownik['results'][0]['name']['first']
        last = uzytkownik['results'][0]['name']['last']
        uuid = uzytkownik['results'][0]['login']['uuid']
        name = first + ' ' + last

        uzytkownicy.append(first)
        uzytkownicy.append(last)
        uzytkownicy.append(username)
        uzytkownicy.append(uuid)
    
        best_bid= requests.get('https://www.bitmarket.pl/json/BTCPLN/ticker.json')
        BTC=best_bid.json()
        kursBTC=float(BTC["ask"])

        randomBTC=round(kursBTC*random()*0.001,3)
        uzytkownicy.append(randomBTC)

        randomPLN=round(uniform(5000,150000),2)
        uzytkownicy.append(randomPLN)
        
        uzytkownicy.append(name)

        wszyscy.append(uzytkownicy)
    except:
        pass

print(wszyscy)

while k<z:
    
    best_bid= requests.get('https://www.bitmarket.pl/json/BTCPLN/ticker.json')
    BTC=best_bid.json()
    kursBTC=float(BTC["ask"])
    kursPLN=1/kursBTC
    
    sprzedajacy=choice(wszyscy)
    x=sprzedajacy[4]*uniform(0.1,0.5)
    wymiana_btc_zl = x * kursBTC
    print(sprzedajacy[2],'zamierza sprzedać',round(x,3),'BTC')

    while wymiana_btc_zl!=0:
        
        kupujacy = choice(wszyscy)

        while sprzedajacy[3] == kupujacy[3]:
            kupujacy = choice(wszyscy)

        y = kupujacy[5]
        
        if y>=wymiana_btc_zl:
            kupujacy[5]=kupujacy[5]-wymiana_btc_zl
            kupujacy[4]=kupujacy[4]+x
            sprzedajacy[5]=sprzedajacy[5]+wymiana_btc_zl
            sprzedajacy[4]=sprzedajacy[4]-x
            print(sprzedajacy[2],"sprzedał",round(wymiana_btc_zl*kursPLN,3),"BTC użytkownikowi", kupujacy[2],"za", round(wymiana_btc_zl,2), "zł")
            wymiana_btc_zl=0

        else:
            kupujacy[5]=0
            kupujacy[4]=kupujacy[4]+y*kursPLN
            sprzedajacy[5]=sprzedajacy[5]+y
            sprzedajacy[4]=sprzedajacy[4]-y*kursPLN
            print(sprzedajacy[2],"sprzedał",round(y*kursPLN,3) , "BTC użytkownikowi", kupujacy[2], "za", round(y,2), "zł")
            wymiana_btc_zl = wymiana_btc_zl - y
            time.sleep(2 / 5)
    print("Koniec tranzakcji użytkownika", sprzedajacy[2])
    k=k+1
    time.sleep(2/5)

end = time.time()
print(end - begin)

