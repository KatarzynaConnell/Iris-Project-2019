# Kasia Connell, 2019
# Iris Data Analysis Project for Programming and Scripting Module

# Import Numpy library for mathematical functions
import numpy as np

# Import Pandas library to analyze the data
import pandas as pd   

# imprt matplotlib for data visualzation
import matplotlib.pyplot as plt

# To download iris dataset in the form of a Pandas DataFrame import the seaborn library
import seaborn as sns 

# Load Iris dataset using sklearn
from sklearn.datasets import load_iris

# Define Iris data as Panda Dataframe
seadf = sns.load_dataset('iris')

# Use shape command to check how many instances(rows) and attributes (columns) the set contains and what are the species proportions
# code adoped from https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
print(seadf.shape)
print(seadf.groupby('species').size())

# Use 'Head' and 'Tail' commands to print first 20 rows to see the format of data
# code adopted from https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
print(seadf.head(10))
print(seadf.tail(10))

#To give a statistical summary about the dataset (mean, maximum, minimum and devation figures)
#Code adopted from https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
print(seadf.describe()) 

#Analysis of the mean by species
#code adopted from Stackoverflow https://stackoverflow.com/a/49970351

print(seadf.groupby('species').mean())

print(seadf.groupby('species').min())

print(seadf.groupby('species').max())

# Print the histograms 
# code adopted from https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
seadf.hist()
plt.show()

# scatter plot matrix
# Verbatim code from https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

sns.pairplot(hue='species', markers="<", data = seadf, palette=['r' , 'y', 'k'])
plt.show()

# Print violinplots to visualize distribution of sepal length variables for all 3 species
# Code adopted from https://www.kaggle.com/gopaltirupur/iris-data-analysis-and-machine-learning-python
sns.violinplot(data=seadf, x='species' , y='sepal_length')
plt.show()

#  Print violinplots to visualize distribution of sepal width variables for all 3 species
sns.violinplot(data=seadf, x='species', y='sepal_width')
plt.show()

#  Print violinplots to visualize distribution of petal length variables for all 3 species
sns.violinplot(data=seadf, x='species', y='petal_length')
plt.show()

#  Print violinplots to visualize distribution of petal width variables for all 3 species
sns.violinplot(data=seadf, x='species', y='petal_width')
plt.show()