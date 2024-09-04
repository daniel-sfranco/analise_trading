import yfinance as yf
from candle import Candle


def set_date(df):
    if 'Datetime' in df:
        df['Year'] = df['Datetime'].dt.year
        df['Month'] = df['Datetime'].dt.month
        df['Day'] = df['Datetime'].dt.day
        df['Hour'] = df['Datetime'].dt.hour
        df['Minute'] = df['Datetime'].dt.minute
    elif 'Date' in df:
        df['Year'] = df['Date'].dt.year
        df['Month'] = df['Date'].dt.month
        df['Day'] = df['Date'].dt.day
    return df


def retrieve_stock_data(stock, interval):
    ticker = yf.Ticker(stock)
    df = ticker.history(interval=interval)
    if df.empty:
        raise NameError
    df.reset_index(inplace=True)
    df = set_date(df)
    df['Open'] = round(df['Open'] * 100) / 100
    df['Close'] = round(df['Close'] * 100) / 100
    df.drop('Stock Splits', axis=1, inplace=True)
    return df


def read_stocks(num_stocks, market):
    interval = '1d'
    stocks = []
    df = []
    candles = []
    i = 0
    while i < num_stocks:
        try:
            stocks.append(input("Choose a stock: ").upper() + ('.SA' if market == 1 else ""))
            df.append(retrieve_stock_data(stocks[i], interval))
        except NameError:
            print("Invalid stock name. Please try again.")
            stocks.pop()
            continue
        candles.append([Candle(self_data=df[i].loc[0])])
        for c in range(1, len(df[i])):
            candles[i].append(Candle(self_data=df[i].loc[c], prev_data=df[i].loc[c - 1]))
        print(f"{stocks[i]} processed")
        i += 1
    return candles