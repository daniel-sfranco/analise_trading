import yfinance as yf


def retrieve_data(stock, interval):
    ticker = yf.Ticker(stock)

    df = ticker.history(interval=interval)
    df.reset_index(inplace=True)

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

    df['Open'] = round(df['Open'] * 100) / 100
    df['Close'] = round(df['Close'] * 100) / 100
    df.drop('Stock Splits', axis=1, inplace=True)
    return df