import pandas as pd

course_sales = { 'course': ['Python', 'Ruby', 'Excel', 'C++'],
                'day':['Mon', 'Tue', 'Wed', 'Fri' ],
                'price': [5, 10, 15, 20],
                'sale': [2,3,4,5]
                }

#print(course_sales)

# df_sales = pd.DataFrame(course_sales)
# print(df_sales)

# Create indidivdual lists from sales data
course = ['Python','Ruby','Excel','C++']

day = ['Mon', 'Tue', 'Tue', 'Wed']

price = [5,10,15,20]

sale = [2,3,5,7]

labels = ['Course', 'Day', 'Price', 'No. of Sales']

cols = [ course, day, price, sale ]

master_list = list(zip(labels, cols))
#print(master_list)

data = dict(master_list)

#data dictionary to dataframe
df_sales = pd.DataFrame(data)
print(df_sales)
# print(type(df_sales))


# adding new column in the data
#df_sales['New_price'] = 2 
#print(df_sales)

#creating new labels
columns_labels = ['Course', 'Day', 'Price', '24HR Sale Price']

df_sales.columns = columns_labels

print(df_sales)