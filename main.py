import pandas as pd
from data import *
from candle import *

stock = 'ABEV3.SA'
interval = '1d'
df = retrieve_data(stock, interval)

sma = int(input("Enter a simple moving average: "))
df[f'{sma} simple moving average'] = df['Close'].rolling(sma).mean().round(2)
ema = int(input("Enter a exponential moving average: "))
df[f'{ema} exp moving average'] = df['Close'].ewm(ema).mean().round(2)

candles = [Candle(df.loc[0], sma=sma, ema=ema)]
print(candles[0])
for c in range(1, len(df)):
    candles.append(Candle(df.loc[c], df.loc[c - 1], sma=sma, ema=ema))
    print(candles[c])
