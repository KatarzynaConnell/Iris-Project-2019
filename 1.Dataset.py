# Kasia Connell, 2019
# Iris Data Analysis Project for Programming and Scripting Module

# Import Numpy library 
import numpy as np

#Import Pandas library to analyze the data
import pandas as pd   

from pandas.tools.plotting import scatter_matrix
#
import matplotlib.pyplot as plt
import seaborn as sns 

# Load Iris dataset using sklearn
from sklearn.datasets import load_iris

#Define Iris data as Panda Dataframe
seadf = sns.load_dataset('iris')

#Print Panda Dataframe
print(seadf)

#To give a statistical summary about the dataset (mean, maximum, minimum and devation figures)
#Code adopted from https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
print(seadf.describe()) 

#Analysis of the mean by species
#code adopted from Stackoverflow https://stackoverflow.com/a/49970351

print(seadf.groupby('species').mean())

print(seadf.groupby('species').min())

print(seadf.groupby('species').max())

# Print the histograms 
seadf.hist()
plt.show()

# scatter plot matrix
scatter_matrix(seadf)
plt.show()