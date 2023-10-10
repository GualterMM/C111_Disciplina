import numpy as np

# NumPy Array
arr = np.array([1, 2, 3])
print(arr)
print(type(arr))

# NumPy Array 2D
mtz = np.array([[1, 2, 3], [4, 5, 6]])
print(mtz)

# zeros, ones, arange e reshape
mtz_um = np.ones(9).reshape(3,3)
print(mtz_um)

mtz_ar = np.arange(10, 20, 2)
print(mtz_ar)

# Concatenação de Arrays
arr = np.arange(1, 10, 1)
arr2 = np.arange(11, 20, 1)
arr3 = (arr + arr2) # faz a soma dos dois vetores
arr3 = np.concatenate((arr, arr2))
print(arr3)

# Verificando a estrutura de um numpy array
print("Dimensoes:", mtz.ndim)
print("Formato:", mtz.shape)
print("Num elementos:", mtz.size)