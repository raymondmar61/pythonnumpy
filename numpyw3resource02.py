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

#25. Write a NumPy program to construct an array by repeating.  Sample array: [1, 2, 3, 4] Expected Output: Original array [1, 2, 3, 4] Repeating 2 times [1 2 3 4 1 2 3 4] Repeating 3 times [1 2 3 4 1 2 3 4 1 2 3 4]
originalarray = np.array([1, 2, 3, 4])
print(originalarray) #print [1 2 3 4]
repeattwotimesnosequence = np.repeat(originalarray, 2)
print(repeattwotimesnosequence) #print [1 1 2 2 3 3 4 4]
repeattwotimesyessequence = np.tile(originalarray, 2)
print(repeattwotimesyessequence) #print [1 2 3 4 1 2 3 4]
repeatthreetimesyessequence = np.tile(originalarray, 3)
print(repeatthreetimesyessequence) #print [1 2 3 4 1 2 3 4 1 2 3 4]

#26. Write a NumPy program to repeat elements of an array. Expected Output: [3 3 3 3] [1 1 2 2 3 3 4 4]
fourthrees = np.repeat(3, 4, axis=0) #axis=0 is default no need to mention
print(fourthrees) #print [3 3 3 3]
originalarray = np.array([1, 2, 3, 4])
repeatoriginalarray = np.repeat(originalarray, 2, axis=0) #axis=0 is default no need to mention
print(repeatoriginalarray) #print [1 1 2 2 3 3 4 4]

#27. Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array. Original array: [1 2 3 4 5 6] Maximum Values: 5 Minimum Values: 0.  #RM:  find the minimum index value and the maximum index value.  Not minimum number and maximum number.
numbersarray = np.arange(1, 7)
print(numbersarray.min()) #print 1
print(numbersarray.max()) #print 6
print(numbersarray.argmin()) #print 0
print(numbersarray.argmax()) #print 5
indexgreatestnumber = np.array([1, 454, 2090, 0, 35])
print(indexgreatestnumber.argmin()) #print 3
print(indexgreatestnumber.argmax()) #print 2

#28. Write a NumPy program compare two given arrays. Array a: [1 2] Array b: [4 5] a > b [False False] a >= b [False False] a < b [ True True] a <= b [ True True]
arraya = np.array([1, 2])
arrayb = np.array([4, 5])
print(arraya > arrayb) #print [False False]
print(arraya >= arrayb) #print [False False]
print(arraya < arrayb) #print [ True True]
print(arraya <= arrayb) #print [ True True]
print(np.greater(arraya, arrayb)) #print [False False]
print(np.greater_equal(arraya, arrayb)) #print [False False]
print(np.less(arraya, arrayb)) #print [ True True]
print(np.less_equal(arraya, arrayb)) #print [ True True]
bonusarraya = np.array([10, 20, 345])
bonusarrayb = np.array([8, 35, 345])
print(np.greater(bonusarraya, bonusarrayb)) #print [ True False False]
print(np.greater_equal(bonusarraya, bonusarrayb)) #print [ True False True]
print(np.less(bonusarraya, bonusarrayb)) #print [False True False]
print(np.less_equal(bonusarraya, bonusarrayb)) #print [False  True  True]

#29. Write a NumPy program to sort an along the first, last axis of an array. Sample array: [[2,5],[4,4]] Expected Output: Original array: [[4 6] [2 1]] Sort along the first axis: [[2 1] [4 6]] Sort along the last axis: [[1 2] [4 6]  RM:  is first axis the zero axis axis 0?
'''
https://numpy.org/doc/stable/reference/generated/numpy.sort.html
np.sort(array, axis=integer which axis to sort or None to flat array default -1 sorts last axis, kind={‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’} optional, order=a string or a list of strings optional) returns a sorted copy of an array.
#also axis 0 is the rows going from up to down.  axis 1 is the columns going from left to right.
'''
originalarray = np.array([[4, 6], [2, 1]])
print(originalarray)
'''
[[4 6]
 [2 1]]
'''
sortfirstaxiswhichisaxis0 = np.sort(originalarray, axis=0)
print(sortfirstaxiswhichisaxis0)
'''
[[2 1]
 [4 6]]
'''
sortlastaxiswhichisaxis1 = np.sort(originalarray, axis=1)
print(sortlastaxiswhichisaxis1)
'''
[[4 6]
 [1 2]]
'''
sortflatoriginalarray = np.sort(originalarray, axis=None)
print(sortflatoriginalarray) #print [1 2 4 6]

