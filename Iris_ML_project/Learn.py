import pandas as pd #allows for managing datasets
#import numpy as np #allows for maths...
#import matplotlib.pyplot as plt #allows for figures

#load the iris data from a given csv file into a dataframe and
irisData = pd.read_csv('Iris.csv')

#Get the number of observations, missing values and nan(Not a Number) values.
print("Number of observation, missing data, nan") 
print(irisData.info())

#To get observations of each species (setosa, versicolor, virginica) from iris data.
print("Observations of each species:") 
print(irisData['Species'].value_counts())

#To view basic statistical details like percentile, mean, std etc. of iris data
print("Statistical Data") 
print(irisData.describe())



#to show the first few line we can use .head from pandas
#print(irisData.head())
#print(irisData.columns())
