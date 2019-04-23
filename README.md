# Iris-Project-2019

This repository contains my solutions the Project 2019 for the module Programming and Scripting at GMIT.
[See here for the instructions](https://github.com/ianmcloughlin/project-pands/raw/master/project.pdf)

# About the dataset and the author

Sir Ronald Aylmer Fisher, byname R.A. Fisher, (born February 17, 1890, London, England—died July 29, 1962, Adelaide, Australia) was British statistician and geneticist who pioneered the application of statistical procedures to the design of scientific experiments.

In 1936 he introduced the Iris flower data set (aka Fisher's Iris data set) which is a multivariate data set that consists of 50 samples from each of three species of Iris:
0 Iris setosa
1 Iris virginica 
2 Iris versicolor

Four features were measured from each sample: 
1 the length of the sepals, in centimeters
2 the length of the petals, in centimeters
3 the width of the sepals, in centimeters 
4 the width of the petals, in centimeters

Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other. 

It is worth noting that dataset is sometimes called Anderson’s Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula “all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus”

References

[Britannica] https://www.britannica.com/biography/Ronald-Aylmer-Fisher
[Wikipedia] https://en.wikipedia.org/wiki/Iris_flower_data_set
[Medium Corporation] https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342


## How to download this repository

1. Go to Github.
2. Click the download button.

## How to run this code

1. Make sure you have Python installed.
2. Run the Dataset.py
# Comments:
The data set contains 150 observations of iris flowers. There are four columns of measurements of the flowers in centimeters. The fifth column is the species of the flower observed. All observed flowers belong to one of three species.
     sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  target
0                  5.1               3.5                1.4               0.2     0.0
1                  4.9               3.0                1.4               0.2     0.0
2                  4.7               3.2                1.3               0.2     0.0
3                  4.6               3.1                1.5               0.2     0.0
4                  5.0               3.6                1.4               0.2     0.0
5                  5.4               3.9                1.7               0.4     0.0
6                  4.6               3.4                1.4               0.3     0.0
7                  5.0               3.4                1.5               0.2     0.0
8                  4.4               2.9                1.4               0.2     0.0
9                  4.9               3.1                1.5               0.1     0.0
10                 5.4               3.7                1.5               0.2     0.0
11                 4.8               3.4                1.6               0.2     0.0
12                 4.8               3.0                1.4               0.1     0.0
13                 4.3               3.0                1.1               0.1     0.0
14                 5.8               4.0                1.2               0.2     0.0
15                 5.7               4.4                1.5               0.4     0.0
16                 5.4               3.9                1.3               0.4     0.0
17                 5.1               3.5                1.4               0.3     0.0
18                 5.7               3.8                1.7               0.3     0.0
19                 5.1               3.8                1.5               0.3     0.0
20                 5.4               3.4                1.7               0.2     0.0
21                 5.1               3.7                1.5               0.4     0.0
22                 4.6               3.6                1.0               0.2     0.0
23                 5.1               3.3                1.7               0.5     0.0
24                 4.8               3.4                1.9               0.2     0.0
25                 5.0               3.0                1.6               0.2     0.0
26                 5.0               3.4                1.6               0.4     0.0
27                 5.2               3.5                1.5               0.2     0.0
28                 5.2               3.4                1.4               0.2     0.0
29                 4.7               3.2                1.6               0.2     0.0
..                 ...               ...                ...               ...     ...
120                6.9               3.2                5.7               2.3     2.0
121                5.6               2.8                4.9               2.0     2.0
122                7.7               2.8                6.7               2.0     2.0
123                6.3               2.7                4.9               1.8     2.0
124                6.7               3.3                5.7               2.1     2.0
125                7.2               3.2                6.0               1.8     2.0
126                6.2               2.8                4.8               1.8     2.0
127                6.1               3.0                4.9               1.8     2.0
128                6.4               2.8                5.6               2.1     2.0
129                7.2               3.0                5.8               1.6     2.0
130                7.4               2.8                6.1               1.9     2.0
131                7.9               3.8                6.4               2.0     2.0
132                6.4               2.8                5.6               2.2     2.0
133                6.3               2.8                5.1               1.5     2.0
134                6.1               2.6                5.6               1.4     2.0
135                7.7               3.0                6.1               2.3     2.0
136                6.3               3.4                5.6               2.4     2.0
137                6.4               3.1                5.5               1.8     2.0
138                6.0               3.0                4.8               1.8     2.0
139                6.9               3.1                5.4               2.1     2.0
140                6.7               3.1                5.6               2.4     2.0
141                6.9               3.1                5.1               2.3     2.0
142                5.8               2.7                5.1               1.9     2.0
143                6.8               3.2                5.9               2.3     2.0
144                6.7               3.3                5.7               2.5     2.0
145                6.7               3.0                5.2               2.3     2.0
146                6.3               2.5                5.0               1.9     2.0
147                6.5               3.0                5.2               2.0     2.0
148                6.2               3.4                5.4               2.3     2.0
149                5.9               3.0                5.1               1.8     2.0

[150 rows x 5 columns]

Underneath the dataset there are the statistical summary figures:
            sepal length	sepal width (cm)      petal length (cm) petal width (cm)        target
count         150.000000        150.000000         150.000000        150.000000  		    150.000000
mean            5.843333          3.057333           3.758000          1.199333    			1.000000
std             0.828066          0.435866           1.765298          0.762238    			0.819232
min             4.300000          2.000000           1.000000          0.100000    			0.000000
25%             5.100000          2.800000           1.600000          0.300000    			0.000000
50%             5.800000          3.000000           4.350000          1.300000    			1.000000
75%             6.400000          3.300000           5.100000          1.800000    			2.000000
max             7.900000          4.400000           6.900000          2.500000    			2.000000

Figure 1 displays the histograms of petal and sepal length and width



