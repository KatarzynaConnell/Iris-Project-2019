# Kasia Connell, 2019
# Dataset presentation with the column headers

# Import datasets, numpy and pandas and iris dataset 
from sklearn import datasets
import numpy as np
import pandas as pd
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