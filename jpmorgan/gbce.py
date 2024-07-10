from functools import lru_cache
from typing import List
from jpmorgan.stock import Stock


class GBCE:
    """
    The GBCE class represents the London Stock Exchange's FTSE 100 Index, also known as the FTSE 100 or the
    FTSE 100 Index. It is a share index of the 100 companies listed on the London Stock Exchange with
    higher market capitalization.

    This class provides methods to add stocks to the index, calculate the volume-weighted stock price
    for individual stocks, and calculate the all-share index of the entire index.

    Attributes:
        stocks (List[Stock]): A list of Stock objects representing the constituent companies of the index.

    Methods:
        add_stock(stock: Stock): Adds a new Stock object to the list of constituent companies.
        calculate_all_share_index() -> float: Calculates the all-share index of the entire index.
    """

    def __init__(self):
        """
        Initializes a new instance of the GBCE class.

        Attributes:
            stocks (List[Stock]): A list of Stock objects representing the constituent companies of the index.
        """
        self.stocks: List[Stock] = []

    def add_stock(self, stock: Stock):
        """
        Adds a new Stock object to the list of constituent companies.

        Args:
            stock (Stock): A Stock object representing a company listed on the London Stock Exchange.

        Returns:
            None
        """
        self.stocks.append(stock)

    @lru_cache(None)
    def calculate_all_share_index(self) -> float:
        """
        Calculates the all-share index of the entire index.

        Returns:
            float: The all-share index of the entire index.
        """
        n = len(self.stocks)
        if n == 0:
            return 0.0

        product_of_prices = 1.0
        valid_stock_count = 0

        for stock in self.stocks:
            price = stock.calculate_volume_weighted_stock_price()
            if price > 0:
                product_of_prices *= price
                valid_stock_count += 1

        if valid_stock_count == 0:
            return 0.0

        return product_of_prices ** (1 / valid_stock_count)

