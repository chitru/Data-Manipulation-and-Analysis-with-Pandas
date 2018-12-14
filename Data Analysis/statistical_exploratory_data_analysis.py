import pandas as pd 
import matplotlib.pyplot as plt

#reading csv file
stock_prices = pd.read_csv('./datasets/tesla.csv')

# printing for review
# print(stock_prices.head())

# print using .describe method
# print(stock_prices.describe())

#printint minimum and maximum and mean value
# print(stock_prices['Open'].min())
# print(stock_prices['Open'].max())
# print(stock_prices['Open'].mean())

plt.title('Tesla Industries Stock Open Graph')
plt.xlabel('Open at')
plt.ylabel('Stock Price in $US')
stock_prices['Open'].plot(kind='box')

#conditional filtering with ooen at 315
print(stock_prices[stock_prices['Open'] == 315])

plt.show()