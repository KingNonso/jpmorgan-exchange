import datetime
from typing import List
from jpmorgan.trade import Trade


class Stock:
    """
    A class representing a stock with its attributes and methods.

    Attributes:
        symbol (str): A string representing the stock's symbol.
        type (str): A string representing the stock's type (either 'Common' or 'Preferred').
        last_dividend (float): A float representing the last dividend paid by the stock.
        fixed_dividend (float): A float representing the fixed dividend paid by the stock (only for 'Preferred' stocks).
        par_value (float): A float representing the par value of the stock.
        trades (List[Trade]): A list of Trade objects representing the stock's trading history.

    Methods:
        __init__(symbol: str, type: str, last_dividend: float, fixed_dividend: float, par_value: float)
            Initializes a new Stock object with the given attributes.

        calculate_dividend_yield(price: float) -> float
            Calculates the dividend yield of the stock based on the given price.

        calculate_pe_ratio(price: float) -> float
            Calculates the price-to-earnings ratio of the stock based on the given price.

        record_trade(quantity: int, indicator: str, price: float)
            Records a new trade for the stock with the given quantity, indicator, and price.

        calculate_volume_weighted_stock_price() -> float
            Calculates the volume-weighted average price of the stock over the last 5 minutes.
    """
    def __init__(self, symbol: str, type: str, last_dividend: float, fixed_dividend: float, par_value: float):
        """
        Initializes a new Stock object with the given attributes.

        Parameters:
            symbol (str): A string representing the stock's symbol.
            type (str): A string representing the stock's type (either 'Common' or 'Preferred').
            last_dividend (float): A float representing the last dividend paid by the stock.
            fixed_dividend (float): A float representing the fixed dividend paid by the stock (only for 'Preferred' stocks).
            par_value (float): A float representing the par value of the stock.

        Attributes:
            symbol (str): The stock's symbol.
            type (str): The stock's type ('Common' or 'Preferred').
            last_dividend (float): The last dividend paid by the stock.
            fixed_dividend (float): The fixed dividend paid by the stock (only for 'Preferred' stocks).
            par_value (float): The par value of the stock.
            trades (List[Trade]): A list of Trade objects representing the stock's trading history.
        """
        self.symbol = symbol
        self.type = type
        self.last_dividend = last_dividend
        self.fixed_dividend = fixed_dividend
        self.par_value = par_value
        self.trades: List[Trade] = []

    def calculate_dividend_yield(self, price: float) -> float:
        """
        Calculates the dividend yield of the stock based on the given price.

        Parameters:
            price (float): The current market price of the stock.

        Returns:
            float: The dividend yield of the stock. If the stock type is 'Common', the function returns the last dividend paid by the stock divided by the current market price. If the stock type is 'Preferred', the function returns the fixed dividend paid by the stock (multiplied by its par value) divided by the current market price.
        """
        if self.type == 'Common':
            return self.last_dividend / price
        elif self.type == 'Preferred':
            return (self.fixed_dividend * self.par_value) / price

    def calculate_pe_ratio(self, price: float) -> float:
        """
        Calculates the price-to-earnings ratio of the stock based on the given price.

        Parameters:
            price (float): The current market price of the stock.

        Returns:
            float: The price-to-earnings (P/E) ratio of the stock. If the dividend is zero, the function returns 0. In some cases, the function may also return infinity.
        """
        dividend = self.last_dividend if self.type == 'Common' else (self.fixed_dividend * self.par_value)
        if dividend == 0:
            return 0 # may also return inf
        return price / dividend

    def record_trade(self, quantity: int, indicator: str, price: float):
        """
        Records a new trade for the stock with the given quantity, indicator, and price.

        Parameters:
            quantity (int): The number of shares traded.
            indicator (str): A string representing the type of trade (e.g., 'Buy', 'Sell').
            price (float): The price at which the trade was executed.

        Returns:
            None: This function does not return a value. It simply records the trade in the stock's trading history.
        """
        timestamp = datetime.datetime.now()
        trade = Trade(timestamp, quantity, indicator, price)
        self.trades.append(trade)

    def calculate_volume_weighted_stock_price(self) -> float:
        """
        Calculates the volume-weighted average price of the stock over the last 5 minutes.

        Parameters:
            None

        Returns:
            float: The volume-weighted average price of the stock over the last 5 minutes. If there are no trades within the last 5 minutes, the function returns 0.
        """
        total_quantity = 0
        total_traded_price_quantity = 0
        five_minutes_ago = datetime.datetime.now() - datetime.timedelta(minutes=5)

        for trade in self.trades:
            if trade.timestamp >= five_minutes_ago:
                total_quantity += trade.quantity
                total_traded_price_quantity += trade.price * trade.quantity

        if total_quantity == 0:
            return 0
        return total_traded_price_quantity / total_quantity

