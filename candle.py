import pandas as pd


class Candle:
    def __init__(self, self_data: pd.Series, prev_data: pd.Series = pd.Series([]), sma: int = 20, ema: int = 9):
        self.date = f"{self_data['Day']}/{self_data['Month']}/{self_data['Year']}"
        self.open = self_data['Open']
        self.high = self_data['High']
        self.low = self_data['Low']
        self.close = self_data['Close']
        self.sma = self_data[f'{sma} simple moving average']
        self.sma_value = sma
        self.ema = self_data[f'{ema} exp moving average']
        self.ema_value = ema
        self.volume = self_data['Volume']

        if "Hour" in self_data:
            self.date += f" {self_data['Hour']}:{self_data['Minute'] if self_data['Minute'] >= 10 else f"0{self_data['Minute']}"}"

        if prev_data.any():
            self.result = (self_data['Close'] - prev_data['Close']) / self_data['Close'] * 100
        else:
            self.result = (self_data['Close'] - self_data['Open']) / self_data['Close'] * 100

    def __str__(self):
        if self.result > 0:
            color = "\033[1;32m "
        elif self.result < 0:
            color = "\033[1;31m "
        else:
            color = "\033[1;90m "
        return f"Date: {self.date} \nOpen: {self.open} \nClose: {self.close} \n{self.sma_value} Simple Moving Average: {self.sma} \n{self.ema_value} Exp Moving Average: {self.ema} \nResult: {color}{self.result:.2f}%\033[0m \nVolume: {self.volume} \n"