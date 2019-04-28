# Iris-Project-2019

This repository contains my solutions the Project 2019 for the module Programming and Scripting at GMIT.
[See here for the instructions](https://github.com/ianmcloughlin/project-pands/raw/master/project.pdf)

## How to download this repository

1. Go to Github.
2. Click the download button.

## How to run this code

1. Make sure you have Python installed.
2. Run the Dataset.py

## Project plan

1. Sir Ronal Fisher and Iris dataset - brief introduction
2. Dataset summary
3. Data Visualiation
4. Summary
5. References



### 1. Sir Ronal Fisher and Iris dataset - brief introduction

Sir Ronald Aylmer Fisher, byname R.A. Fisher, (born February 17, 1890, London, England—died July 29, 1962, Adelaide, Australia) was British statistician and geneticist who pioneered the application of statistical procedures to the design of scientific experiments.

In 1936 he introduced the Iris flower data set (aka Fisher's Iris data set) which is a multivariate data set that consists of 50 samples from each of three species of Iris:
Iris setosa, Iris virginica, Iris versicolor.

Four features were measured (in cm) from each sample: 
the length of the sepals, the length of the petals
the width of the sepals, the width of the petals

Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other. 

It is worth noting that dataset is sometimes called Anderson’s Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula “all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus”

<img width="520" alt="Iris pictures" src="https://user-images.githubusercontent.com/47403763/56757773-f41af300-678c-11e9-8f4d-7f9c26d0357d.PNG">


### 2. Dataset Summary

2.1 The data set contains 150 observations of iris flowers (sample of first and last 10 lines is shown below). There are four columns of measurements of the flowers in centimeters. The fifth column is the species of the flower observed. 

<img width="393" alt="Data_sample" src="https://user-images.githubusercontent.com/47403763/56863832-4fc6c580-69b3-11e9-8400-87ac44bcd959.PNG">

2.2 The statistical summary figures for each attribute include count, mean, max and min a well as some percntiles. We can see that all of the numerical values have the same scale (centimeters) and similar ranges between 0 and 8 centimeters.

<img width="353" alt="Column_stats" src="https://user-images.githubusercontent.com/47403763/56864216-c2d23b00-69b7-11e9-9f13-9d79d4eb0cea.PNG">

2.3 The Mean, Maximum and Minimum value for each of the species give us better understanding of the size attributes of each specie:

Mean of each of the species:

<img width="363" alt="Species_Mean" src="https://user-images.githubusercontent.com/47403763/56864233-f745f700-69b7-11e9-92d0-d2c18a6f66ce.PNG">

Minimum values for each species are presented below:

<img width="361" alt="Species_Min" src="https://user-images.githubusercontent.com/47403763/56864251-29575900-69b8-11e9-93fd-980111035aef.PNG">

Maximum Values for each species:

<img width="361" alt="Species_Max" src="https://user-images.githubusercontent.com/47403763/56864240-104ea800-69b8-11e9-9f80-1bceaf8a9ab8.PNG">


3. Data Visualiation 
3.1 Histogram presentation of both sepal and petal width and length gives us an idea about the data distribution:

![Figure_1](https://user-images.githubusercontent.com/47403763/56864311-de8a1100-69b8-11e9-91b2-ada58a5b833a.png)

3.2 To see the interactions between the variables let’s look at scatterplots of all pairs of attributes. 
There is noticable diagonal grouping of some pairs of attributes. This suggests a high correlation and a predictable relationship.

![Scatter_Matrix](https://user-images.githubusercontent.com/47403763/56864321-fbbedf80-69b8-11e9-9586-f90ac2b44c5b.png)



4. Summary


5. References

[Britannica] https://www.britannica.com/biography/Ronald-Aylmer-Fisher
[Wikipedia] https://en.wikipedia.org/wiki/Iris_flower_data_set
[Medium Corporation] https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
[Stackoverflow] Stackoverflow https://stackoverflow.com/a/49970351
[README images in Github]
[Towards data science] https://towardsdatascience.com/pandas-dataframe-a-lightweight-intro-680e3a212b96
[Machine Learning Mastery] https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
[Matpotlib markers] https://matplotlib.org/api/markers_api.html
