#https://www.w3resource.com/python-exercises/
#https://www.w3resource.com/python-exercises/numpy/index.php
#https://www.w3resource.com/python-exercises/numpy/index-array.php

import numpy as np

#https://www.w3resource.com/python-exercises/numpy/index-array.php
#1. Write a NumPy program to print the NumPy version in your system.
print(np.version.version) #print 1.18.1

#2. Write a NumPy program to convert a list of numeric value into a one-dimensional NumPy array.
originallist = [12.23, 13.32, 100, 36.32]
onedimensionalnumpyarray = np.array(originallist, dtype=np.float)
print(onedimensionalnumpyarray) #print [ 12.23  13.32 100.    36.32]
print(type(onedimensionalnumpyarray)) #print <class 'numpy.ndarray'>

#3.Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
print(np.array([[2, 3, 4], [5, 6, 7], [8, 9, 10]])) #print [[ 2  3  4]\n  [ 5  6  7]\n  [ 8  9 10]]
threebythree = np.arange(2, 11)
displaythreebythree = threebythree.reshape(3, 3)
print(displaythreebythree) #print [[ 2  3  4]\n  [ 5  6  7]\n  [ 8  9 10]]
