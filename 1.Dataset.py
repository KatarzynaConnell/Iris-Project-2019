# Kasia Connell, 2019
# Present the Dataset with the column headers

# Import datasets, numpy, pandas, pyplot and iris dataset to present dataset and analyze content
from sklearn import datasets
import numpy as np
import pandas as pd   
import matplotlib.pyplot as plt      
from sklearn.datasets import load_iris
data = datasets.load_iris()
digits = datasets.load_digits()

# Check the types of the features and response
type('data.data')
type('data.target')

df = pd.DataFrame(np.column_stack((data.data, data.target)), columns = data.feature_names+['target'])

data1 = pd.DataFrame(data= np.c_[data['data'], data['target']],
                 columns= list(data['feature_names']) + ['target'])
print(data1)

print(data1.describe()) #to give a statistical summary about the dataset (mean, maximum, minimum and devation figures)

print(df.isnull().sum()) #checks out how many null info are on the dataset

data1.hist()
plt.show()
