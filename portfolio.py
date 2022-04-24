#!/usr/bin/env python

import sys
import pandas as pd
from pandas_datareader.data import get_quote_yahoo

import reports

if len(sys.argv) == 1:
    print("No args given, using example data...")
    data = pd.read_csv("example_data.csv")
else:
    if sys.argv[1].endswith(".csv"):
        data = pd.read_csv(sys.argv[1])
    elif sys.argv[1].endswith(".gpg"):
        from encryption import getDataFromEncryptedFile as GDFEF
        decryptedData = GDFEF(sys.argv[1])
        data = pd.read_csv(decryptedData)
    else:
        print("Invalid filetype")


def getQuotes(data):
    tickers = data["Ticker"]

    print("Getting current prices from Yahoo Finance...")
    balances = []

    for i in range(0, len(tickers)):
        ac = data["AC"][i]
        # If Asset Class is cash, then get amount only
        if ac == "CASH":
            balances.append(data["Amount"][i])
        else:
            try:
                currPrice = get_quote_yahoo(tickers[i])["price"][0]
                amount = data["Amount"][i]
                balances.append(round(currPrice*amount, 2))
            except Exception:
                print("No quote for this ticker")
    data["Balance"] = balances
    return data

def getTotalBalance():
    totalBalance = 0.0
    for i in range(0, len(data)):
        totalBalance += data["Balance"][i]
    return totalBalance


def getAssetAllocation():
    labels = "Stocks", "Bonds", "Commodities", "Gold", "Crypto", "Cash"
    stocks, bonds, commodities, gold, crypto, cash = 0, 0, 0, 0, 0, 0
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
        elif ac == "CASH":
            cash += data["Balance"][i]
    return labels, (stocks, bonds, commodities, gold, crypto, cash)

def getAllocationForClass(c):
    cdata = data.loc[data['AC'] == c]
    labels = []
    ticker_balances = []
    for i in range(0, len(cdata)):
        labels.append(cdata["Name"].iloc[i])
        ticker_balances.append(cdata["Balance"].iloc[i])
    return labels, ticker_balances

def analyzeAC():
    stocks, bonds, commodities, gold, crypto, cash = getAssetAllocation()[1]
    totalBalance = getTotalBalance()

    pctStocks = stocks/totalBalance * 100
    pctBonds = bonds/totalBalance * 100
    pctCommodities = commodities/totalBalance * 100
    pctGold = gold/totalBalance * 100
    pctCrypto = crypto/totalBalance * 100
    pctCash = cash/totalBalance * 100


    print("Percentage of stocks: " + str(round(pctStocks, 2))+"%")
    print("Percentage of bonds: " + str(round(pctBonds, 2))+"%")
    print("Percentage of commodities: " + str(round(pctCommodities, 2))+"%")
    print("Percentage of gold: " + str(round(pctGold, 2))+"%")
    print("Percentage of crypto: " + str(round(pctCrypto, 2))+"%")
    print("Percentage of cash: " + str(round(pctCash, 2))+"%")
    print("================================================================")

def getDataFrame(filename):
    data = pd.read_csv(filename)
    df = getQuotes(data)
    return df

def main():
    getQuotes(data)

    cmdOptions = [
        '\033[1m' + '(a)'+'\033[0m'+'nalyze',    # analyze portfolio (e.g. for market conditions)
        '\033[1m' + '(b)'+'\033[0m'+'alance',    # show balance
        '\033[1m' + '(r)'+'\033[0m'+'eports',    # show reports
        '\033[1m' + '(q)'+'\033[0m'+'uit'        # quit
    ]

    greetingText = '\033[1m' + "Hello, what do you want to do?" + '\033[0m' + " (Choose option and hit Enter)\n"
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
                  str(round(getTotalBalance(), 2))+"EUR")
            print("================================================================")
        elif cmd == "r":
            reports.plotReports(getAssetAllocation(), getAllocationForClass("S"), getAllocationForClass("CRYPTO"))


if __name__ == "__main__":
    main()
