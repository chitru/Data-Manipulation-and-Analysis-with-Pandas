import pandas as pd
import matplotlib.pyplot as plt

#importing file
filepath = ('datasets/irish_life_expec.csv')
life = pd.read_csv(filepath)

#print dataframe to check
print(life)

#create scatter plot with y-axis = life expectancy and x-axis = year
life.plot(kind='scatter', x='year', y='life expec')

#adding title
plt.title('Irish Life Expectancy')

#labelling both axis
plt.xlabel('Age')
plt.ylabel('Life Expectancy')

#showing plot
plt.show()
