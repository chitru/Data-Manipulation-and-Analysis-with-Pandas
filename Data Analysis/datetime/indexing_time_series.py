import pandas as pd

#importing the file
sales_data = pd.read_csv('datasets/sales_data.csv', parse_dates=True, index_col='InvoiceDate')

#reviewing the file
# print(df.head())

#looking with .info() method
# print(sales_data.info())

#use .loc accessor (slicing can also be used or just selecting the year or month etc)
morning_sale = sales_data.loc['2010-12-01 08:26:00', 'Description']
print(morning_sale)