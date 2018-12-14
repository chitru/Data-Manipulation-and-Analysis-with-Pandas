import pandas as pd 

#reading file
sales_data = pd.read_csv('datasets/resampling_sales_data.csv', parse_dates=True, index_col='InvoiceDate')

#reviewing
# print(sales_data.head())

#downsampling into weekly sales | calculating mean 
#weekly average
# weekly_mean = sales_data.resample('W').mean()
#monthly average
# weekly_mean = sales_data.resample('W').mean()
# print(weekly_mean.loc['2010-02-21 ', 'Quantity'])

weekly_sum = sales_data.resample('W').sum()
print(weekly_sum)