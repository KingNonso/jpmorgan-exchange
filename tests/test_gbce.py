import unittest
from unittest.mock import Mock
from jpmorgan.gbce import GBCE
from jpmorgan.stock import Stock

class TestGBCE(unittest.TestCase):

    def setUp(self):
        """Set up the test data for the tests."""
        self.gbce = GBCE()

    def test_add_stock(self):
        """Test adding a single stock."""
        stock = Mock(spec=Stock)
        self.gbce.add_stock(stock)
        self.assertEqual(len(self.gbce.stocks), 1)
        self.assertEqual(self.gbce.stocks[0], stock)

    def test_add_multiple_stocks(self):
        """Test adding multiple stocks."""
        stock1 = Mock(spec=Stock)
        stock2 = Mock(spec=Stock)
        self.gbce.add_stock(stock1)
        self.gbce.add_stock(stock2)
        self.assertEqual(len(self.gbce.stocks), 2)
        self.assertEqual(self.gbce.stocks[0], stock1)
        self.assertEqual(self.gbce.stocks[1], stock2)

    def test_calculate_all_share_index_no_stocks(self):
        """Test calculating the all-share index with no stocks."""
        index = self.gbce.calculate_all_share_index()
        self.assertEqual(index, 0)

    def test_calculate_all_share_index_with_trades(self):
        """Test calculating the all-share index with stocks that have recorded trades."""
        stock1 = Mock(spec=Stock)
        stock1.calculate_volume_weighted_stock_price.return_value = 100.0
        stock2 = Mock(spec=Stock)
        stock2.calculate_volume_weighted_stock_price.return_value = 200.0

        self.gbce.add_stock(stock1)
        self.gbce.add_stock(stock2)

        index = self.gbce.calculate_all_share_index()
        expected_index = (100.0 * 200.0) ** 0.5
        self.assertAlmostEqual(index, expected_index)

    def test_calculate_all_share_index_with_no_trades(self):
        """Test calculating the all-share index with stocks that have no trades."""
        stock1 = Mock(spec=Stock)
        stock1.calculate_volume_weighted_stock_price.return_value = 0.0
        stock2 = Mock(spec=Stock)
        stock2.calculate_volume_weighted_stock_price.return_value = 0.0

        self.gbce.add_stock(stock1)
        self.gbce.add_stock(stock2)

        index = self.gbce.calculate_all_share_index()
        self.assertEqual(index, 0)

    def test_calculate_all_share_index_mix_trades_no_trades(self):
        """Test calculating the all-share index with a mix of stocks with and without trades."""
        stock1 = Mock(spec=Stock)
        stock1.calculate_volume_weighted_stock_price.return_value = 100.0
        stock2 = Mock(spec=Stock)
        stock2.calculate_volume_weighted_stock_price.return_value = 0.0

        self.gbce.add_stock(stock1)
        self.gbce.add_stock(stock2)

        index = self.gbce.calculate_all_share_index()
        self.assertEqual(index, 100.0)

if __name__ == '__main__':
    unittest.main()
