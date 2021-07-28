
import pandas as pd
from pandasgui import show
import FundamentalAnalysis as fa

df = pd.DataFrame({'a':[1,2,3], 'b':[4,5,6], 'c':[7,8,9]})
show(df)


msft = yf.Ticker("MSFT")