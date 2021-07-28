
import pandas as pd
from pandasgui import show
import FundamentalAnalysis as fa
import yfinance as yf

tickerList = ['MSFT', 'AAPL', 'GOOG']
print(tickerList)
tickerData = yf.download(tickerList, period="1d")
print(tickerData)

