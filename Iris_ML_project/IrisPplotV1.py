
import numpy as np
data_ = np.random.randn(1000)
plt.hist(data_,bins = 40,color='gold')
plt.grid(True)
plt.xlabel('points')
plt.title("Histogram")
plt.show()