#30. Write a NumPy program to sort pairs of first name and last name return their indices. (first by last name, then by first name). first_names = (Betsey, Shelley, Lanell, Genesis, Margery) last_names = (Battle, Brien, Plotner, Stahl, Woolum) Expected Output: [1 3 2 4 0]
firstname = np.array(["Betsey", "Shelley", "Lanell", "Genesis", "Margery"])
lastname = np.array(["Battle", "Brien", "Plotner", "Stahl", "Woolum"])
print(np.char.add(firstname, lastname)) #print ['BetseyBattle' 'ShelleyBrien' 'LanellPlotner' 'GenesisStahl' 'MargeryWoolum']
print(np.sort(np.char.add(firstname, lastname))) #print ['BetseyBattle' 'GenesisStahl' 'LanellPlotner' 'MargeryWoolum' 'ShelleyBrien']
print(np.lexsort((firstname, lastname))) #print [0 1 2 3 4]
print(np.lexsort(np.char.add(firstname, lastname))) #print 0
#official solution
firstname = ('Margery', 'Betsey', 'Shelley', 'Lanell', 'Genesis')
lastname = ('Woolum', 'Battle', 'Plotner', 'Brien', 'Stahl')
print(np.lexsort((firstname, lastname))) #print [1 3 2 4 0]

#31. Write a NumPy program to get the values and indices of the elements that are bigger than 10 in a given array. Original array: [[ 0 10 20] [20 30 40]] Values bigger than 10 = [20 20 30 40] Their indices are (array([0, 1, 1, 1]), array([2, 0, 1, 2]))
originalarray = np.array([[0, 10, 20], [20, 30, 40]])
print(originalarray)
'''
[[ 0 10 20]
 [20 30 40]]
'''
greaterthanten = originalarray[originalarray > 10]
print(greaterthanten) #print [20 20 30 40]
indexindicesgreaterthanten = np.nonzero(originalarray > 10)
print(indexindicesgreaterthanten) #print (array([0, 1, 1, 1]), array([2, 0, 1, 2]))
bonusoriginalarray = np.array([778, 0, 10, 20, 40, 30, 10, 500])
indexindicesgreaterthanten = np.nonzero(bonusoriginalarray > 10)
print(indexindicesgreaterthanten) #print (array([0, 3, 4, 5, 7]),)
print(indexindicesgreaterthanten[0]) #print [0 3 4 5 7]

#32. Write a NumPy program to save a NumPy array to a text file.
originalarray = np.arange(0, 21)
print(originalarray)
np.savetxt("arraytextfilename.txt", originalarray, delimiter=",") #delimiter is the string or character separating columns.

#33. Write a NumPy program to find the memory size of a NumPy array.
originalarray = np.arange(0, 11)
memoryinbyteseachelementtakes = originalarray.itemsize
print(memoryinbyteseachelementtakes) #print 8
totalitemsize = originalarray.size * originalarray.itemsize
print(totalitemsize) #print 88

import numpy as np

#34. Write a NumPy program to create an array of ones and an array of zeros. Expected Output: Create an array of zeros Default type is float [[ 0. 0.]] Type changes to int [[0 0]] Create an array of ones Default type is float [[ 1. 1.]] Type changes to int [[1 1]]
arrayzeros = np.zeros([1, 2])
print(arrayzeros) #print [[0. 0.]]
arrayzerosinteger = np.zeros([1, 2], dtype="uint8")
print(arrayzerosinteger) #print [[0 0]]
arrayones = np.ones([1, 2])
print(arrayones) #print [[1. 1.]]
arrayonesinteger = np.ones([1, 2], dtype="uint8")
print(arrayonesinteger) #print [[1 1]]

#35. Write a NumPy program to change the dimension of an array. Expected Output: 6 rows and 0 columns (6,) (3, 3) -> 3 rows and 3 columns [[1 2 3] [4 5 6] [7 8 9]] Change array shape to (3, 3) -> 3 rows and 3 columns [[1 2 3] [4 5 6] [7 8 9]]
sixrows = np.arange(1, 7)
print(sixrows) #print [1 2 3 4 5 6]
sixrowsactual = sixrows.reshape(6, 1)
print(sixrowsactual)
'''
[[1]
 [2]
 [3]
 [4]
 [5]
 [6]]
'''
threerowsthreecolumns = np.arange(1, 10)
print(threerowsthreecolumns) #print [1 2 3 4 5 6 7 8 9]
threerowsthreecolumnsactual = threerowsthreecolumns.reshape(3, 3)
print(threerowsthreecolumnsactual)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''

#36. Write a NumPy program to create a contiguous flattened array. Original array: [[10 20 30] [20 40 50]] New flattened array: [10 20 30 20 40 50]
originalarray = np.array([[10, 20, 30], [20, 40, 50]])
print(originalarray)
'''
[[10 20 30]
 [20 40 50]]
'''
flatoriginalarray = originalarray.ravel()
print(flatoriginalarray) #print [10 20 30 20 40 50]

