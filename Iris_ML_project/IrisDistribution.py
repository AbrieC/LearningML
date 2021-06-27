"""
Get back to the basics with numpy to create arrays and manage data.
Create a python application “IrisDistibution.py” to create distribution plots 
(Histograms) to visually assess how the data points are distributed with 
respect to its frequency of occurrence between the three classes of flowers for:
•	Make use of the Iris.csv file to load data. 
>> I made use of sklearn instead
•	You can only use NumPy and Matplotlib. 
•	Make sure to add different colours for each label.

#a.	Petal length
#b.	Petal width
#c.	Sepal length
#d.	Sepal width
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

#load the iris dataset
iris = load_iris() 
print("Keys:", iris.keys()) # print keys of dataset

#acquiring the bin sizes for the histograms
print("Bin counts for targets:", np.bincount(iris.target))

print("Feature names:", iris.feature_names)
print("Target names:", iris.target_names)

#setting the colours for the different species 
colors = ['blue', 'red', 'green']

# plot histogram
for feature in range(iris.data.shape[1]): # (shape = 150, 4)
    plt.subplot(2, 2, feature+1) # subplot starts from 1 (not 0)
    for label, color in zip(range(len(iris.target_names)), colors):
        # find the label and plot the corresponding data
        plt.hist(iris.data[iris.target==label, feature],
                 label=iris.target_names[label],
                 color=color)
    plt.xlabel(iris.feature_names[feature])
    plt.legend()
plt.show()