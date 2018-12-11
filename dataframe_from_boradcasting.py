import pandas as pd

counties = ['Antrim','Armagh','Carlow','Cavan','Clare','Cork','Derry','Donegal','Down','Dublin','Fermanagh','Galway',
            'Kerry','Kildare','Kilkenny','Laois','Leitrim','Limerick','Longford','Louth','Mayo','Meath','Monaghan',
            'Offaly','Roscommon','Sligo','Tipperary','Tyrone','Waterford','Westmeath','Wexford','Wicklow']

#creating a string with value ireland
country = 'IRELAND'

#new dictionary
ireland = {'Country': country, 'County': counties}

#creating a dataframe
df = pd.DataFrame(ireland)

print(df)