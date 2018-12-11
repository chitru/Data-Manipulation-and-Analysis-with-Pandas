import pandas as pd

df = pd.read_csv('intel.csv')

open = df['Open']
#Series type
#print(type(open))  

#converting the series into ndarray
new_open = open.values
print(new_open)

#looking at data types
# print(type(new_open))