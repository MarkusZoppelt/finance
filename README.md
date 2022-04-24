# Finance

A simple command line tool for managing personal financial investment portfolios

Install requirements:

    pip install -r requirements.txt

Usage:

    ./portfolio.py <data.csv>

Example data can be found in [`example_data.csv`](/example_data.csv)

Check your portfolio balance:

```
================================================================
                Name   Ticker      AC  Amount  Balance
0            S&P 500      SPY       S    2.00   852.08
1  US Treasury 20+yr      TLT       B    4.00   479.96
2        Commodities      GSG       C    3.00    70.05
3               Gold      GLD       G    1.00   180.29
4            Bitcoin  BTC-USD  CRYPTO    0.01   396.30
5               Cash        -    CASH  200.00   200.00
Your total balance is: 2178.68EUR
================================================================
```

Analyze your portfolio:

```
================================================================
Percentage of stocks: 39.11%
Percentage of bonds: 22.03%
Percentage of commodities: 3.22%
Percentage of gold: 8.28%
Percentage of crypto: 18.19%
Percentage of cash: 9.18%
================================================================
```

Bonus: GPG Encryption

This tool supports (gpg) encrypted csv files for secure sync between platforms via, e.g., git.
Decrypted values are never written to disk.

    # you will need a valid gpg key in ~/.gnupg/
    ./portfolio.py data.gpg

Pro Tip: Use a plugin like [vim-gnupg](https://github.com/jamessan/vim-gnupg) for editing your data file.
