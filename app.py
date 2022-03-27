#!/usr/bin/python

from tkinter import filedialog
from tkinter import *
from pandastable import Table
import pandas as pd

import portfolio


class App(Frame):
	def __init__(self, parent=None):
		self.parent = parent
		Frame.__init__(self)
		self.main = self.master
		self.main.geometry('1200x800+400+200')
		self.main.title('Finance App')
		f = Frame(self.main)
		f.pack(fill=BOTH,expand=1)

		filename = filedialog.askopenfilename(initialdir = "~/",title="Please select data file", filetypes=(("csv files", "*.csv"), ("encrypted files", "*.gpg")))

		if filename.endswith(".csv"):
 			df = portfolio.getDataFrame("/home/mz/code/finance/example_data.csv")
		else:
 			from encryption import getDataFromEncryptedFile as GDFEF
 			decryptedData = GDFEF(filename)
 			df = portfolio.getDataFrame(pd.read_csv(decryptedData))


		self.table = pt = Table(f, dataframe=df,
								showtoolbar=False, showstatusbar=False)
		pt.show()
		return


app = App()
app.mainloop()
