import datetime
from typing import List
from jpmorgan.trade import Trade


class Stock:
    def __init__(self, symbol: str, type: str, last_dividend: float, fixed_dividend: float, par_value: float):
        self.symbol = symbol
        self.type = type
        self.last_dividend = last_dividend
        self.fixed_dividend = fixed_dividend
        self.par_value = par_value
        self.trades: List[Trade] = []

    def calculate_dividend_yield(self, price: float) -> float:
        if self.type == 'Common':
            return self.last_dividend / price
        elif self.type == 'Preferred':
            return (self.fixed_dividend * self.par_value) / price

    def calculate_pe_ratio(self, price: float) -> float:
        dividend = self.last_dividend if self.type == 'Common' else (self.fixed_dividend * self.par_value)
        if dividend == 0:
            return 0 # may also return inf
        return price / dividend

    def record_trade(self, quantity: int, indicator: str, price: float):
        timestamp = datetime.datetime.now()
        trade = Trade(timestamp, quantity, indicator, price)
        self.trades.append(trade)

    def calculate_volume_weighted_stock_price(self) -> float:
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

