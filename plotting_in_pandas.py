import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('intel.csv', index_col='Date', parse_dates=True)

#close_value = df['Close'].values

# print(type(close_value))

#numpyplot
# plt.plot(close_value)
# plt.show() 

#only one cloumn in the graph
#df['Close'].plot(color='g', style='-', legend=True)
#plt.axis(('2017', '2018', 0, 60))

df.plot(color='blue')
plt.title('Stock Price')
plt.xlabel('Date')
plt.ylabel('Price')

#plt.show() 
# Saving as png, jpg, pdf
plt.savefig('df.png')