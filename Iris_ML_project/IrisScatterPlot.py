"""
Create a python application “IrisScatterPlot.py” to sort and create scatter plots of the data. 
•	Make use of the Iris.csv file to load data. 
•	You can only use NumPy, Matplotlib, Pandas and Seaborn. 
•	It is your choice to use the libraries as you see fit.

a.	Create a scatter plot of relationship between sepal width and length between the three classes of flower.
b.	Scatter plot of the relationship between petal length and width of the petal of the three classes of flowers.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#read iris.csv file
iris = pd.read_csv('Iris.csv')

#assign sets and plot scatter plots
iris.head()

iris.drop('Id',axis=1,inplace=True)
sns.FacetGrid(iris,hue='Species',height=5)\
.map(plt.scatter,'SepalLengthCm','SepalWidthCm')\
.add_legend()
sns.FacetGrid(iris,hue='Species',height=5)\
.map(plt.scatter,'PetalLengthCm','PetalWidthCm')\
.add_legend()

plt.show()
