import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

col = ['sepal_length','sepal_width','petal_length','petal_width','type']
iris = pd.read_csv('Iris.csv',names=col)


iris_setosa=iris.loc[iris['type']=='Iris-setosa']
iris_virginica=iris.loc[iris['type']=='Iris-virginica']
iris_versicolor=iris.loc[iris['type']=='Iris-versicolor']

sns.FacetGrid(iris,hue='type',size=3).map(sns.distplot,'petal_length').add_legend()
sns.FacetGrid(iris,hue='type',size=3).map(sns.distplot,'petal_width').add_legend()
sns.FacetGrid(iris,hue='type',size=3).map(sns.distplot,'sepal_length').add_legend()
sns.FacetGrid(iris,hue='type',size=3).map(sns.distplot,'sepal_width').add_legend()
plt.show()