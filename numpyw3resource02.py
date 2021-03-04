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

#11. Write a NumPy program to convert a list and tuple into arrays.
listtoarray = [1, 2, 3, 4, 5, 6, 7, 8]
tupletoarray = (8, 4, 6, 1, 2, 3)
print(listtoarray) #print [1, 2, 3, 4, 5, 6, 7, 8]
print(tupletoarray) #print (8, 4, 6, 1, 2, 3)
print(np.array(listtoarray)) #print [1 2 3 4 5 6 7 8]
print(type(np.array(listtoarray))) #print <class 'numpy.ndarray'>
print(np.array(tupletoarray)) #print [8 4 6 1 2 3]
print(type(np.array(tupletoarray))) #print <class 'numpy.ndarray'>
tupletoarray2by3 = np.array(tupletoarray).reshape(2, 3)
print(tupletoarray2by3) #print [[8 4 6]\n [1 2 3]]
#official solution
print(np.asarray(listtoarray)) #print [1, 2, 3, 4, 5, 6, 7, 8]

#12. Write a NumPy program to append values to the end of an array. Expected Output: Original array: [10, 20, 30] After append values to the end of the array: [10 20 30 40 50 60 70 80 90]
originalarray = np.array([10, 20, 30])
print(originalarray) #print [10 20 30]
originalarray = np.append(originalarray, [40, 50])
print(originalarray) #print [10 20 30 40 50]
for n in range(60, 100, 10):
    originalarray = np.append(originalarray, n)
print(originalarray) #print [10 20 30 40 50 60 70 80 90]

#13. Write a NumPy program to create an empty and a full array.
'''
Expected Output:
[ 6.93270651e-310 1.59262180e-316 6.93270559e-310 6.93270665e-310]
[ 6.93270667e-310 6.93270671e-310 6.93270668e-310 6.93270483e-310]
[ 6.93270668e-310 6.93270671e-310 6.93270370e-310 6.93270488e-310]]
[[6 6 6]
[6 6 6]
[6 6 6]]
'''
emptyarray = np.empty((3, 3))
print(emptyarray)
'''
[[6.93556384e-310 1.40349188e-316 4.41322039e-143]
 [6.93555378e-310 6.93555150e-310 6.01377908e-180]
 [6.93555378e-310 6.93555150e-310 3.95252517e-322]]
'''
sixemptyarray = np.ones([3, 3], dtype="int8")
print(sixemptyarray)
'''
[[1 1 1]
 [1 1 1]
 [1 1 1]]
'''
multiplybysixemptyarray = sixemptyarray * 6
print(multiplybysixemptyarray)
'''
[[6 6 6]
 [6 6 6]
 [6 6 6]]
'''
number6 = np.full([3, 3], 6, dtype="int16")
print(number6)
'''
[[6 6 6]
 [6 6 6]
 [6 6 6]]
'''

#14. Write a NumPy program to convert the values of Centigrade degrees into Fahrenheit degrees. Centigrade values are stored into a NumPy array.  Sample Array [0, 12, 45.21 ,34, 99.91] Expected Output: Values in Fahrenheit degrees: [ 0. 12. 45.21 34. 99.91] Values in Centigrade degrees: [-17.77777778 -11.11111111 7.33888889 1.11111111 37.72777778]
samplearrayinfahrenheit = np.array([0, 12, 45.21, 34, 99.91])
print(samplearrayinfahrenheit) #print [ 0.   12.   45.21 34.   99.91]
converttocentigrade = ((samplearrayinfahrenheit - 32) * (5 / 9))
print(converttocentigrade) #print [-17.77777778 -11.11111111   7.33888889   1.11111111  37.72777778]

#15. Write a NumPy program to find the real and imaginary parts of an array of complex numbers.  Expected Output: Original array [ 1.00000000+0.j 0.70710678+0.70710678j] Real part of the array: [ 1. 0.70710678] Imaginary part of the array: [ 0. 0.70710678]
originalarray = np.array([1.00000000 + 0.j, 0.70710678 + 0.70710678j])
print(originalarray) #print [1.        +0.j         0.70710678+0.70710678j]
print(originalarray.real) #print [1.         0.70710678]
print(originalarray.imag) #print [0.         0.70710678]

#16. Write a NumPy program to find the number of elements of an array, length of one array element in bytes and total bytes consumed by the elements.
sizethreearray = np.array([1, 2, 3])
print(sizethreearray) #print [1 2 3]
print(sizethreearray.size) #print 3
#length of one array element in bytes
print(sizethreearray.itemsize) #print 8
#total bytes consumed
print(sizethreearray.nbytes) #print 24

