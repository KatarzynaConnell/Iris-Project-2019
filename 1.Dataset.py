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

#Print first 20 rows to see the format of data
print(seadf.head(20))

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
plt.savefig('Figure_1.png')
plt.show()

# scatter plot matrix
# Verbatim code from https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

sns.pairplot(hue='species', markers="<", data = seadf, palette=['r' , 'y', 'k'])
plt.show()