#37. Write a NumPy program to create a 2-dimensional array of size 2 x 3 (composed of 4-byte integer elements), also print the shape, type and data type of the array. Expected Output: (2, 3) int32
sizetwobythree = np.array([[45, 67, 89], [13, 46, 79]], np.int32)
print(sizetwobythree)
print(sizetwobythree.shape) #print (2, 3)
print(sizetwobythree.dtype) #print int32

#38. Write a NumPy program to create a new shape to an array without changing its data. Reshape 3x2: [[1 2] [3 4] [5 6]] Reshape 2x3: [[1 2 3] [4 5 6]]
originalarray = np.arange(1, 7)
print(originalarray) #print [1 2 3 4 5 6]
print(originalarray.reshape(3, 2))
'''
[[1 2]
 [3 4]
 [5 6]]
'''
print(originalarray.reshape(2, 3))
'''
[[1 2 3]
 [4 5 6]]
'''

#39. Write a NumPy program to change the data type of an array. Expected Output: [[ 2 4 6] [ 6 8 10]] Data type of the array x is: int32 New Type: float64 [[ 2. 4. 6.] [ 6. 8. 10.]]
datatypearrayint64 = np.array([[2, 4, 6], [6, 8, 10]])
print(datatypearrayint64.dtype) #print int64
datatypearrayfloat64 = datatypearrayint64.astype("float64")
print(datatypearrayfloat64.dtype) #print float64

#40. Write a NumPy program to create a new array of 3*5, filled with 2. Expected Output: [[2 2 2 2 2] [2 2 2 2 2] [2 2 2 2 2]]
twosarray = np.ones([3, 5], dtype="int8") * 2
print(twosarray)
'''
[[2 2 2 2 2]
 [2 2 2 2 2]
 [2 2 2 2 2]]
'''

#41. Write a NumPy program to create an array of 10's with the same shape and type of a given array. Sample array: x = np.arange(4, dtype=np.int64) Expected Output: [10 10 10 10]
samplearray = np.arange(4, dtype=np.int64)
print(samplearray) #print [0 1 2 3]
samplearray.fill(10)
print(samplearray) #print [10 10 10 10]

#42. Write a NumPy program to create a 3-D array with ones on a diagonal and zeros elsewhere. Expected Output: [[ 1. 0. 0.] [ 0. 1. 0.] [ 0. 0. 1.]]
zerosarray = np.zeros([3, 3], dtype=np.int8)
print(zerosarray)
'''
[[0 0 0]
 [0 0 0]
 [0 0 0]]
'''
print(zerosarray.shape[1]) #print 3
for n in range(0, zerosarray.shape[1]):
    zerosarray[n, n] = 1
print(zerosarray)
'''
[[1 0 0]
 [0 1 0]
 [0 0 1]]
'''
#official solution
zerosarray = np.zeros([3, 3], dtype=np.int8)
zerosarrayeye = np.eye(3)
print(zerosarrayeye)
'''
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
'''
#RM:  np.identity(3) works, too.

#43. Write a NumPy program to create a 2-D array whose diagonal equals [4, 5, 6, 8] and 0's elsewhere. Expected Output: [[4 0 0 0] [0 5 0 0] [0 0 6 0] [0 0 0 8]]
zerosfourbyfour = np.zeros([4, 4], dtype=np.int8)
print(zerosfourbyfour)
'''
[[0 0 0 0]
 [0 0 0 0]
 [0 0 0 0]
 [0 0 0 0]]
'''
questionisaclue = np.array([4, 5, 6, 8], dtype=np.int8)
print(questionisaclue) #print [4 5 6 8]
print(zerosfourbyfour.shape[1]) #print 4
for n in range(0, zerosfourbyfour.shape[1]):
    zerosfourbyfour[n, n] = questionisaclue[n]
print(zerosfourbyfour)
'''
[[4 0 0 0]
 [0 5 0 0]
 [0 0 6 0]
 [0 0 0 8]]
'''
#official solution
x = np.diagflat([4, 5, 6, 8])
print(x)
'''
[[4 0 0 0]
 [0 5 0 0]
 [0 0 6 0]
 [0 0 0 8]]
'''

#44. Write a NumPy program to create a 1-D array going from 0 to 50 and an array from 10 to 50. Expected Output: Array from 0 to 50: [ 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49] Array from 10 to 50: [10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49]
array0to50 = np.arange(0, 51)  #RM:  faster and python way is np.arange(51)
print(array0to50) #print [ 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50]
array10to50 = np.arange(10, 51)
print(array10to50) #print [10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50]

