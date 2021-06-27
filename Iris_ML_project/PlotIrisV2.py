from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load some data
iris = datasets.load_iris()
#iris =  pd.read_csv("Iris.csv")
iris_df = pd.DataFrame(iris['data'], columns=iris['feature_names'])
print(iris_df)

iris_df['species'] = iris['target']

colours = ['red', 'orange', 'blue']
species = ['I. setosa', 'I. versicolor', 'I. virginica']

for i in range(0, 3):    
    species_df = iris_df[iris_df['species'] == i]    
    plt.scatter(        
        species_df['sepal width (cm)'],        
        species_df['petal width (cm)'],
        color=colours[i],        
        alpha=0.5,        
        label=species[i]   
    )

plt.xlabel('sepal witdh (cm)')
plt.ylabel('petal width (cm)')
plt.title('Iris dataset: petal width vs sepal width')
plt.legend(loc='lower right')

plt.show()