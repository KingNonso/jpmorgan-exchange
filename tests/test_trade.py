import unittest
from datetime import datetime
from jpmorgan.trade import Trade  

class TestTrade(unittest.TestCase):

    def setUp(self):
        """Set up test data for the tests."""
        self.timestamp = datetime.now()
        self.quantity = 100
        self.indicator = "buy"
        self.price = 150.0

    def test_trade_initialization(self):
        """Test the initialization of the Trade object with valid inputs."""
        trade = Trade(self.timestamp, self.quantity, self.indicator, self.price)
        
        self.assertEqual(trade.timestamp, self.timestamp)
        self.assertEqual(trade.quantity, self.quantity)
        self.assertEqual(trade.indicator, self.indicator)
        self.assertEqual(trade.price, self.price)
    
    def test_trade_invalid_quantity(self):
        """Test the initialization of the Trade object with invalid quantity."""
        with self.assertRaises(ValueError):
            Trade(self.timestamp, -10, self.indicator, self.price)
    
    def test_trade_invalid_price(self):
        """Test the initialization of the Trade object with invalid price."""
        with self.assertRaises(ValueError):
            Trade(self.timestamp, self.quantity, self.indicator, -50.0)

    def test_trade_invalid_indicator(self):
        """Test the initialization of the Trade object with invalid indicator."""
        with self.assertRaises(ValueError):
            Trade(self.timestamp, self.quantity, "hold", self.price)

    def test_trade_invalid_timestamp(self):
        """Test the initialization of the Trade object with invalid timestamp."""
        with self.assertRaises(TypeError):
            Trade("2024-07-09", self.quantity, self.indicator, self.price)

if __name__ == '__main__':
    unittest.main()
