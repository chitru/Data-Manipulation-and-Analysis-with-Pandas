import pandas as pd 
import matplotlib.pyplot as plt

#reading file
play_data = pd.read_csv('datasets/googleplaystore.csv')

#review reading
# print(play_data)

#printing all reviews greater or equal to 5
# print(play_data[play_data['Rating'] >= 5])

#create a conditional filter to find 'Arcade' in Genre column
# arcade_data = play_data[play_data['Genres'] == 'Arcade']
# print(arcade_data)
