from matplotlib import pyplot as plt
import pandas as pd


def plotReports(assets, stocks, crypto):
	f1 = plt.figure(1)
	ax1 = f1.add_axes([0, 0, 1, 1])
	ax1.axis('equal')
	
	ax1.pie(assets[1], labels=assets[0], autopct='%1.2f%%')


	f2 = plt.figure(2)
	ax2 = f2.add_axes([0, 0, 1, 1])
	ax2.axis('equal')
	ax2.pie(stocks[1], labels=stocks[0], autopct='%1.2f%%')


	f3 = plt.figure(3)
	ax3 = f3.add_axes([0, 0, 1, 1])
	ax3.axis('equal')
	ax3.pie(crypto[1], labels=crypto[0], autopct='%1.2f%%')

	plt.show()
