import pandas as pd


class Candle:
    def __init__(self, self_data: pd.Series, prev_data: pd.Series = pd.Series([])):
        self.date = f"{self_data['Day']}/{self_data['Month']}/{self_data['Year']}"
        self.open = self_data['Open']
        self.high = self_data['High']
        self.low = self_data['Low']
        self.close = self_data['Close']
        self.volume = self_data['Volume']

        if "Hour" in self_data:
            self.date += f" {self_data['Hour']}:{self_data['Minute'] if self_data['Minute'] >= 10 else f"0{self_data['Minute']}"}"

        if prev_data.any():
            self.result = (self_data['Close'] - prev_data['Close']) / self_data['Close'] * 100
        else:
            self.result = (self_data['Close'] - self_data['Open']) / self_data['Close'] * 100

