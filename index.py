
from jpmorgan.gbce import GBCE
from jpmorgan.stock import Stock

# Example usage
if __name__ == "__main__":
    gbce = GBCE()
    
    stock1 = Stock(symbol="TEA", type="Common", last_dividend=0, fixed_dividend=0, par_value=100)
    stock2 = Stock(symbol="POP", type="Common", last_dividend=8, fixed_dividend=0, par_value=100)
    stock3 = Stock(symbol="GIN", type="Preferred", last_dividend=8, fixed_dividend=0.02, par_value=100)
    stock4 = Stock(symbol="ALE", type="Common", last_dividend=23, fixed_dividend=0, par_value=60)
    stock5 = Stock(symbol="JOE", type="Common", last_dividend=13, fixed_dividend=0, par_value=250)
    
    gbce.add_stock(stock1)
    gbce.add_stock(stock2)
    gbce.add_stock(stock3)
    gbce.add_stock(stock4)
    gbce.add_stock(stock5)

    stock1.record_trade(quantity=100, indicator='buy', price=110)
    stock1.record_trade(quantity=50, indicator='sell', price=115)
    stock2.record_trade(quantity=200, indicator='buy', price=120)
    stock3.record_trade(quantity=150, indicator='sell', price=130)
    stock4.record_trade(quantity=80, indicator='buy', price=95)
    stock5.record_trade(quantity=120, indicator='sell', price=140)

    price = 100
    print(f"Dividend Yield for POP: {stock2.calculate_dividend_yield(price)}")
    print(f"P/E Ratio for POP: {stock2.calculate_pe_ratio(price)}")

    vwsp_POP = stock2.calculate_volume_weighted_stock_price()
    print(f"Volume Weighted Stock Price for POP: {vwsp_POP}")

    print(f"Dividend Yield for GIN: {stock3.calculate_dividend_yield(price)}")
    print(f"P/E Ratio for GIN: {stock3.calculate_pe_ratio(price)}")

    vwsp_GIN = stock3.calculate_volume_weighted_stock_price()
    print(f"Volume Weighted Stock Price for GIN: {vwsp_GIN}")

    all_share_index = gbce.calculate_all_share_index()
    print(f"GBCE All Share Index: {all_share_index}")
