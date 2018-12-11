import pandas as pd
import matplotlib.pyplot as plt

#importing the file
df = pd.read_csv('datasets/intel_amd_stock_prices.csv')

#y-columns
y_columns = ['intel', 'amd']

#assigning names
df.plot(x='month', y=y_columns)

#giving title 
plt.title('Monthly Stock Prices')

plt.ylabel('Prices ($US)')

plt.show()