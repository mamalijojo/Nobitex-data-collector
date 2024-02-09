import requests as req
import datetime
from time import sleep
import csv
# ______________________

field_names = ['date','price']

with open('1MinPrice.csv', 'a', newline='') as csv_file:

    writerObj = csv.writer(csv_file)
    # writerObj.writerow(['date','price'])

    _url = 'https://api.nobitex.ir/market/stats'
    _data = {'srcCurrency': 'btc', 'dstCurrency': 'usdt'}

    x = datetime.datetime.now()
    d = x.strftime("%H:%M")
    time = f'{x.month}/{x.day}/{x.year} ' + d

    now_price = req.post(_url, _data).json()['global']['binance']['btc']

    writerObj.writerow([time, now_price])
