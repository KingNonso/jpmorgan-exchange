import datetime

class Trade:
    def __init__(self, timestamp: datetime.datetime, quantity: int, indicator: str, price: float):
        self.timestamp = timestamp
        self.quantity = quantity
        self.indicator = indicator
        self.price = price