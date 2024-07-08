import unittest
from datetime import datetime, timedelta

from index import GBCE
from jpmorgan.stock import Stock
from jpmorgan.trade import Trade

class TestStockMethods(unittest.TestCase):

    def setUp(self):
        self.common_stock = Stock(symbol="POP", type="Common", last_dividend=8, fixed_dividend=0, par_value=100)
        self.preferred_stock = Stock(symbol="GIN", type="Preferred", last_dividend=8, fixed_dividend=0.02, par_value=100)
        self.gbce = GBCE()

    def test_calculate_dividend_yield_common(self):
        price = 100
        expected_yield = 0.08  # 8 / 100
        self.assertAlmostEqual(self.common_stock.calculate_dividend_yield(price), expected_yield)

    def test_calculate_dividend_yield_preferred(self):
        price = 100
        expected_yield = 0.02  # (0.02 * 100) / 100
        self.assertAlmostEqual(self.preferred_stock.calculate_dividend_yield(price), expected_yield)

    def test_calculate_pe_ratio_common(self):
        price = 100
        expected_pe_ratio = 12.5  # 100 / 8
        self.assertAlmostEqual(self.common_stock.calculate_pe_ratio(price), expected_pe_ratio)

    def test_calculate_pe_ratio_preferred(self):
        price = 100
        expected_pe_ratio = 50  # 100 / (0.02 * 100)
        self.assertAlmostEqual(self.preferred_stock.calculate_pe_ratio(price), expected_pe_ratio)

    def test_record_trade(self):
        quantity = 100
        indicator = 'buy'
        price = 110
        self.common_stock.record_trade(quantity, indicator, price)
        self.assertEqual(len(self.common_stock.trades), 1)
        trade = self.common_stock.trades[0]
        self.assertEqual(trade.quantity, quantity)
        self.assertEqual(trade.indicator, indicator)
        self.assertEqual(trade.price, price)

    def test_calculate_volume_weighted_stock_price(self):
        now = datetime.now()
        self.common_stock.trades = [
            Trade(now - timedelta(minutes=4), 100, 'buy', 110),
            Trade(now - timedelta(minutes=3), 200, 'sell', 120),
            Trade(now - timedelta(minutes=6), 150, 'buy', 130),  # This trade should be ignored
        ]
        expected_vwsp = (100*110 + 200*120) / (100 + 200)
        self.assertAlmostEqual(self.common_stock.calculate_volume_weighted_stock_price(), expected_vwsp)

    def test_calculate_all_share_index(self):
        stock1 = Stock(symbol="POP", type="Common", last_dividend=8, fixed_dividend=0, par_value=100)
        stock2 = Stock(symbol="TEA", type="Common", last_dividend=0, fixed_dividend=0, par_value=100)
        stock3 = Stock(symbol="GIN", type="Preferred", last_dividend=8, fixed_dividend=0.02, par_value=100)
        
        stock1.trades = [Trade(datetime.now() - timedelta(minutes=4), 100, 'buy', 110)]
        stock2.trades = [Trade(datetime.now() - timedelta(minutes=3), 200, 'sell', 120)]
        stock3.trades = [Trade(datetime.now() - timedelta(minutes=2), 150, 'buy', 130)]
        
        self.gbce.add_stock(stock1)
        self.gbce.add_stock(stock2)
        self.gbce.add_stock(stock3)
        
        vwsp1 = stock1.calculate_volume_weighted_stock_price()
        vwsp2 = stock2.calculate_volume_weighted_stock_price()
        vwsp3 = stock3.calculate_volume_weighted_stock_price()
        
        expected_index = (vwsp1 * vwsp2 * vwsp3) ** (1/3)
        self.assertAlmostEqual(self.gbce.calculate_all_share_index(), expected_index)

if __name__ == '__main__':
    unittest.main()
