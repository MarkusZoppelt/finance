from matplotlib import pyplot as plt
import pandas as pd


def pieChartReport(assetAllocation):
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('equal')

    assets = ['Stocks', 'Bonds', 'Commodities',
              'Gold', 'Crypto', 'P2P', 'Cash']
    balances = assetAllocation

    ax.pie(balances, labels=assets, autopct='%1.2f%%')
    plt.show()

def cryptoReport(cryptoAllocation):
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('equal')

    assets = ['Bitcoin', 'Ether', 'Monero']
    balances = cryptoAllocation

    ax.pie(balances, labels=assets, autopct='%1.2f%%')
    plt.show()