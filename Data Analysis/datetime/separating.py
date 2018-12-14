import pandas as pd 

#reading data
sales_data = pd.read_csv('datasets/sales_data.csv', parse_dates=True, index_col='InvoiceDate')

#reciewing datafile
# print('sales_data')

morning_sales = sales_data['Quantity']['2010-12-01']
 
high_quantity = morning_sales.resample('H').max()

print(high_quantity)