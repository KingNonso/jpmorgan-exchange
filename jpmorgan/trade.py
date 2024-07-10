import datetime

class Trade:
    def __init__(self, timestamp: datetime.datetime, quantity: int, indicator: str, price: float) -> None:
        """
        Initialize a Trade object with the given timestamp, quantity, indicator, and price.

        :param timestamp: The datetime object representing the time of the trade.
        :type timestamp: datetime.datetime
        :param quantity: The integer representing the quantity of the trade.
        :type quantity: int
        :param indicator: The string representing the indicator used for the trade.
        :type indicator: str
        :param price: The float representing the price of the trade.
        :type price: float
        """
        if not isinstance(timestamp, datetime.datetime):
            raise TypeError("timestamp must be a datetime object")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("quantity must be a positive integer")
        if indicator not in ["buy", "sell"]:
            raise ValueError("indicator must be 'buy' or 'sell'")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("price must be a positive number")
        self.timestamp = timestamp
        self.quantity = quantity
        self.indicator = indicator
        self.price = price