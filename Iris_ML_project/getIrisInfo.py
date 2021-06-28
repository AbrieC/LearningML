"""
Develop a Python application “IrisGetInfo.py” to
a. To get the number of observations, missing values, and nan (Not a Number) values of the Iris Data set.
b. To view the following statistical details of the Iris data set
• Maxim value
• minimum value
• Mean
• Median
• Standard deviation
c. To ascertain the following statistical details of each species of ‘Iris-setosa’, ‘Iris-versicolor’ and ‘Iris-versicolor’.
• Maxim value
• minimum value
• percentile
• mean
• median
• standard deviation
for (b) and (c) create a new table in your report to represent the answers in a detailed table format.
"""


import pandas as pd #allows for managing datasets

#load the iris data from a given csv file into a dataframe and
irisData = pd.read_csv('Iris.csv')

#Get the number of observations, missing values and nan(Not a Number) values.
print("\nNumber of observation, missing data, nan\n") 
print(irisData.info())

#To get observations of each species (setosa, versicolor, virginica) from iris data.
print("\nObservations of each species:\n") 
print(irisData['Species'].value_counts())

#To view basic statistical details like percentile, mean, std etc. of iris data this me adding a change to my application
print("\nStatistical Data for entire data set\n") 
print(irisData.describe())


#basic statistical details of each species
print('\nIris-setosa\n')
setosa = irisData ['Species'] == 'Iris-setosa'
print(irisData[setosa].describe())
print('\nIris-versicolor\n')
versicolor = irisData ['Species'] == 'Iris-versicolor'
print( irisData [versicolor].describe())
print('\nIris-virginica\n')
virginica = irisData['Species'] == 'Iris-virginica'
print(irisData[virginica].describe())