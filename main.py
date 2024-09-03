import pandas as pd
from data import *
from candle import *

market = int(input("Which market do you want to analyze? \n    1. Brazil \n    2. USA\n"))
num_stocks = int(input("How many stocks to analyze? "))
interval = '1d'
stocks = []
df = []
candles = []
i = 0
while i < num_stocks:
    try:
        stocks.append(input("Choose a stock: ").upper() + ('.SA' if market == 1 else ""))
        df.append(retrieve_data(stocks[i], interval))
    except NameError:
        print("Invalid stock name. Please try again.")
        stocks.pop()
        continue
    candles.append([Candle(self_data=df[i].loc[0])])
    for c in range(1, len(df[i])):
        candles[i].append(Candle(self_data=df[i].loc[c], prev_data=df[i].loc[c - 1]))
    print(f"{stocks[i]} processed")
    i += 1
