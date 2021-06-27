from sklearn import datasets
import matplotlib.pyplot as plt

bins = 20
iris = datasets.load_iris()
X_iris = iris.data
fig, axs = plt.subplots(2, 2)
axs[0, 0].hist(X_iris[:, 0])
axs[0, 1].hist(X_iris[:, 1], color='orange')
axs[1, 0].hist(X_iris[:, 2], color='green')
axs[1, 1].hist(X_iris[:, 3], color='red')

i = 0
for ax in axs.flat:
    ax.set(xlabel=iris.feature_names[i], ylabel='Frequency')
    i += 1

fig.suptitle("Iris Histograms")

plt.show()