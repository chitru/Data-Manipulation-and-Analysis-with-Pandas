import pandas as pd

column_names = ['Apps', 'Rating', 'Reviews', 'Size', '# of Installs', 'Types', 'Price', 'Last Updated']
fielpath = ('edited_googleplaystore_dataset.csv')
df = pd.read_csv(fielpath, header=None, names=column_names, na_values='-1')

#indexing with Last Updated Column
df.index = df['Last Updated']

new_column = ['Apps', 'Reviews']

df = df[new_column]
 
#print(df.info())
#print(df.tail())

#exporting cleaned file
out_csv = 'GooglePlayStoreData'
df.to_csv(out_csv)

#exorting to excel file
out_xlsx = 'GooglePLayDataEXCEL.xlsx'
df.to_excel(out_xlsx)