# Kasia Connell, 2019
# Present the Dataset with the column headers
# Code adopted from 

# Import datasets, numpy, pandas, pyplot and iris dataset to present dataset and analyze content

import numpy as np
import pandas as pd   
import matplotlib.pyplot as plt
import seaborn as sns 

# Load Iris dataset
from sklearn.datasets import load_iris

seadf = sns.load_dataset('iris')

#Print the dataset
print(seadf)

#To give a statistical summary about the dataset (mean, maximum, minimum and devation figures)
#Code adopted from https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
print(seadf.describe()) 

#Analysis of the mean by species
#code adopted from Stackoverflow https://stackoverflow.com/a/49970351

print(seadf.groupby('species').mean())

print(seadf.groupby('species').min())

print(seadf.groupby('species').max())

seadf.hist()
plt.show()
