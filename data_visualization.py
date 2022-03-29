import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


dataset = pd.read_csv("datasets/Unicorn_Companies.csv")

sep = ' - '

# Print list of features
print(dataset.columns)
#
# # Print one specific feature
# print(dataset["Date Joined"])
#
# # Print list of all elements for specific feature one by one
# for col in dataset.columns:
#     print(dataset[col])
#
# # Print which year the oldest company on the list was founded
# print(dataset['Founded Year'].min())
#
# # Print general info about dataset
# print(dataset.describe())
#
# # Print info about data in dataset
# print(dataset.info())

# Print specific info about Companies from specific country
for index, row in dataset.iterrows():
    if row['Country'] == 'Germany':
        print(index, sep, row['Founded Year'], sep, row['Valuation ($B)'], sep, row['Company'], sep, row['Industry'])