import csv
import matplotlib.pyplot as plt
import numpy as np


# the numpy method
import csv
with open("Iris.csv", 'r') as f:
    data = list(csv.reader(f, delimiter=","))

IrisData = np.array(data[:])

print(IrisData)

#plot the iris data