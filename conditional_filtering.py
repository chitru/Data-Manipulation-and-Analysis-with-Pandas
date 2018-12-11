import pandas as pd

df = pd.read_csv('intel.csv')

#print(df)

#my_open = df['Open'] > 40
#print(my_open)

#print(df[my_open])

print(df[df['Open'] <= 55.8 ])