# Iris-Project-2019

This repository contains my solutions the Project 2019 for the module Programming and Scripting at GMIT.
[See here for the instructions](https://github.com/ianmcloughlin/project-pands/raw/master/project.pdf)

## How to download this repository

1. Go to Github.
2. Click the download button.

## How to run this code

1. Make sure you have Python installed.
2. Run the Dataset.py

## Project Plan:
1. Sir Ronal Fisher and Iris dataset - brief introduction
2. Summarize the dataset
3. Data Visualiation
4. Summary
5. References


1. Sir Ronal Fisher and Iris dataset - brief introduction

Sir Ronald Aylmer Fisher, byname R.A. Fisher, (born February 17, 1890, London, England—died July 29, 1962, Adelaide, Australia) was British statistician and geneticist who pioneered the application of statistical procedures to the design of scientific experiments.

In 1936 he introduced the Iris flower data set (aka Fisher's Iris data set) which is a multivariate data set that consists of 50 samples from each of three species of Iris:
Iris setosa, Iris virginica, Iris versicolor.

Four features were measured (in cm) from each sample: 
the length of the sepals, the length of the petals
the width of the sepals, the width of the petals

Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other. 

It is worth noting that dataset is sometimes called Anderson’s Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula “all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus”

<img width="520" alt="Iris pictures" src="https://user-images.githubusercontent.com/47403763/56757773-f41af300-678c-11e9-8f4d-7f9c26d0357d.PNG">


2. Summarize the dataset
2.1 The data set contains 150 observations of iris flowers (sample of 20 lines is shown below). There are four columns of measurements of the flowers in centimeters. The fifth column is the species of the flower observed. 


2.2 All observed flowers belong to one of three species. Number of instances in each class are presented in the table below.

2.3 The statistical summary figures for each attribute include count, mean, max and min a well as some percntiles. We can see that all of the numerical values have the same scale (centimeters) and similar ranges between 0 and 8 centimeters.

2.4 The Mean, Maximum and Minimum value for each of the species are:
# Code adpoted from Stackoverflow https://stackoverflow.com/a/49970351
Mean of each of the species:
            
Minimum values for each species:

Maximum Values for each species:

3. Data Visualiation 
3.1 Histogram presentation of both sepal and petal width and length gives us an idea about the data distribution:


3.2 To see the interactions between the variables let’s look at scatterplots of all pairs of attributes. 
There is noticable diagonal grouping of some pairs of attributes. This suggests a high correlation and a predictable relationship.



4. Summry


5. References

[Britannica] https://www.britannica.com/biography/Ronald-Aylmer-Fisher
[Wikipedia] https://en.wikipedia.org/wiki/Iris_flower_data_set
[Medium Corporation] https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
[Stackoverflow] Stackoverflow https://stackoverflow.com/a/49970351
[README images in Github]
[Towards data science] https://towardsdatascience.com/pandas-dataframe-a-lightweight-intro-680e3a212b96
[Machine Learning Mastery] https://machinelearningmastery.com/machine-learning-in-python-step-by-step/