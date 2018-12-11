import pandas as pd
import matplotlib.pyplot as plt

#importing dataset
stock_prices = pd.read_csv('datasets/intel_stock_price.csv')

# print(stock_prices)

#creating bar plot
stock_prices.plot(kind='bar',x='month', y='price')

#showing 
plt.show()