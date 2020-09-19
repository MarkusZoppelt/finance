# Finance

A simple command line tool for managing private financial investment portfolios

Install requirements:

    pip install -r requirements.txt

Usage:

    ./portfolio.py <data.csv>

Example data can be found in [`example_data.csv`](/example_data.csv)

Check your portfolio balance:

```
Hello Sir, what do you want to do? (a)nalyze, (b)alance, (q)uit: b
================================================================
                Name   Ticker      AC  Amount  Balance
0         NASDAQ 100      QQQ       S    4.00  1036.32
1  US Treasury 20+yr      TLT       B    4.00   680.04
2        Commodities      GSG       C    1.00    10.82
3               Gold      GLD       G    1.00   182.54
4            Bitcoin  BTC-USD  CRYPTO    0.05   554.73
5               Cash        -    CASH  200.00   200.00
Your total balance is: 2664.45€
================================================================
```

Analyze your portfolio:

```
Hello Sir, what do you want to do? (a)nalyze, (b)alance, (q)uit: a
================================================================
Percentage of stocks: 38.89%
Percentage of bonds: 25.52%
Percentage of commodities: 0.41%
Percentage of gold: 6.85%
Percentage of crypto: 20.82% (optimal: 1% - 10%)
Percentage of P2P: 0.0%
Percentage of cash: 7.51%
----------------------------------------------------------------
Prepared for market situations:
Normal: 38.89
Inflation: 28.08
Deflation: 33.03
================================================================

```

Bonus: GPG Encryption

This tool supports (gpg) encrypted csv files for secure sync between platforms via, e.g., git.
Decrypted values are never written to disk.

    # you will need a valid gpg key in ~/.gnupg/
    ./portfolio.py data.gpg

Pro Tip: Use a plugin like [vim-gnupg](https://github.com/jamessan/vim-gnupg) for editing your data file.