#17. Write a NumPy program to test whether each element of a 1-D array is also present in a second array.  Expected Output: Array1: [ 0 10 20 40 60] Array2: [0, 40] Compare each element of array1 and array2 [ True False False True False].  RM:  Array2: [0, 40] is a list.  Confusing.
array1 = np.array([0, 10, 20, 40, 60])
array2 = np.array([0, 40])
comparearray1array2 = array1 = array2
print(comparearray1array2) #print [ 0 40]
comparearray1array2true = array1 == array2
print(comparearray1array2true) #print [ True  True]
comparearray1array2all = np.all(array1 == array2, axis=0)
print(comparearray1array2all) #print True
comparearray1array2any = np.any(array1 == array2, axis=0)
print(comparearray1array2any) #print True
comparearray2array1all = np.all(array2 == array1, axis=0)
print(comparearray2array1all) #print True
comparearray2array1any = np.any(array2 == array1, axis=0)
print(comparearray2array1any) #print True
#official solution
completecomparison = np.in1d(array1, array2)
print(completecomparison) #print [ True  True]
array1 = np.array([0, 10, 20, 40, 60])
list1 = [0, 40]
completecomparison = np.in1d(array1, list1)
print(completecomparison) #print [ True False False  True False]
completecomparison = np.isin(array1, list1) #isin can be used with a matrix of any shape
print(completecomparison) #print [ True False False  True False]
#user solution
x = np.array([0, 10, 20, 40, 60])
y = np.array([0, 40])
print(np.array([item in y for item in x])) #print [ True False False  True False]

#18. Write a NumPy program to find common values between two arrays.  Expected Output:  Array1: [ 0 10 20 40 60]  Array2: [10, 30, 40]  Common values between two arrays: [10 40]
array1 = np.array([0, 10, 20, 40, 60])
array2 = np.array([10, 30, 40])
print(np.intersect1d(array1, array2)) #print [10 40]

#19. Write a NumPy program to get the unique elements of an array.  Source:  https://numpy.org/doc/stable/reference/generated/numpy.unique.html
tensarray = np.array([10, 10, 20, 20, 30, 30])
twodarray = np.array([[1, 1], [2, 3]])
print(np.unique(tensarray)) #print [10 20 30]
print(np.unique(twodarray, axis=None)) #print [1 2 3]
print(np.unique(twodarray, axis=0)) #print [[1 1] [2 3]]
print(np.unique(twodarray, axis=1)) #print [[1 1] [2 3]]

#20. Write a NumPy program to find the set difference of two arrays. The set difference will return the sorted, unique values in array1 that are not in array2.  Expected Output: Array1: [ 0 10 20 40 60 80] Array2: [10, 30, 40, 50, 70, 90] Set difference between two arrays: [ 0 20 60 80].  RM:  what values in array1 not in array2.  Source:  https://numpy.org/doc/stable/reference/generated/numpy.setdiff1d.html
array1 = np.array([0, 10, 20, 40, 60, 80])
array2 = np.array([10, 30, 40, 50, 70, 90])
print(np.setdiff1d(array1, array2)) #print [ 0 20 60 80]

#21. Write a NumPy program to find the set exclusive-or of two arrays. Set exclusive-or will return the sorted, unique values that are in only one (not both) of the input arrays. Array1: [ 0 10 20 40 60 80] Array2: [10, 30, 40, 50, 70] Unique values that are in only one (not both) of the input arrays: [ 0 20 30 50 60 70 80].  RM:  Include unique values in both arrays.  Exclude values in both values.
array1 = np.array([0, 10, 20, 40, 60, 80])
array2 = np.array([10, 30, 40, 50, 70])
print(np.setxor1d(array1, array2)) #print [ 0 20 30 50 60 70 80]

#22. Write a NumPy program to find the union of two arrays. Union will return the unique, sorted array of values that are in either of the two input arrays. Array1: [ 0 10 20 40 60 80] Array2: [10, 30, 40, 50, 70] Unique sorted array of values that are in either of the two input arrays: [ 0 10 20 30 40 50 60 70 80]
array1 = np.array([0, 10, 20, 40, 60, 80])
array2 = np.array([10, 30, 40, 50, 70])
print(np.union1d(array1, array2)) #print [ 0 10 20 30 40 50 60 70 80]
print(np.in1d(array1, array2)) #print [False  True False  True False False]  Test whether each element of a 1-D array is also present in a second array.  0 False, 10, True, 20 False, 40, True, 60 False 80 False

#23. Write a NumPy program to test whether all elements in an array evaluate to True.
zerotonine = np.random.randint(0, 10, size=(1, 6))
print(zerotonine) #print [[9 0 0 7 3 4]]
print(zerotonine >= 1) #print [[ True False False  True  True  True]]
#official solution
print(np.all([[True, False], [True, False]])) #False
print(np.all([True, True])) #True
print(np.all([10, 20, 0, -50])) #False
print(np.all([10, 20, -50])) #True

#24. Write a NumPy program to test whether any array element along a given axis evaluates to True.
print(np.any([[False, False], [False, False]])) #False
print(np.any([True, True])) #True
print(np.any([10, 20, 0, -50])) #True
print(np.any([10, 20, -50])) #True
print(np.any([0, 0, 0])) #False
