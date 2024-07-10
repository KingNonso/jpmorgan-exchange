# Super Simple Stock Market

## To run the tests

```
python -m unittest discover -s tests
```

## Potential Edge Cases

- Invalid Prices:

Negative or zero prices provided for dividend yield and P/E ratio calculations.

- Invalid Quantities:

Negative or zero quantities when recording trades.

- Invalid Indicators:

Indicators other than "buy" or "sell" when recording trades.

- No Trades:

Calculating the volume-weighted stock price or all-share index when there are no trades recorded.

- Trades Older than 5 Minutes:

Only include trades within the last 5 minutes for volume-weighted stock price calculation.

- Zero or Negative Dividends:

Dividends of zero or less for P/E ratio calculations, potentially leading to infinite or undefined ratios.

- Empty Stock List:

Calculating the all-share index when no stocks are present.

- Mixed Trades:

Ensure the system correctly handles stocks with a mix of trades within and outside the 5-minute window.
