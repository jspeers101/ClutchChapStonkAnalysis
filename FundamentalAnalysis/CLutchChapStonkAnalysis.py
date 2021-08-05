import pandas as pd
from pandasgui import show
import FundamentalAnalysis as fa
import yfinance as yf


def stockratios(ticker):
    # ratioDf = pd.DataFrame(columns=['peg', 'trailingpe', 'ebitda'])
    ticker = yf.Ticker(ticker)
    ratiodf = pd.DataFrame([ticker.info['pegRatio'], ticker.info['trailingPE'], ticker.info['ebitda']])
    ratiodf = ratiodf.T
    ratiodf.columns = ['PEG', 'PE (TTM)', 'EBITDA']
    return ratiodf


aapl = stockratios('AAPL')
show(aapl)