#45. Write a NumPy program to Create a 1-D array of 30 evenly spaced elements between 2.5. and 6.5, inclusive. Expected Output: [ 2.5 2.63793103 2.77586207 2.9137931 3.05172414 3.18965517 ................. 5.81034483 5.94827586 6.0862069 6.22413793 6.36206897 6.5 ]
thirtyevenlyspacedvalues = np.linspace(2.5, 6.5, 30)
print(thirtyevenlyspacedvalues)
'''
[2.5        2.63793103 2.77586207 2.9137931  3.05172414 3.18965517
 3.32758621 3.46551724 3.60344828 3.74137931 3.87931034 4.01724138
 4.15517241 4.29310345 4.43103448 4.56896552 4.70689655 4.84482759
 4.98275862 5.12068966 5.25862069 5.39655172 5.53448276 5.67241379
 5.81034483 5.94827586 6.0862069  6.22413793 6.36206897 6.5       ]
'''

#46. Write a NumPy program to to create a 1-D array of 20 element spaced evenly on a log scale between 2. and 5., exclusive. Expected Output: [ 100. 141.25375446 199.5262315 281.83829313 ...................... 25118.8643151 35481.33892336 50118.72336273 70794.57843841]
twentyevenlyspacedvalues = np.linspace(2, 6, 20)
print(twentyevenlyspacedvalues)
logscale = np.log10(twentyevenlyspacedvalues)
print(logscale)
'''
[0.30103    0.34449569 0.38400423 0.4202164  0.45364016 0.48467439
 0.51363809 0.54079033 0.56634444 0.59047812 0.613341   0.63506025
 0.65574485 0.67548891 0.69437425 0.71247247 0.72984657 0.74655226
 0.76263908 0.77815125]
 '''
logspaceinclusive = np.logspace(2, 5, 20, endpoint=True)
print(logspaceinclusive)
'''
[ 100. 143.84498883 206.91380811 297.63514416 428.13323987 615.84821107 885.86679041 1274.2749857 1832.98071083 2636.65089873 3792.69019073 5455.59478117 7847.59970351 11288.37891685 16237.76739189 23357.2146909 33598.18286284 48329.30238572 69519.27961776 100000. ] 
'''
logspaceexclusivecorrectanswer = np.logspace(2, 5, 20, endpoint=False)
print(logspaceexclusivecorrectanswer)
'''
[  100.           141.25375446   199.5262315    281.83829313
   398.10717055   562.34132519   794.32823472  1122.0184543
  1584.89319246  2238.72113857  3162.27766017  4466.83592151
  6309.5734448   8912.50938134 12589.25411794 17782.79410039
 25118.8643151  35481.33892336 50118.72336273 70794.57843841]
'''

#47. Write a NumPy program to create an array which looks like below array. Expected Output: [[ 0. 0. 0.] ........... [ 1. 1. 1.]].  RM:  create a triangle of zeros and ones.  Reference https://numpy.org/doc/stable/reference/generated/numpy.tri.html
zerostoprightonesbottomleft = np.tri(4, 3, -1)
print(zerostoprightonesbottomleft)
'''
[[0. 0. 0.]
 [1. 0. 0.]
 [1. 1. 0.]
 [1. 1. 1.]]
'''
defaultzero = np.tri(4, 3, 0)
print(defaultzero)
'''
[[1. 0. 0.]
 [1. 1. 0.]
 [1. 1. 1.]
 [1. 1. 1.]]
'''

#48. Write a NumPy program to create an array which looks like below array. Expected Output: [[ 2 3 4] [ 5 6 7] [ 0 9 10] [ 0 0 13]] Reference https://numpy.org/doc/stable/reference/generated/numpy.triu.html
x = np.triu(np.arange(2, 14))
print(x)
'''
[[ 2  3  4  5  6  7  8  9 10 11 12 13]
 [ 0  3  4  5  6  7  8  9 10 11 12 13]
 [ 0  0  4  5  6  7  8  9 10 11 12 13]
 [ 0  0  0  5  6  7  8  9 10 11 12 13]
 [ 0  0  0  0  6  7  8  9 10 11 12 13]
 [ 0  0  0  0  0  7  8  9 10 11 12 13]
 [ 0  0  0  0  0  0  8  9 10 11 12 13]
 [ 0  0  0  0  0  0  0  9 10 11 12 13]
 [ 0  0  0  0  0  0  0  0 10 11 12 13]
 [ 0  0  0  0  0  0  0  0  0 11 12 13]
 [ 0  0  0  0  0  0  0  0  0  0 12 13]
 [ 0  0  0  0  0  0  0  0  0  0  0 13]]
'''
x = np.triu(np.arange(2, 14).reshape(4, 3), -1)
print(x)
'''
[[ 2  3  4]
 [ 5  6  7]
 [ 0  9 10]
 [ 0  0 13]]
'''
