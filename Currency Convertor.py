import json
import urllib.request
#turn off certificate check
#this website has incorrectly signed certificate:
import ssl

#turn off cert check
context = ssl._create_unverified_context()

# download raw json object
url = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
data = urllib.request.urlopen(url, context=context).read().decode()

# parse json object
rates = json.loads(data)

#get user input with value exception
try:
    UAH=float(input("Enter UAH amount: "))
except (ValueError):
    print("Incorrect value, use numbers only")
    quit()

#function prints result
def print_values(currency,buy,sale):
    print(currency, 'buy:',buy ,'sale:',sale)

#convert UAH to all downloaded currencies except bitcoins
for rate in rates:
    if rate['ccy']!='BTC':
        Buy=UAH/float(rate['buy'])
        Sale=UAH/float(rate['sale'])
        print_values(rate['ccy'], Buy, Sale)

#convert UAH to USD to BTC
BTC_buy=UAH/float(rates[0]['buy'])/float(rates[3]['buy'])
BTC_sale=UAH/float(rates[0]['sale'])/float(rates[3]['sale'])

print_values('BTC',BTC_buy ,BTC_sale)
