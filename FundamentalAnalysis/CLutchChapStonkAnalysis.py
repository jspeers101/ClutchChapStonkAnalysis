import pandas as pd
from pandasgui import show
import FundamentalAnalysis as fa
import yfinance as yf


def stockratios(ticker):
    ticker = yf.Ticker(ticker)
    ratiodf = pd.DataFrame([ticker.info['shortName'],
                            ticker.info['currentPrice'],
                            ticker.info['marketCap'] / 1e9,
                            ticker.info['totalRevenue'] / 1e9,
                            ticker.info['shortPercentOfFloat']*100,
                            ticker.info['pegRatio'],
                            # ticker.info['trailingPE'],
                            ticker.info['trailingEps'],
                            ticker.info['forwardEps'],
                            ticker.info['priceToSalesTrailing12Months'],
                            ticker.info['enterpriseToEbitda'],
                            ticker.info['totalCashPerShare'],
                            ticker.info['revenueGrowth']*100])
    ratiodf = ratiodf.T
    ratiodf.columns = ['Company Name', 'Price', 'Market Cap (b)', 'Revenue (b)', 'Short %',
                       'PEG', 'EPS (TTM)', 'EPS (NTM)', 'P/S (TTM)',
                       'EV/EBITDA', 'Cash Per Share', 'Revenue Growth (%)']
    return ratiodf


stonks = pd.concat([stockratios('AAPL'),
                    stockratios('MSFT'),
                    stockratios('PLTR'),
                    stockratios('AMD'),
                    stockratios('PSFE')])
show(stonks)
