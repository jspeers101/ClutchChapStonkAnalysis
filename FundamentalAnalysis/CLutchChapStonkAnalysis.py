
import pandas as pd
from pandasgui import show
import FundamentalAnalysis as fa
import yfinance as yf

tickerList = ['MSFT', 'AAPL', 'GOOG']
print(tickerList)
tickerData = yf.Ticker(tickerList[1])
print(tickerData)
print(tickerData.info['revenuePerShare'])


