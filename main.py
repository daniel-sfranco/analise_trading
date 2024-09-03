import pandas as pd
from data import *
from candle import *

num_stocks = int(input("How many stocks to analyze? "))
interval = '1d'
stocks = []
df = []
candles = []
for i in range(num_stocks):
    stocks.append(input("Choose a stock: ").upper() + '.SA')
    df.append(retrieve_data(stocks[i], interval))
    candles.append([Candle(self_data=df[i].loc[0])])
    for c in range(1, len(df[i])):
        candles[i].append(Candle(self_data=df[i].loc[c], prev_data=df[i].loc[c - 1]))
    print(f"{stocks[i]} processed")
