# Let's import some packages
import talib 
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import date
from dateutil.relativedelta import relativedelta
from tkinter import *
import streamlit as st

"""
# Stock analysis app
"""
  

StockList = ['XIT.TO', 'NVDA', 'AMD', 'MSFT', 'AAPL', 'GOOGL']

Stock = StockList[0]

# Let's download stock_data and plot it
current_date = date.today()
Start_date = current_date - relativedelta(years=1)
stock_data = yf.download(Stock, start=Start_date, end=current_date)

# To create the MACD we have to code this
macd, macdsignal, macdhist = talib.MACD(stock_data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.set_ylabel('Price')
ax1.plot(stock_data['Close'])
ax2.set_ylabel('MACD')
ax2.plot(macdsignal, color='green', label='Signal Line')
ax2.plot(macd, color='red', label='MACD')
ax2.bar(macdhist.index, macdhist, color='purple')
ax1.set_title(Stock + ' : Daily Close Price and MACD')
plt.legend()
plt.show()
