import pandas as pd 

#reading data
sales_data = pd.read_csv('datasets/sales_data.csv', parse_dates=True, index_col='InvoiceDate')

search = sales_data['Description'].str.contains('POPPY')

total_poppy_sales = search.resample('H').sum()

print(total_poppy_sales)