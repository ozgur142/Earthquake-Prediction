import numpy as np

a = np.array([[1, 2, 3]])
b = np.array([[4, 5, 6], [7, 8, 9]])

X = np.concatenate((b, a), axis=0)

print(a.shape)


print(X)


