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

#4. Write a NumPy program to create a null vector of size 10 and update sixth value to 11.  [ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]  Update sixth value to 11 [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]
sizeten = np.zeros([1, 11])
print(sizeten) #print [[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
sizeten[0, 5] = 11
print(sizeten) #print [[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
#official solution
moresizeten = np.zeros(10)
print(moresizeten) #print [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
moresizeten[5] = 11
print(moresizeten) #print [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

#5. Write a NumPy program to create an array with values ranging from 12 to [38].
twelvearray = np.arange(12, 39)
print(twelvearray) #print [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38]

#6. Write a NumPy program to reverse an array (first element becomes last).
twelvearray = np.arange(12, 39)
print(twelvearray) #print [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38]
print(twelvearray[::-1]) #print [38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12]

#7. Write a NumPy program to convert an array to a float type.
sampleoutput = np.array([1, 2, 3, 4])
print(sampleoutput)
sampleoutputfloat = np.array([1, 2, 3, 4], dtype="float")
print(sampleoutputfloat)
#official solution
sampleoutputasfloat = np.asfarray(sampleoutput)
print(sampleoutputasfloat) #print [1. 2. 3. 4.]

#8. Write a NumPy program to create a 2d array with 1 on the border and 0 inside.
twodimensionones = np.ones([2, 5])
print(twodimensionones)
'''
[[1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]
'''
twodimensionones[:, 1:4] = 0
print(twodimensionones)
'''
[[1. 0. 0. 0. 1.]
 [1. 0. 0. 0. 1.]]
'''
#official solution
x = np.ones((5, 5))
x[1:-1, 1:-1] = 0

#9. Write a NumPy program to add a border (filled with 0's) around an existing array.  #RM:  keep the 3x3 array with ones.  Surround the 3x3 array with ones with the border of all zeroes.
onesthreebythree = np.ones([3, 3])
print(onesthreebythree)
'''
[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]
'''
#official solution
onesthreebythreeborderzeros = np.pad(onesthreebythree, pad_width=1, mode="constant", constant_values=0)
print(onesthreebythreeborderzeros)
'''
[[0. 0. 0. 0. 0.]
 [0. 1. 1. 1. 0.]
 [0. 1. 1. 1. 0.]
 [0. 1. 1. 1. 0.]
 [0. 0. 0. 0. 0.]]
'''

#10. Write a NumPy program to create a 8x8 matrix and fill it with a checkerboard pattern.
checkerboardzeros = np.zeros([8, 8], dtype="int8")
print(checkerboardzeros)
'''
[[0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]]
'''
checkerboardzeros[::, ::2] = 1
print(checkerboardzeros)  #RM:  incorrect
'''
[[1 0 1 0 1 0 1 0]
 [1 0 1 0 1 0 1 0]
 [1 0 1 0 1 0 1 0]
 [1 0 1 0 1 0 1 0]
 [1 0 1 0 1 0 1 0]
 [1 0 1 0 1 0 1 0]
 [1 0 1 0 1 0 1 0]
 [1 0 1 0 1 0 1 0]]
'''
rownumber, columnumber = checkerboardzeros.shape
counter = 0
for r in range(0, rownumber):
    for c in range(0, columnumber):
        if r % 2 == 0:
            if counter % 2 == 0:
                checkerboardzeros[r, c] = 0
            else:
                checkerboardzeros[r, c] = 1
        counter += 1
print(checkerboardzeros)
'''
[[0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]
 [0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]
 [0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]
 [0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]]
'''
#official solution
x = np.zeros((8, 8), dtype=int)
x[1::2, ::2] = 1
x[::2, 1::2] = 1
print(x)
