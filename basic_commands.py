import pandas as pd

df = pd.read_csv("intel.csv")

#print df to view the file
#print(df)

#checking the data frame type
#print(type(df))

#checking the shape of dataframe
#print(df.shape)

#view column names
#print(df.columns)

#inspects first rows of data - default is 5
#print(df.head(10))

#inspects last rows of data - default is 5
#print(df.tail()) 

#inspects summary of dataframe
#print(df.info())

#view 'Open' column from intel.csv
#open = df['Open']
#print(open)

#print(open.head())

#view one or more columns side by side
#print(df[['Open', 'Close']].head())

#using describe method(mean, std, min, max)
#print(df.describe())