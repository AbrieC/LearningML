import pandas as pd #allows for managing datasets
import numpy as np #allows for maths...
import matplotlib.pyplot as plt #allows for figures


"""
1. Loading data with pandas, then testing if we have succesfully loaded the data. And manipulating the data further with arrays.

"""
#load the iris data from a given csv file into a dataframe and
data = pd.read_csv('Iris.csv')

#1.1. to show the first few line we can use .head from pandas
print('first few lines of dataset\n', data.head())


#1.2. to create the array = data[start:end], remember START is inclusive whereas END is exclusive
print('first 20 lines of data set\n',data[0:2])



#1.3/ print first three colums
#x = data.iloc[:, 0:3].values
#print('\n First three columsn', x) 

#x = data.iloc[:, [1, 2, 3, 4]].values
#print(x) 

#sepalLenght = np.array(x[1:])
#print(sepalLenght)

#remove the id column
#new_data = data.drop('Id',axis=1)
#print("After removing id column:")
#print(new_data.head())



"""
2. for displaying only specific columns
"""
#to access specefic data from array we can make use of data[["column_name1","column_name2","column_name3"]]

#specific_data = data[["Id","Species"]]

#now we will print the first 20 rows of the specific_data dataframe.*(remember we start at ID 1)

#print('\n Specefic data\n', specific_data.head(20))




"""
# /*3. Create row vector to catpure all setosaSepallenghts only using numpy
# and calculate average, mean, etc. https://numpy.org/devdocs/reference/generated/numpy.average.html?highlight=average#numpy.average
"""

#specificData = np.array(data[:])
#setosaSepalL = specificData[:50, 1]

# Create matrix
# matrix = np.array([[1, 2, 3],
#                   [4, 5, 6],
#                   [7, 8, 9]])

#print(setosaSepalL)

#with old school maths
#sumSSL = sum(setosaSepalL)
#averageMath = sumSSL/50

#with np
#npAVGSSL = np.average(setosaSepalL)

#print the results
#print(sumSSL)
#print(averageMath)
#print(npAVGSSL)


##WORKING with PANDAS
"""
#/* 4. for filtering, work with specific data, and plotting
"""
#Displaying the specific rows using “iloc” and “loc”
#print(data.iloc[5])


#specific_data = irisData[["SepalLengthCm"]]

#print only the Setosa data
#print(specific_data.head(51))

#specific_data.plot()
#plt.show()
#*/

"""
*5. Print the shape of the data, type of the data and first 3 rows.
"""
#print("Shape of the data:")
#print(irisData.shape)
#print("\nData Type:")
#print(type(irisData))
#print("\nFirst 3 rows:")
#print(irisData.head(3))


"""
6. get the number of observations, missing values and nan values.
"""
#print(irisData.info())


"""
7. Statistical info
"""
"""
#basic statistical details of each species
print('Iris-setosa')
setosa = irisData ['Species'] == 'Iris-setosa'
print(irisData[setosa].describe())
print('\nIris-versicolor')
versicolor = irisData ['Species'] == 'Iris-versicolor'
print( irisData [versicolor].describe())
print('\nIris-virginica')
virginica = irisData['Species'] == 'Iris-virginica'
print(irisData[virginica].describe())
"""
