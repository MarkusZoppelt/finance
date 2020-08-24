#!/usr/bin/env python

import sys
import getopt
import pandas as pd
from pandas_datareader.data import get_quote_yahoo
from termcolor import colored
import reports

if len(sys.argv) == 1:
    print("No args given, using example data...")
    data = pd.read_csv("example_data.csv")
else:
    data = pd.read_csv(sys.argv[1])


def getQuotes():
    tickers = data["Ticker"]

    print("Getting current prices from Yahoo Finance...")
    balances = []

    for i in range(0, len(tickers)):
        ac = data["AC"][i]
        # If Asset Class is cash, then get amount only
        if ac == "CASH" or ac == "P2P":
            balances.append(data["Amount"][i])
        else:
            try:
                currPrice = get_quote_yahoo(tickers[i])["price"][0]
                amount = data["Amount"][i]
                balances.append(round(currPrice*amount, 2))
            except Exception:
                print("No quote for this ticker")
    data["Balance"] = balances


def getTotalBalance():
    totalBalance = 0.0
    for i in range(0, len(data)):
        totalBalance += data["Balance"][i]
    return totalBalance


def getAssetAllocation():
    stocks, bonds, commodities, gold, crypto, p2p, cash = 0, 0, 0, 0, 0, 0, 0
    for i in range(0, len(data)):
        ac = data["AC"][i]

        if ac == "S":
            stocks += data["Balance"][i]
        elif ac == "B":
            bonds += data["Balance"][i]
        elif ac == "C":
            commodities += data["Balance"][i]
        elif ac == "G":
            gold += data["Balance"][i]
        elif ac == "CRYPTO":
            crypto += data["Balance"][i]
        elif ac == "P2P":
            p2p += data["Balance"][i]
        elif ac == "CASH":
            cash += data["Balance"][i]
    return stocks, bonds, commodities, gold, crypto, p2p, cash

def getCryptoAllocation():
    bitcoin, ether, monero = 0,0,0

    for i in range(0, len(data)):
        ticker = data["Ticker"][i]
        
        if ticker == "BTC-EUR":
            bitcoin += data["Balance"][i]
        elif ticker == "ETH-EUR":
            ether += data["Balance"][i]
        elif ticker == "XMR-EUR":
            monero += data["Balance"][i]
    return bitcoin, ether, monero


def analyzeAC():
    stocks, bonds, commodities, gold, crypto, p2p, cash = getAssetAllocation()
    totalBalance = getTotalBalance()

    pctStocks = stocks/totalBalance * 100
    pctBonds = bonds/totalBalance * 100
    pctCommodities = commodities/totalBalance * 100
    pctGold = gold/totalBalance * 100
    pctCrypto = crypto/totalBalance * 100
    pctP2P = p2p/totalBalance * 100
    pctCash = cash/totalBalance * 100

    cryptoStr = ""
    if pctCrypto < 1 or pctCrypto > 10:
        cryptoStr = colored(str(round(pctCrypto, 2))+"%",
                            "red") + " (optimal: 1% - 10%)"
    else:
        cryptoStr = str(round(pctCrypto, 2))+"%"

    commoditiesStr = ""
    if pctCommodities > 7.5:
        commoditiesStr = colored(
            str(round(pctCommodities, 2))+"%", "red") + " (optimal: 0% - 7.5%)"
    else:
        commoditiesStr = str(round(pctCommodities, 2))+"%"

    goldStr = ""
    if pctGold < 5 or pctGold > 10:
        goldStr = colored(str(round(pctGold, 2))+"%",
                          "red") + " (optimal: 5% - 10%)"
    else:
        goldStr = str(round(pctGold, 2))+"%"

    p2pStr = ""
    if pctP2P > 10:
        p2pStr = colored(str(round(pctP2P, 2))+"%", "red") + \
            " (optimal: 0% - 10%)"
    else:
        p2pStr = str(round(pctP2P, 2))+"%"

    print("Percentage of stocks: " + str(round(pctStocks, 2))+"%")
    print("Percentage of bonds: " + str(round(pctBonds, 2))+"%")
    print("Percentage of commodities: " + commoditiesStr)
    print("Percentage of gold: " + goldStr)
    print("Percentage of crypto: " + cryptoStr)
    print("Percentage of P2P: " + p2pStr)
    print("Percentage of cash: " + str(round(pctCash, 2))+"%")
    print("----------------------------------------------------------------")
    print("Prepared for market situations:")
    print("Normal: " + str(round(pctStocks, 2)))
    print("Inflation: " + str(round(pctCommodities + pctGold + pctCrypto, 2)))
    print("Deflation: " + str(round(pctBonds + pctCash + pctP2P, 2)))

    print("================================================================")


def main():
    getQuotes()

    cmdOptions = [
        '\033[1m' + '(a)'+'\033[0m'+'nalyze',    # analyze portfolio (e.g. for market conditions)
        '\033[1m' + '(b)'+'\033[0m'+'alance',    # show balance
        '\033[1m' + '(r)'+'\033[0m'+'eports',    # show reports
        '\033[1m' + '(q)'+'\033[0m'+'uit'        # quit
    ]

    greetingText = '\033[1m' + "🎩 Hello Sir, what do you want to do?" + '\033[0m' + " (Choose option and hit Enter)\n"
    for co in cmdOptions:
           greetingText += "  " + co+"\n"
    greetingText += ">"

    cmd = ""

    while cmd != "q":
        cmd = input(greetingText)

        print("================================================================")

        if cmd == "a":
            analyzeAC()
        elif cmd == "b":
            print(data)
            print("Your total balance is: " +
                  str(round(getTotalBalance(), 2))+"€")
            print("================================================================")
        elif cmd == "r":
            reports.pieChartReport(getAssetAllocation())
        elif cmd == "cr":
            reports.cryptoReport(getCryptoAllocation())


if __name__ == "__main__":
    main()
