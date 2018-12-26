# %matplotlib inline
import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt
# import panda as pd

x = np.array([[1, 2, 3], [4, 5, 6]])
print("x:\n{}".format(x))

eye = np.eye(4)
print("array Numpy:\n{}".format(eye))

sparse_matrix = sparse.csr_matrix(eye)
print("Rarefied matrix SciPy in CSR format:\n{}".format(sparse_matrix))

data = np.ones(4)
row_indices = np.arange(4)
col_indices = np.arange(4)
eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))
print("Format COO:\n{}".format(eye_coo))

# Generate a sequence of numbers from -10 to 10 with 100 steps in between
x = np.linspace(-10, 10, 100)
# Create a second array using sine
y = np.sin(x)
# The plot function makes a line chart of one array against another
plt.plot(x, y, marker="x")
plt.show()

data = {'Name': ["John", "Anna", "Peter", "Linda"],
'Location' : ["New York", "Paris", "Berlin", "London"],
'Age' : [24, 13, 53, 33]
}
# data_pandas = pd.DataFrame(data)
# display(data_pandas)