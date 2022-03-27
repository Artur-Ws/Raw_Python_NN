import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


dataset = pd.read_csv("datasets/Unicorn_Companies.csv")

# Print list of features
print(dataset.columns)

# Print one specific feature
print(dataset["Date Joined"])