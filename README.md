# Iris-Project-2019

This repository contains my solutions the Project 2019 for the module Programming and Scripting at GMIT.
[See here for the instructions](https://github.com/ianmcloughlin/project-pands/raw/master/project.pdf)

# Project Plan:
1. Sir Ronal Fisher and Iris dataset - brief introduction
2. Presentation of the dataset with the column headers
3. Statistical summary of each column
4. Mean, maximum and minimum of each of the species
5. Histogram presentation of both sepal and petal width and length
6. Summary
7. References

## How to download this repository

1. Go to Github.
2. Click the download button.

## How to run this code

1. Make sure you have Python installed.
2. Run the Dataset.py

1. Sir Ronal Fisher and Iris dataset - brief introduction

Sir Ronald Aylmer Fisher, byname R.A. Fisher, (born February 17, 1890, London, England—died July 29, 1962, Adelaide, Australia) was British statistician and geneticist who pioneered the application of statistical procedures to the design of scientific experiments.

In 1936 he introduced the Iris flower data set (aka Fisher's Iris data set) which is a multivariate data set that consists of 50 samples from each of three species of Iris:
Iris setosa, Iris virginica, Iris versicolor.

Four features were measured (in cm) from each sample: 
the length of the sepals, the length of the petals
the width of the sepals, the width of the petals

Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other. 

It is worth noting that dataset is sometimes called Anderson’s Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula “all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus”

![screenshot] https://user-images.githubusercontent.com/47403763/56757773-f41af300-678c-11e9-8f4d-7f9c26d0357d.PNG

References

[Britannica] https://www.britannica.com/biography/Ronald-Aylmer-Fisher
[Wikipedia] https://en.wikipedia.org/wiki/Iris_flower_data_set
[Medium Corporation] https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
[Stackoverflow] Stackoverflow https://stackoverflow.com/a/49970351


2. Presentation of the dataset with the column headers
The data set contains 150 observations of iris flowers. There are four columns of measurements of the flowers in centimeters. The fifth column is the species of the flower observed. All observed flowers belong to one of three species.


|     sepal length (cm) | sepal width (cm)  | petal length (cm) | petal width (cm) | target |
|      :---:                   :---:               :---:             :---:           :---:
|0                  5.1 |              3.5  |              1.4  |            0.2   |  0.0   |
--------------------------------------------------------------------------------------------|
1                  4.9 |              3.0  |              1.4  |            0.2   |  0.0   |
|2                  4.7 |              3.2  |              1.3  |            0.2   |  0.0   |
|3                  4.6 |              3.1  |              1.5  |            0.2   |  0.0   |
|4                  5.0 |              3.6  |              1.4  |            0.2   |  0.0   |
|                       |                   |                   |                  |        |
|..                 ... |              ...  |              ...  |             ...  |   ...  |
|                       |                   |                   |                  |        |
|145                6.7 |              3.0  |              5.2  |             2.3  |   2.0  |
|146                6.3 |              2.5  |              5.0  |             1.9  |   2.0  |
|147                6.5 |              3.0  |              5.2  |             2.0  |   2.0  |
|148                6.2 |              3.4  |              5.4  |             2.3  |   2.0  |
|149                5.9 |              3.0  |              5.1  |             1.8  |   2.0  |
--------------------------------------------------------------------------------------------


[150 rows x 5 columns]

3. Statistical summary of each column
Underneath the dataset there are the statistical summary figures for each column:
            sepal length	sepal width (cm)      petal length (cm) petal width (cm)        target
count         150.000000        150.000000         150.000000        150.000000  		    150.000000
mean            5.843333          3.057333           3.758000          1.199333    			1.000000
std             0.828066          0.435866           1.765298          0.762238    			0.819232
min             4.300000          2.000000           1.000000          0.100000    			0.000000
25%             5.100000          2.800000           1.600000          0.300000    			0.000000
50%             5.800000          3.000000           4.350000          1.300000    			1.000000
75%             6.400000          3.300000           5.100000          1.800000    			2.000000
max             7.900000          4.400000           6.900000          2.500000    			2.000000

4. Statitical summary for each species:
# Code adpoted from Stackoverflow https://stackoverflow.com/a/49970351
Mean of each of the species:
            
Species        sepal_length  sepal_width  petal_length  petal_width
setosa             5.006        3.428         1.462        0.246
versicolor         5.936        2.770         4.260        1.326
virginica          6.588        2.974         5.552        2.026

Minimum values for each species:
Species          sepal_length  sepal_width  petal_length  petal_width

setosa               4.3          2.3           1.0          0.1
versicolor           4.9          2.0           3.0          1.0
virginica            4.9          2.2           4.5          1.4

Maximum Values for each species:
            sepal_length  sepal_width  petal_length  petal_width
species
setosa               5.8          4.4           1.9          0.6
versicolor           7.0          3.4           5.1          1.8
virginica            7.9          3.8           6.9          2.5

5. Histogram presentation of both sepal and petal width and length



