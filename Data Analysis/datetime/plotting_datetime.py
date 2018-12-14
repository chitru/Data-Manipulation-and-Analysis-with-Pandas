import pandas as pd 
import matplotlib.pyplot as plt

#reading data
stock_price = pd.read_csv('datasets/intel.csv', parse_dates=True, index_col='Date')

#reviewing the data
# print(stock_price)

stock_price.loc['2017-10-16':'2017-10-20', ['Open', 'Close']].plot(style='.-', title='Intel Stock Price', subplots=True)
plt.ylabel('Closing Price')
plt.show() 