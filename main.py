import pandas as pd
from data import *
from candle import *

market = int(input("Which market do you want to analyze? \n    1. Brazil \n    2. USA\n"))
num_stocks = int(input("How many stocks to analyze? "))
candles = read_stocks(num_stocks, market)
avaliable_strategies = ["SMA/EMA", "VOLUME"]
strategy = int(input("Choose a strategy to analyze: \n  1. SMA/EMA \n   2. Volume"))

