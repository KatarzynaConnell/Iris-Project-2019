# Kasia Connell, 2019
# Present the Dataset with the column headers
# Code adopted from 

# Import datasets, numpy, pandas, pyplot and iris dataset to present dataset and analyze content
from sklearn import datasets
import numpy as np
import pandas as pd   
import matplotlib.pyplot as plt
import seaborn as sns      
from sklearn.datasets import load_iris
data = datasets.load_iris()
digits = datasets.load_digits()
seadf = sns.load_dataset('iris')

# Check the types of the features and response
type('data.data')
type('data.target')

df = pd.DataFrame(np.column_stack((data.data, data.target)), columns = data.feature_names+['target'])

data1 = pd.DataFrame(data= np.c_[data['data'], data['target']],
                 columns= list(data['feature_names']) + ['target'])
print(data1)

# To give a statistical summary about the dataset (mean, maximum, minimum and devation figures)
# Code adopted from https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
print(data1.describe()) 

print(df.isnull().sum()) #checks out how many null info are on the dataset
# Analysis of the mean by species
# code adopted from Stackoverflow https://stackoverflow.com/a/49970351

print(seadf.groupby('species').mean())

print(seadf.groupby('species').min())

print(seadf.groupby('species').max())

data1.hist()
plt.show()
