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
#49. Write a NumPy program to collapse a 3-D array into one dimension array. Expected Output: 3-D array: [[ 1. 0. 0.] [ 0. 1. 0.] [ 0. 0. 1.]] One dimension array: [ 1. 0. 0. 0. 1. 0. 0. 0. 1.]
array3d = np.diagflat([1., 1., 1.], k=0)
print(array3d)
'''
[[1 0 0]
 [0 1 0]
 [0 0 1]]
'''
print(array3d.shape) #print (3, 3)
print("Number of dimensions", array3d.ndim) #print Number of dimensions 2
print(array3d.flatten()) #print [1. 0. 0. 0. 1. 0. 0. 0. 1.]
#official solution
diagonalonefloats = np.eye(3)
print(diagonalonefloats)
'''
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
'''
print("Number of dimensions", diagonalonefloats.ndim) #print Number of dimensions 2
print(np.ravel(diagonalonefloats, order="F")) #print [1. 0. 0. 0. 1. 0. 0. 0. 1.]

#50. Write a NumPy program to find the 4th element of a specified array. Expected Output: [[ 2 4 6] [ 6 8 10]] Forth e1ement of the array: 6
findfourthelement = np.array([[2, 4, 6], [6, 8, 10]])
print(findfourthelement)
'''
[[ 2  4  6]
 [ 6  8 10]]
'''
print(findfourthelement[1, 0]) #print 6
#official solution
flatfindfourthelement = findfourthelement.flat[3]
print(flatfindfourthelement) #print 6
flatfindfourthelement = findfourthelement.flat
print(flatfindfourthelement) #print <numpy.flatiter object at 0x279ce40>
flatfindfourthelement = findfourthelement.flat[0:]
print(flatfindfourthelement) #print [ 2  4  6  6  8 10]
print(type(flatfindfourthelement)) #print <class 'numpy.ndarray'>

#51. Write a NumPy program to interchange two axes of an array. Sample array: [[1 2 3]] Expected Output: [[1] [2] [3]]
samplearray = np.array([1, 2, 3])
print(samplearray) #print [1 2 3]
expectedoutputarray = samplearray.reshape(3, 1)
print(expectedoutputarray)
'''
[[1]
 [2]
 [3]]
'''
#official solution
twobracketssamplearray = np.array([[1, 2, 3]])
print(twobracketssamplearray) #print [[1 2 3]]
print(twobracketssamplearray.shape) #print (1,3)
print("Number of dimensions", twobracketssamplearray.ndim) #print Number of dimensions 2
print(np.swapaxes(twobracketssamplearray, 0, 1))
'''
[[1]
 [2]
 [3]]
'''

#52. Write a NumPy program to move axes of an array to new positions. Other axes remain in their original order. Expected Output: (3, 4, 2) (4, 2, 3).  RM:  I don't understand the question.  Looked at answer.  Create a two 3 rows and 4 columns of zeros numpy.  Then reshape to three 4 rows and 2 columns and reshape to four 2 rows and 3 columns.  I sitll don't understand.
x = np.zeros([2, 3, 4], dtype="int8")
print(x)
'''
[[[0 0 0 0]
  [0 0 0 0]
  [0 0 0 0]]

 [[0 0 0 0]
  [0 0 0 0]
  [0 0 0 0]]]
'''
print(np.moveaxis(x, 0, -1))
'''
[[[0. 0.]
  [0. 0.]
  [0. 0.]
  [0. 0.]]

 [[0. 0.]
  [0. 0.]
  [0. 0.]
  [0. 0.]]

 [[0. 0.]
  [0. 0.]
  [0. 0.]
  [0. 0.]]]
'''
print(np.moveaxis(x, 0, -1).shape) #print (3, 4, 2)
print(np.moveaxis(x, -1, 0))
'''
[[[0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]]]
'''
print(np.moveaxis(x, -1, 0).shape) #print (4, 2, 3)

#53. Write a NumPy program to move the specified axis backwards, until it lies in a given position. Move the following 3rd array axes to first position. (2,3,4,5) Sample Expected Output: (2, 5, 3, 4)
initialarray = np.ones([2, 3, 4, 5])
print(initialarray)
'''
[[[[1. 1. 1. 1. 1.]
   [1. 1. 1. 1. 1.]
   [1. 1. 1. 1. 1.]
   [1. 1. 1. 1. 1.]]

  [[1. 1. 1. 1. 1.]
   [1. 1. 1. 1. 1.]
   [1. 1. 1. 1. 1.]
   [1. 1. 1. 1. 1.]]

  [[1. 1. 1. 1. 1.]
   [1. 1. 1. 1. 1.]
   [1. 1. 1. 1. 1.]
   [1. 1. 1. 1. 1.]]]


 [[[1. 1. 1. 1. 1.]
   [1. 1. 1. 1. 1.]
   [1. 1. 1. 1. 1.]
   [1. 1. 1. 1. 1.]]

  [[1. 1. 1. 1. 1.]
   [1. 1. 1. 1. 1.]
   [1. 1. 1. 1. 1.]
   [1. 1. 1. 1. 1.]]

  [[1. 1. 1. 1. 1.]
   [1. 1. 1. 1. 1.]
   [1. 1. 1. 1. 1.]
   [1. 1. 1. 1. 1.]]]]
'''
print(np.rollaxis(initialarray, 3, 1))
'''
[[[[1. 1. 1. 1.]
   [1. 1. 1. 1.]
   [1. 1. 1. 1.]]

  [[1. 1. 1. 1.]
   [1. 1. 1. 1.]
   [1. 1. 1. 1.]]

  [[1. 1. 1. 1.]
   [1. 1. 1. 1.]
   [1. 1. 1. 1.]]

  [[1. 1. 1. 1.]
   [1. 1. 1. 1.]
   [1. 1. 1. 1.]]

  [[1. 1. 1. 1.]
   [1. 1. 1. 1.]
   [1. 1. 1. 1.]]]


 [[[1. 1. 1. 1.]
   [1. 1. 1. 1.]
   [1. 1. 1. 1.]]

  [[1. 1. 1. 1.]
   [1. 1. 1. 1.]
   [1. 1. 1. 1.]]

  [[1. 1. 1. 1.]
   [1. 1. 1. 1.]
   [1. 1. 1. 1.]]

  [[1. 1. 1. 1.]
   [1. 1. 1. 1.]
   [1. 1. 1. 1.]]

  [[1. 1. 1. 1.]
   [1. 1. 1. 1.]
   [1. 1. 1. 1.]]]]
'''

import numpy as np

#54. Write a NumPy program to convert specified inputs to arrays with at least one dimension.
x = 12.0
print(np.atleast_1d(x)) #print 12.
x2 = np.arange(6).reshape(2, 3)
print(x2)
'''
[[0 1 2]
 [3 4 5]]
'''
print(np.atleast_1d(x2))
'''
[[0 1 2]
 [3 4 5]]
'''
print(np.atleast_1d(1)) #print [1]
print(np.atleast_1d([3, 4])) #print [3 4]
print(np.atleast_1d(1, [3, 4])) #print [array([1]), array([3, 4])]

#55. Write a NumPy program to view inputs as arrays with at least two dimensions, three dimensions.
print(np.atleast_1d(10)) #print [10]
print(np.atleast_2d(10)) #print [[10]]
tenx = 10
print(np.atleast_2d(tenx)) #print [[10]]
threesx = np.arange(4).reshape(2, 2)
print(threesx)
'''
[[0 1]
 [2 3]]
'''
print(np.atleast_1d(threesx))
'''
[[0 1]
 [2 3]]
'''
print(np.atleast_2d(threesx))
'''
[[0 1]
 [2 3]]
'''
print(np.atleast_3d(tenx)) #print [[[10]]]
threedimensionx = np.arange(3)
print(np.atleast_3d(threedimensionx))
'''
[[[0]
  [1]
  [2]]]
'''

#56. Write a NumPy program to insert a new axis within a 2-D array.
#official solution
x = np.zeros([3, 4])
print(x)
'''
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
'''
y = np.expand_dims(x, axis=1)
print(y)
'''
[[[0. 0. 0. 0.]]

 [[0. 0. 0. 0.]]

 [[0. 0. 0. 0.]]]
'''
print(y.shape) #print (3, 1, 4)

#57. Write a NumPy program to remove single-dimensional entries from a specified shape.
#official solution
zeros314 = np.zeros([3, 1, 4])
print(zeros314)
'''
[[[0. 0. 0. 0.]]

 [[0. 0. 0. 0.]]

 [[0. 0. 0. 0.]]]
'''
zeros34 = np.squeeze(zeros314)
print(zeros34)
'''
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
'''
#58. Write a NumPy program to concatenate two 2-dimensional arrays.  Expected Output:[[ 0 1 3 0 2 4] [ 5 7 9 6 8 10]]
samplearray = np.array([[[0, 1, 3], [5, 7, 9]], [[0, 2, 4], [6, 8, 10]]])
print(samplearray)
'''
[[[ 0  1  3]
  [ 5  7  9]]

 [[ 0  2  4]
  [ 6  8 10]]]
'''
print(samplearray.ndim) #print 3
print(samplearray.shape) #print (2, 2, 3) two arrays per dimension or groups of arrays(?), two rows per array, three columns per array
print(samplearray.flatten()) #print [ 0  1  3  5  7  9  0  2  4  6  8 10]
print(samplearray.reshape(2, 6)) #print [ 0  1  3  5  7  9  0  2  4  6  8 10]
#official solution
arraya = np.array([[0, 1, 3], [5, 7, 9]])
arrayb = np.array([[0, 2, 4], [6, 8, 10]])
concatenateab = np.concatenate((arraya, arrayb), axis=1)
print(concatenateab)
'''
[[ 0  1  3  0  2  4]
 [ 5  7  9  6  8 10]]
'''

#59. Write a NumPy program to convert 1-D arrays as columns into a 2-D array.  Sample array: (10,20,30), (40,50,60) Expected Output: [[10 40] [20 50] [30 60]]
array10 = np.array([10, 20, 30])
array40 = np.array([40, 50, 60])
print(array10) #print [10 20 30]
print(array40) #print [40 50 60]
print(np.column_stack((array10, array40)))
'''
[[10 40]
 [20 50]
 [30 60]]
'''
print(np.concatenate((array10, array40), axis=0)) #print [10 20 30 40 50 60]

#60. Write a NumPy program to convert (in sequence depth wise (along third axis)) two 1-D arrays into a 2-D array. Sample array: (10,20,30), (40,50,60)
#official solution
a = np.array([[10], [20], [30]])
b = np.array([[40], [50], [60]])
c = np.dstack((a, b))
print(c)
'''
[[[10 40]]

 [[20 50]]

 [[30 60]]]
'''

#61. Write a NumPy program to split an array of 14 elements into 3 arrays, each of which has 2, 4, and 8 elements in the original order. Expected Output: Original array: [ 1 2 3 4 5 6 7 8 9 10 11 12 13 14] After splitting: [array([1, 2]), array([3, 4, 5, 6]), array([ 7, 8, 9, 10, 11, 12, 13, 14])]
originalarray = np.arange(1, 15)
print(originalarray) #print [ 1 2 3 4 5 6 7 8 9 10 11 12 13 14]
split248 = np.split(originalarray, [2, 6])
print(split248) #print [array([1, 2]), array([3, 4, 5, 6]), array([ 7,  8,  9, 10, 11, 12, 13, 14])]

#62. Write a NumPy program to split of an array of shape 4x4 it into two arrays along the second axis.  Sample array: [[ 0 1 2 3] ........ [12 13 14 15]] Expected Output: [array([[ 0, 1], [ 4, 5], [ 8, 9], [12, 13]]), array([[ 2, 3], [ 6, 7], [10, 11], [14, 15]]), array([], shape=(4, 0), dtype=int64)]
samplearray = np.arange(16).reshape(4, 4)
print(samplearray)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
'''
split2 = np.hsplit(samplearray, [2])
print(split2)
'''
[array([[ 0,  1],
       [ 4,  5],
       [ 8,  9],
       [12, 13]]), array([[ 2,  3],
       [ 6,  7],
       [10, 11],
       [14, 15]])]
'''
split26 = np.hsplit(samplearray, [2, 6])
print(split26)
'''
[array([[ 0,  1],
       [ 4,  5],
       [ 8,  9],
       [12, 13]]), array([[ 2,  3],
       [ 6,  7],
       [10, 11],
       [14, 15]]), array([], shape=(4, 0), dtype=int64)]
'''

#63. Write a NumPy program to get the number of nonzero elements in an array. Original array: [[ 0 10 20] [20 30 40]] Number of non zero elements in the above array: 5
nonzeroarrayelements = np.array([0, 10, 20, 20, 30, 40]).reshape(2, 3)
print(nonzeroarrayelements)
'''
[[ 0 10 20]
 [20 30 40]]
'''
counter = 1
for eachnonzero in nonzeroarrayelements:
    print("row", counter, eachnonzero)
    '''
    row 1 [ 0 10 20]
    row 2 [20 30 40]
    '''
    counter += 1
countnonzero = 0
for x in nonzeroarrayelements:
    for y in x:
        print(y) #print 0\n 10\n 20\n 20\n 30\n 40
        if y != 0:
            countnonzero += 1
print(countnonzero) #print 5
countnonzero = 0
for x in np.nditer(nonzeroarrayelements, order="C"):
    print(x)  #print 0\n 10\n 20\n 20\n 30\n 40
    if x != 0:
        countnonzero += 1
print(countnonzero) #print 5
print("Quickest way np function", np.count_nonzero(nonzeroarrayelements)) #print Quickest way np function 5

#64. Write a NumPy program to create a 5x5 matrix with row values ranging from 0 to 4.  Original array: [[ 0. 0. 0. 0. 0.] ......... [ 0. 0. 0. 0. 0.]] Row values ranging from 0 to 4. [[ 0. 1. 2. 3. 4.] .......... [ 0. 1. 2. 3. 4.]]
rowvalueszerotofour = np.arange(5)
print(rowvalueszerotofour) #print [0 1 2 3 4]
duplicaterowvalueszerotofour = np.repeat(rowvalueszerotofour, 5, axis=0)
print(duplicaterowvalueszerotofour) #print [0 0 0 0 0 1 1 1 1 1 2 2 2 2 2 3 3 3 3 3 4 4 4 4 4]
originalzeros = np.zeros([5, 5])
print(originalzeros)
'''
[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]
'''
blankarray = np.array([])
print(blankarray) #print []
for x in originalzeros:
    x = x + rowvalueszerotofour
    blankarray = np.append(blankarray, x)
print(blankarray) #print [0. 1. 2. 3. 4. 0. 1. 2. 3. 4. 0. 1. 2. 3. 4. 0. 1. 2. 3. 4. 0. 1. 2. 3. 4.]
print(blankarray.reshape(5, 5))
'''
[[0. 1. 2. 3. 4.]
 [0. 1. 2. 3. 4.]
 [0. 1. 2. 3. 4.]
 [0. 1. 2. 3. 4.]
 [0. 1. 2. 3. 4.]]
'''
#official solution  RM:  no need a for loop
officialsolution = originalzeros + rowvalueszerotofour
print(officialsolution)
'''
[[0. 1. 2. 3. 4.]
 [0. 1. 2. 3. 4.]
 [0. 1. 2. 3. 4.]
 [0. 1. 2. 3. 4.]
 [0. 1. 2. 3. 4.]]
'''

#65. Write a NumPy program to test whether specified values are present in an array.  #RM:  stupid question
originalarray = np.array([[1.12, 2., 3.45], [2.33, 5.12, 6.]])
print(originalarray)
'''
[[1.12 2.   3.45]
 [2.33 5.12 6.  ]]
'''
flatoriginalarray = originalarray.flatten()
print(flatoriginalarray) #print [1.12 2.   3.45 2.33 5.12 6.  ]
#official solution
print(2 in originalarray) #print True
print(0 in originalarray) #print False
print(6 in originalarray) #print True
print(2.3 in originalarray) #print False
print(5.12 in originalarray) #print True

#66. Write a NumPy program to create a vector of size 10 with values ranging from 0 to 1, both excluded.
vectortenbetweenzeroandone = np.random.random([1, 10])
print(vectortenbetweenzeroandone) #print [[0.97410434 0.48697155 0.48658977 0.4015471  0.42917672 0.46705215 0.32546243 0.55157408 0.02361853 0.69659801]]
#official solution.  RM:  solution wanted linespace starting from zero to one and between 0 and 1 use index to exclude 0 and 1
vectorascendingbetweenzeroandonesize10 = np.linspace(0, 1, 10, endpoint=False)
print(vectorascendingbetweenzeroandonesize10) #print [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]
vectorascendingbetweenzeroandonesize10 = np.linspace(0, 1, 10, endpoint=True)
print(vectorascendingbetweenzeroandonesize10) #print [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]
vectorascendingbetweenzeroandonesize12index = np.linspace(0, 1, 12, endpoint=True)[1:-1]
print(vectorascendingbetweenzeroandonesize12index) #print [0.09090909 0.18181818 0.27272727 0.36363636 0.45454545 0.54545455 0.63636364 0.72727273 0.81818182 0.90909091]

#67. Write a NumPy program to make an array immutable (read-only).
#official solution
# x = np.zeros(10)
# x.flags.writeable = False
# x[0] = 1
'''
Traceback (most recent call last):
  File "yywork.py", line 141, in <module>
    x[0] = 1
ValueError: assignment destination is read-only
'''

#68. Write a NumPy program (using NumPy) to sum of all the multiples of 3 or 5 below 100.
numpyarraytohundred = np.arange(100)
print(numpyarraytohundred)
'''
[  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17
  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35
  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53
  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71
  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89
  90  91  92  93  94  95  96  97  98  99]
'''
sumanswer = 0
for eachnumpyarraytohundred in numpyarraytohundred:
    if eachnumpyarraytohundred % 3 == 0 or eachnumpyarraytohundred % 5 == 0:
        sumanswer += eachnumpyarraytohundred
print(sumanswer) #print 2318

#69. Write a NumPy program to create an array with 10^3 elements.
array1000 = np.arange(1000, dtype=np.float)
#or
#array1000 = np.arange(1000, dtype="float")
print(array1000)
array1e3 = np.arange(1e3)
print(array1e3)

#70. Write a NumPy program to create display every element of a NumPy array.
array11 = np.arange(12)
for eacharray11 in array11:
    print(eacharray11) #print 0\n 1\n 2\n 3\n 4\n 5\n 6\n 7\n 8\n 9\n 10\n 11

#71. Write a NumPy program to create and display every element of a NumPy array in Fortran order.
array11 = np.arange(12).reshape(3, 4)
print(np.nditer(array11, order="F")) #<numpy.nditer object at 0x7f2e96bd6a30>
for eacharray11 in np.nditer(array11, order="F"):
    print(eacharray11, end=",") #print 0,4,8,1,5,9,2,6,10,3,7,11,

#72. Write a NumPy program to create a 5x5x5 cube of 1's.
cubeofones = np.ones([5, 5, 5], dtype="uint8")
print(cubeofones)

#73. Write a NumPy program to create an array of (3, 4) shape, multiply every element value by 3 and display the new array.  Original array elements: [[ 0 1 2 3] [ 4 5 6 7] [ 8 9 10 11]] New array elements: [[ 0 3 6 9] [12 15 18 21] [24 27 30 33]]
originalarray = np.arange(0, 12)
print(originalarray) #print [ 0  1  2  3  4  5  6  7  8  9 10 11]
print(originalarray.reshape(3, 4))
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''
reshapemultiple3 = originalarray.reshape(3, 4) * 3
print(reshapemultiple3)
'''
[[ 0  3  6  9]
 [12 15 18 21]
 [24 27 30 33]]
'''

#74. Write a NumPy program to combine a one and a two dimensional array together and display their elements.  One dimensional array: [0 1 2 3] Two dimensional array: [[0 1 2 3] [4 5 6 7]]
onedimension = np.array([0, 1, 2, 3])
twodimension = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
#https://www.geeksforgeeks.org/combining-a-one-and-a-two-dimensional-numpy-array/
#Combine 1 dimension and 2 dimension arrays and display their elements use numpy.nditer()
for oned, twod in np.nditer([onedimension, twodimension]):
    print(oned, ":", twod)
    '''
    0 : 0
    1 : 1
    2 : 2
    3 : 3
    0 : 4
    1 : 5
    2 : 6
    3 : 7
    '''

#75. Write a NumPy program to create an array of zeros and three column types (integer, float, character).  Expected Output: [(1, 2., b'Albert Einstein') (2, 2., b'Edmond Halley') (3, 3., b'Gertrude B. Elion')]
experiment = np.array([1, 2., "Albert Einstein"])
print(experiment) #print ['1' '2.0' 'Albert Einstein']
threecolumnzeroes = np.zeros([3, 3])
print(threecolumnzeroes)
'''
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
'''
x = np.array([('Rex', 9, 81.0), ('Fido', 3, 27.0)], dtype=[('name', 'U10'), ('age', 'i4'), ('weight', 'f4')])
print(x) #print [('Rex', 9, 81.) ('Fido', 3, 27.)]
integerfloat = np.array([[1, 2.0], [2, 2.0], [3, 3.0]], dtype=[("wholenumber", "i4"), ("decimalnumber", "f4")])
print(integerfloat)
'''
[[(1, 1.) (2, 2.)]
 [(2, 2.) (2, 2.)]
 [(3, 3.) (3, 3.)]]
'''
# integerfloatcharacter = np.array([[1, 2.0, "Albert Einstein"], [2, 2.0, "Edmont Halley"], [3, 3.0, "Gertrude B. Elion"]], dtype=[("wholenumber", "i4"), ("decimalnumber", "f4"), ("namestring", "U9")])
# print(integerfloatcharacter) #print ValueError: invalid literal for int() with base 10: 'Albert Einstein'
#official solution
x = np.zeros((3,), dtype=("i4,f4,a40"))
new_data = [(1, 2., "Albert Einstein"), (2, 2., "Edmond Halley"), (3, 3., "Gertrude B. Elion")]
x[:] = new_data
print(x) #print [(1, 2., b'Albert Einstein') (2, 2., b'Edmond Halley') (3, 3., b'Gertrude B. Elion')]

#76. Write a NumPy program to create a function cube which cubes all the elements of an array.  Exponent
cubearray = np.arange(1, 4) ** 3
print(cubearray)

#77. Write a NumPy program to create an array of (3, 4) shape and convert the array elements in smaller chunks.
originalarray = np.arange(0, 12).reshape(3, 4)
print(originalarray)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''
originalarrayshape = originalarray.shape
print(originalarrayshape) #print (3, 4)
for column in range(0, originalarrayshape[1]):
        #commas switches from row to column.  colon specifies the range of numbers.(?)
    print(originalarray[:, column])
    '''
    [0 4 8]
    [1 5 9]
    [ 2  6 10]
    [ 3  7 11]
    '''
# official solution
# for a in np.nditer(originalarray, flags=['external_loop'], order='F'):
#     print(a)

#78. Write a NumPy program to create a record array from a (flat) list of arrays.  Sample arrays: [1,2,3,4], ['Red', 'Green', 'White', 'Orange'], [12.20,15,20,40] Expected Output: (1, 'Red', 12.2) (2, 'Green', 15.0) (3, 'White', 20.0)
#official solution
a1 = np.array([1, 2, 3, 4])
a2 = np.array(["Red", "Green", "White", "Orange"])
a3 = np.array([12.20, 15, 20, 40])
result = np.core.records.fromarrays([a1, a2, a3], names="a,b,c")
print(result[0]) #print (1, 'Red', 12.2)
print(result[1]) #print (2, 'Green', 15.)
print(result[2]) #print (3, 'White', 20.)

#79. Write a NumPy program to generate a generic 2D Gaussian-like array.
gaussianarray = np.random.normal(loc=0.0, scale=1.0, size=None)
print(gaussianarray) #print -0.3658662019704474
#official solution
# x, y = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))
# d = np.sqrt(x * x + y * y)
# sigma, mu = 1.0, 0.0
# g = np.exp(-((d - mu)**2 / (2.0 * sigma**2)))
# print("2D Gaussian-like array:")
# print(g)

#80. Write a NumPy program to convert a NumPy array into Python list structure.
originalarrayelements = np.array([[0, 1], [2, 3], [4, 5]])
print(originalarrayelements)
'''
[[0 1]
 [2 3]
 [4 5]]
'''
longwaylist = []
for eachoriginalarrayelements in originalarrayelements:
    longwaylist.append(eachoriginalarrayelements)
print(longwaylist) #print [array([0, 1]), array([2, 3]), array([4, 5])]
print(list(originalarrayelements)) #print [array([0, 1]), array([2, 3]), array([4, 5])]
originalarrayelementstolist = originalarrayelements.tolist()
print(originalarrayelementstolist) #print [[0, 1], [2, 3], [4, 5]]

#81. Write a NumPy program to access an array by column.  RM:  official solution has correct question.
x = np.arange(9).reshape(3, 3)
print(x) #print [[0 1 2] [3 4 5] [6 7 8]]
print(x[:, 0]) #print [0 3 6]
print(x[:, 1]) #print [1 4 7]
print(x[:, 2]) #print [2 5 8]

#82. Write a NumPy program to convert a NumPy array of float values to a NumPy array of integer values.
originalfloatvalues = np.array([[12., 12.51], [2.34, 7.98], [25.23, 36.5]])
converttointeger = originalfloatvalues.astype(int)
print(converttointeger)
'''
[[12 12]
 [ 2  7]
 [25 36]]
'''

#83. Write a NumPy program to display NumPy array elements of floating values with given precision.
originalfloatvalues = np.array([0.26153123, 0.52760141, 0.5718299, 0.5927067, 0.7831874, 0.69746349, 0.35399976, 0.99469633, 0.0694458, 0.54711478])
threedecimalplaces = np.around(originalfloatvalues, decimals=3)
print(threedecimalplaces) #print [0.262 0.528 0.572 0.593 0.783 0.697 0.354 0.995 0.069 0.547]
threedecimalplacesround = np.round(originalfloatvalues, 3)
print(threedecimalplacesround) #print [0.262 0.528 0.572 0.593 0.783 0.697 0.354 0.995 0.069 0.547]

#84. Write a NumPy program to suppresses the use of scientific notation for small numbers in NumPy array.
scientificnotationarray = np.array([1.60000000e-10, 1.60000000e+00, 1.20000000e+03, 2.35000000e-01])
print(scientificnotationarray) #print [1.60e-10 1.60e+00 1.20e+03 2.35e-01]
np.set_printoptions(suppress=True)
print(scientificnotationarray) #print [   0.       1.6   1200.       0.235]
np.set_printoptions(suppress=False)
print(scientificnotationarray) #print [1.60e-10 1.60e+00 1.20e+03 2.35e-01]

#84. Write a NumPy program to suppresses the use of scientific notation for small numbers in NumPy array.  RM:  https://stackoverflow.com/questions/9777783/suppress-scientific-notation-in-numpy-when-creating-array-from-nested-list.  Also in numpyalltutorials.py Print options or display options section.
scientificnotationarray = np.array([1.60000000e-10, 1.60000000e+00, 1.20000000e+03, 2.35000000e-01])
print(scientificnotationarray) #print [1.60e-10 1.60e+00 1.20e+03 2.35e-01]
np.set_printoptions(suppress=True)
print(scientificnotationarray) #print [   0.       1.6   1200.       0.235]
np.set_printoptions(suppress=False)

#85. Write a NumPy program to create a NumPy array of 10 integers from a generator.
tenintegers = np.arange(0, 10)
print(tenintegers) #print [0 1 2 3 4 5 6 7 8 9]

#86. Write a NumPy program to add an extra column to a NumPy array.
column = np.arange(10, 70, 10).reshape(2, 3)
print(column)
'''
[[10 20 30]
 [40 50 60]]
'''
addedcolumn = np.array([[100], [200]])
print(addedcolumn)
'''
[[100]
 [200]]
'''
hstackinsertcolumn = np.hstack((column, addedcolumn))
print(hstackinsertcolumn)
'''
[[ 10  20  30 100]
 [ 40  50  60 200]]
'''

#87. Write a NumPy program to find unique rows in a NumPy array.  RM:  distinct rows
x = np.array([[20, 20, 20, 0], [0, 20, 20, 20], [0, 20, 20, 20], [20, 20, 20, 0], [10, 20, 20, 20]])
print(x)
'''
[[20 20 20  0]
 [ 0 20 20 20]
 [ 0 20 20 20]
 [20 20 20  0]
 [10 20 20 20]]
'''
uniquerows = np.unique(x, axis=0)
print(uniquerows)
'''
[[ 0 20 20 20]
 [10 20 20 20]
 [20 20 20  0]]
'''
uniquecolumns = np.unique(x, axis=1)
print(uniquecolumns)
'''
 [20  0 20]
 [20  0 20]
 [ 0 20 20]
 [20 10 20]]
'''

#88. Write a NumPy program to replace all elements of NumPy array that are greater than specified array.
greaterthanfive = np.array([[0.42436315, 0.48558583, 0.32924763], [0.7439979, 0.58220701, 0.38213418], [0.5097581, 0.34528799, 0.1563123]])
print(greaterthanfive)
'''
[[0.42436315 0.48558583 0.32924763]
 [0.7439979  0.58220701 0.38213418]
 [0.5097581  0.34528799 0.1563123 ]]
'''
replacegreaterthanfive = greaterthanfive > 0.5
greaterthanfive[replacegreaterthanfive] = 0.5
print(greaterthanfive)
'''
[[0.42436315 0.48558583 0.32924763]
 [0.5        0.5        0.38213418]
 [0.5        0.34528799 0.1563123 ]]
'''
#official solution
greaterthanfive[greaterthanfive > .5] = .5

#89. Write a NumPy program to remove specific elements in a NumPy array.  RM:  question asks remove first, fourth, and fifth elements.  Reference https://numpy.org/doc/stable/reference/generated/numpy.delete.html
defaultarray = np.arange(10, 110, 10)
print(defaultarray) #print [ 10  20  30  40  50  60  70  80  90 100]
removespecificnumber = np.delete(defaultarray, [0, 3, 4], axis=0)
print(removespecificnumber) #print [ 20  30  60  70  80  90 100]

#90. Write a NumPy program to replace the negative values in a NumPy array with 0.
originalarray = np.array([-1, -4, 0, 2, 3, 4, 5, -6])
print(originalarray) #print [-1 -4  0  2  3  4  5 -6]
originalarray[originalarray < 0] = 0
print(originalarray) #print [0 0 0 2 3 4 5 0]

import numpy as np

#91. Write a NumPy program to remove all rows in a NumPy array that contain non-numeric values.
numericandnonnumeric = np.array([[1., 2., 3.], [4., 5., np.nan], [7., 8., 9.], [1., 0., 1.]])
print(numericandnonnumeric)
'''
[[ 1.  2.  3.]
 [ 4.  5. nan]
 [ 7.  8.  9.]
 [ 1.  0.  1.]]
'''
for eachrow in numericandnonnumeric:
    #print(np.where(eachrow == np.isnan(eachrow)))
    print(eachrow == np.isnan(eachrow))
    if np.isnan(eachrow).any():
        pass
    else:
        print(eachrow)
    '''
    [False False False]
    [1. 2. 3.]
    [False False False]
    [False False False]
    [7. 8. 9.]
    [False  True False]
    [1. 0. 1.]
    '''
#official solution  #RM:  what if you don't know which row contains np.nan?  Need to search.
removenonnumeric = numericandnonnumeric[~np.isnan(numericandnonnumeric).any(axis=1)]
print(removenonnumeric)
'''
[[1. 2. 3.]
 [7. 8. 9.]
 [1. 0. 1.]]
'''

#92. Write a NumPy program to select indices satisfying multiple conditions in a NumPy array. Select the elements from the first array corresponding to elements in greater than 100 and less than 110.  Keep ['e' 'i'] in the second array.
samplea = np.array([97, 101, 105, 111, 117])
sampleb = np.array(["a", "e", "i", "o", "u"])
samplea100110exclusive = ((samplea > 100) & (samplea < 110))
print(samplea100110exclusive) #print [False  True  True False False]
samplea100110exclusive = samplea[samplea > 100]
samplea100110exclusive = samplea100110exclusive[samplea100110exclusive < 110]
print(samplea100110exclusive) #print [101 105]
sampleatryagain = np.array([97, 101, 105, 111, 117])
sampleatryagain[(sampleatryagain > 100) & (sampleatryagain < 110)]
print(sampleatryagain) #print [ 97 101 105 111 117]
sampleatryagain[(sampleatryagain > 100) & (sampleatryagain < 110)] *= -1
print(sampleatryagain) #print [  97 -101 -105  111  117]
#official answer
a = np.array([97, 101, 105, 111, 117])
b = np.array(["a", "e", "i", "o", "u"])
print("Elements from the second array  corresponding to elements in the first array  that are greater than 100 and less than 110:")
print(b[(100 < a) & (a < 110)]) #print ['e' 'i']

#93. Write a NumPy program to get the magnitude of a vector in NumPy.
originalarray = np.arange(1, 6)
print(originalarray) #print [1 2 3 4 5]
print(np.linalg.norm(originalarray)) #print 7.416198487095663

#94. Write a NumPy program to count the frequency of unique values in NumPy array.
frequencyuniquevalues = np.array([10, 10, 20, 10, 20, 20, 20, 30, 30, 50, 40, 40])
print(np.unique(frequencyuniquevalues)) #print [10 20 30 40 50]
print(np.unique(frequencyuniquevalues, return_counts=True)) #print (array([10, 20, 30, 40, 50]), array([3, 4, 2, 2, 1]))
uniquenumbers, countuniquenumbers = np.unique(frequencyuniquevalues, return_counts=True)
print(uniquenumbers) #print [10 20 30 40 50]
print(countuniquenumbers) #print [3 4 2 2 1]
print(np.array([uniquenumbers, countuniquenumbers])) #print [[10 20 30 40 50] [ 3  4  2  2  1]]
print(list((uniquenumbers, countuniquenumbers))) #print [array([10, 20, 30, 40, 50]), array([3, 4, 2, 2, 1])]

#95. Write a NumPy program to check whether the NumPy array is empty or not.  RM:  check null numpy null
emptyarray = np.array([])
isarrayempty = np.size(emptyarray) == 0
print(isarrayempty) #print True
#also
isarrayempty = emptyarray.size == 0
print(isarrayempty) #print True

#96. Write a NumPy program to divide each row by a vector element.
twentyforty = np.array([[20, 20, 20], [30, 30, 30], [40, 40, 40]])
print(twentyforty) #print [[20 20 20] [30 30 30] [40 40 40]]
divideby = np.array([20, 30, 40])
print(twentyforty / divideby)
'''
[[1.         0.66666667 0.5       ]
 [1.5        1.         0.75      ]
 [2.         1.33333333 1.        ]]
'''
print(twentyforty[0] / divideby[0]) #print [1. 1. 1.]
print(twentyforty.shape[1]) #print 3
answernumpy = np.array([])
for x in range(0, twentyforty.shape[1]):
    print(twentyforty[x] / divideby[x]) #print [1. 1. 1.]
    answernumpy = np.append(answernumpy, twentyforty[x] / divideby[x])
print(answernumpy) #print [1. 1. 1. 1. 1. 1. 1. 1. 1.]
reshapeanswernumpy = answernumpy.reshape(twentyforty.shape[0], twentyforty.shape[1])
print(reshapeanswernumpy) #print [[1. 1. 1.] [1. 1. 1.] [1. 1. 1.]]
#official solution
print(twentyforty / divideby[:, None]) #print [[1. 1. 1.] [1. 1. 1.] [1. 1. 1.]]
#bonus
bonusarray = np.arange(1, 11)
print(bonusarray) #print [ 1  2  3  4  5  6  7  8  9 10]
print(bonusarray[:, None]) #print [[ 1] [ 2] [ 3] [ 4] [ 5] [ 6] [ 7] [ 8] [ 9] [10]]
print(type(bonusarray[:, None])) #print <class 'numpy.ndarray'>
bonusarraynone = bonusarray[:, None]
print(bonusarray.size) #print 10
print(bonusarray.shape) #print (10,)
print(bonusarray[4:7, None]) #print [[ 5] [ 6] [ 7]]

#97. Write a NumPy program to print all the values of an array.
#official solution
#np.set_printoptions(threshold=np.nan)
x = np.zeros((4, 4))
#print(x) #print ValueError: threshold must be non-NAN, try sys.maxsize for untruncated representation

#98. Write a NumPy program to convert the raw data in an array to a binary string and then create an array.
originalarray = np.array([10., 20., 30.])
#official solution
print(originalarray) #print [10. 20. 30.]
converttobinarystring = originalarray.tostring() #print b'\x00\x00\x00\x00\x00\x00$@\x00\x00\x00\x00\x00\x004@\x00\x00\x00\x00\x00\x00>@'
print(converttobinarystring)
convertfrombinarystring = np.fromstring(converttobinarystring)
print(convertfrombinarystring) #print [10. 20. 30.]

#99. Write a NumPy program to sum and compute the product of a NumPy array elements.
originalarray = np.array([10., 20., 30.])
print(originalarray.sum()) #print 60.0
print(originalarray.prod())  #print 6000.0.  multiply or product

#100. Write a NumPy program to take values from a source array and put them at specified indices of another array.
originalarray = np.array([0., 10., 20., 30., 40.])
originalarray[0] = 10.
originalarray[4] = 30.
print(originalarray) #print [10. 10. 20. 30. 30.]
#official solution
x = np.array([0, 10, 20, 30, 40], dtype=np.float)
replacementnumbers = np.array([10, 30], dtype=np.float)
print(x) #print [ 0. 10. 20. 30. 40.]
x.put([0, 4], replacementnumbers)
print(x) #print [10. 10. 20. 30. 30.]

#101. Write a NumPy program to print the full NumPy array, without truncation.
zerotonineteeneightynine = np.arange(0, 2000)
print(zerotonineteeneightynine) #print [   0    1    2 ... 1997 1998 1999]

#102. Write a NumPy program to convert a NumPy array into a csv file.
#official solution
numpyarray = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(numpyarray) #print [[10 20 30] [40 50 60] [70 80 90]]
np.savetxt("arraytocsv.csv", numpyarray, delimiter=",")

#103. Write a NumPy program to calculate the Euclidean distance.
#official solution
from scipy.spatial import distance
p1 = (1, 2, 3)
p2 = (4, 5, 6)
d = distance.euclidean(p1, p2)
print("Euclidean distance: ", d) #print Euclidean distance:  5.196152422706632

#104. Write a NumPy program to access last two columns of a multidimensional columns.
twodimensionarray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(twodimensionarray) #print [[1 2 3] [4 5 6] [7 8 9]]
print(twodimensionarray[:, 1:3]) #print [[2 3] [5 6] [8 9]]
print(twodimensionarray[:, [1, 2]]) #print [[2 3] [5 6] [8 9]] #RM:  slice slicing using exact index numbers

#105. Write a NumPy program to read a CSV data file and store records in an array.  RM:  open csv file, load csv file.  #Additional procedures https://www.pythonpool.com/numpy-read-csv/
getcsvdata = np.genfromtxt("genfromtxtcsvfile.csv", dtype=["S10", "float32", "float32", "float32", "float32"], delimiter=",")  #The S in S10 must be upper case.
print(getcsvdata)
'''
[(b'Date',    nan,     nan,    nan,    nan)
 (b'03-10-16', 774.25, 776.065, 769.5 , 772.56)
 (b'04-10-16', 776.03, 778.71 , 772.89, 776.43)
 (b'05-10-16', 779.31, 782.07 , 775.65, 776.47)
 (b'06-10-16', 779.  , 780.48 , 775.54, 776.86)
 (b'07-10-16', 779.66, 779.66 , 770.75, 775.08)]
'''

#106. Write a NumPy program to count the occurrence of a specified item in a given NumPy array.
countitems = np.array([10, 20, 20, 20, 20, 0, 20, 30, 30, 30, 0, 0, 20, 20, 0])
print(countitems) #print [10 20 20 20 20  0 20 30 30 30  0  0 20 20  0]
count10 = np.count_nonzero(countitems == 10)
print(count10) #print 1
count20 = np.count_nonzero(countitems == 20)
print(count20) #print 7
count30 = np.count_nonzero(countitems == 30)
print(count30) #print 3
count0 = np.count_nonzero(countitems == 0)
print(count0) #print 4
countitemsunique = np.array([10, 20, 20, 20, 20, 0, 20, 30, 30, 30, 0, 0, 20, 20, 0])
unique, counts = np.unique(countitemsunique, return_counts=True)
print(dict(zip(unique, counts))) #print {0: 4, 10: 1, 20: 7, 30: 3}

#107. Write a NumPy program to calculate percentiles for a sequence or single-dimensional NumPy array.
nums = np.array([1, 2, 3, 4, 5])
percentile50 = np.percentile(nums, 50)
print(percentile50) #print 3.0
percentile40 = np.percentile(nums, 40)
print(percentile40) #print 2.6
percentile90 = np.percentile(nums, 90)
print(percentile90) #print 4.6

#108. Write a NumPy program to convert a PIL Image into a NumPy array.
#official solution
# import PIL
# img_data = PIL.Image.open("w3resource-logo.png" )
# img_arr = np.array(img_data)
# print(img_arr)

#109. Write a NumPy program to convert a NumPy array to an image. Display the image.
#official solution
# from PIL import Image
# img_w, img_h = 200, 200
# data = np.zeros((img_h, img_w, 3), dtype=np.uint8)
# data[100, 100] = [255, 0, 0]
# img = Image.fromarray(data, 'RGB')
# img.save('test.png')
# img.show()

#110. Write a NumPy program to remove nan values from a given array.  #RM:  remove blanks, remove nulls, delete blanks, delete nulls
#official solution
x = np.array([200, 300, np.nan, np.nan, np.nan, 700])
y = np.array([[1, 2, 3], [np.nan, 0, np.nan], [6, 7, np.nan]])
print("Original array:")
print(x)
'''
Original array:
[200. 300.  nan  nan  nan 700.]
'''
print("After removing nan values:")
result = x[np.logical_not(np.isnan(x))]
print(result)
'''
After removing nan values:
[200. 300. 700.]
'''
print("\nOriginal array:")
print(y)
'''
Original array:
[[ 1.  2.  3.]
 [nan  0. nan]
 [ 6.  7. nan]]
'''
print("After removing nan values:")
result = y[np.logical_not(np.isnan(y))]
print(result)
'''
After removing nan values:
[1. 2. 3. 0. 6. 7.]
[[1 4]
 [2 4]
 [3 4]
 [1 5]
 [2 5]
 [3 5]]
'''

#111. Write a NumPy program to create a Cartesian product of two arrays into single array of 2D points.
#official solution
x = np.array([1, 2, 3])
y = np.array([4, 5])
result = np.transpose([np.tile(x, len(y)), np.repeat(y, len(x))])
print(result)
'''
[[1 4]
 [2 4]
 [3 4]
 [1 5]
 [2 5]
 [3 5]]
'''

#112. Write a NumPy program to get the memory usage by NumPy arrays.
anarray = np.arange(0, 11)
print(anarray) #print [ 0 1 2 3 4 5 6 7 8 9 10]
numberofelements = anarray.size
print(numberofelements) #print 11
memoryinbyteseachelementtakes = anarray.itemsize
print(memoryinbyteseachelementtakes) #print 8
totalitemsize = numberofelements * memoryinbyteseachelementtakes
print(totalitemsize) #print 88
print(anarray.nbytes) #print 88
#official solution
from sys import getsizeof
print(getsizeof(anarray)) #print 184

#113. Write a NumPy program to build an array of all combinations of three NumPy arrays.
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5])
array3 = np.array([6, 7])
allcombinations = np.array(np.meshgrid(array1, array2, array3)).T.reshape(-1, 3)
print(allcombinations)
'''
[[1 4 6]
 [1 5 6]
 [2 4 6]
 [2 5 6]
 [3 4 6]
 [3 5 6]
 [1 4 7]
 [1 5 7]
 [2 4 7]
 [2 5 7]
 [3 4 7]
 [3 5 7]]
'''

#114. Write a NumPy program to create random set of rows from 2D array.  RM:  create a random 2D array.  Five rows, three columns.  Elements between 0 and 5 inclusive.
random2darray = np.random.randint(0, 6, size=(5, 3))
print(random2darray)
'''
[[1 2 0]
 [0 4 5]
 [0 1 4]
 [4 2 5]
 [1 5 1]]
'''

#115. Write a NumPy program to find indices of elements equal to zero in a NumPy array.
samplearray = np.array([1, 0, 2, 0, 3, 0, 4, 5, 6, 7, 8])
print(samplearray) #print [1 0 2 0 3 0 4 5 6 7 8]
counter = 0
length = samplearray.size
print(length) #print 11
for findzeroforloop in range(0, length):
    if samplearray[findzeroforloop] == 0:
        print(findzeroforloop) #print 1\n 3\n 5\n
findzeros = np.where(samplearray == 0)
print(findzeros) #print (array([1, 3, 5]),)
print(findzeros[0]) #print [1,3,5]

#116. Write a NumPy program to compute the histogram of a set of data.  #RM:  question is a Matplotlib import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
countthenumbers = ([1, 2, 1, 4])
bins = [0, 1, 2, 3, 4, 5]
plt.hist(countthenumbers, bins)
plt.title("Histogram x-axis or bins range inclusive to exclusive.  Two 1's.  One 2's.  One 4's.")
plt.show()

#117. Write a NumPy program to compute the line graph of a set of data.
import matplotlib.pyplot as plt
xvalues = np.arange(1, 51)
yvalues = np.random.randint(0, 3, 50)
print(xvalues)
print(yvalues)
plt.title("Line chart xvalues and its corresponding yvalues")
plt.plot(xvalues, yvalues)
plt.show()


#118. Write a NumPy program to find the position of the index of a specified value greater than existing value in NumPy array.
#RM:  I looked at the solution and pictorial presentation.  I don't understand.

#119. Write a NumPy program to add a new row to an empty NumPy array.
emptyarray = np.array([], dtype=np.int8)
print(emptyarray) #print []
addarray1 = np.arange(10, 31, 10)
print(addarray1) #print [10 20 30]
addarray2 = np.arange(40, 61, 10)
print(addarray2) #print [40 50 60]
emptyarray = np.append(emptyarray, addarray1)
print(emptyarray) #print [10 20 30]
emptyarray = np.append(emptyarray, addarray2)
print(emptyarray) #print [10 20 30 40 50 60]
emptyarray2d = emptyarray.reshape(2, 3)
print(emptyarray2d)

#bonus insert values in an existing numpy by index or by position
a = np.array([[1, 1], [2, 2], [3, 3]])
print(a)
'''
[[1 1]
 [2 2]
 [3 3]]
'''
insert55firstindexandflatten = np.insert(a, 1, 55)
print(insert55firstindexandflatten) #print [ 1 55  1  2  2  3  3]
insert55firstindexbycolumns = np.insert(a, 1, 55, axis=1)
print(insert55firstindexbycolumns)
'''
[[ 1 55  1]
 [ 2 55  2]
 [ 3 55  3]]
'''
insert55firstindexbyrow = np.insert(a, 1, 55, axis=0)
print(insert55firstindexbyrow)
'''
[[ 1  1]
 [55 55]
 [ 2  2]
 [ 3  3]]
'''

#120. Write a NumPy program to get the index of a maximum element in a NumPy array along one axis.
originalarray = np.array([[1, 2, 3], [500, 3, 1]])
print(originalarray)
'''
[[  1   2   3]
 [500   3   1]]
'''
print(originalarray.max()) #print 500
print(originalarray.argmax()) #print 3
print(np.unravel_index(originalarray.argmax(), originalarray.shape)) #print (1, 0)

#121. Write a NumPy program to join a sequence of arrays along a new axis.
firstarray = np.array([1, 2, 3])
secondarray = np.array([4, 5, 6])
combinearray = np.array([firstarray, secondarray]) #append array
print(combinearray)
'''
[[1 2 3]
 [4 5 6]]
'''
#also
print(np.vstack((firstarray, secondarray)))
'''
[[1 2 3]
 [4 5 6]]
'''
firstarray = np.array([[1], [2], [3]])
secondarray = np.array([[4], [5], [6]])
print(firstarray)
'''
[[[1]
  [2]
  [3]]
'''
print(secondarray)
'''
[[4]
 [5]
 [6]]
'''
print(np.array([firstarray, secondarray]))
'''
[[[1]
  [2]
  [3]]

 [[4]
  [5]
  [6]]]
'''
print(np.vstack((firstarray, secondarray)))
'''
[[1]
 [2]
 [3]
 [4]
 [5]
 [6]]
'''

#122. Write a NumPy program to find the index of the sliced elements as follows from a given 4x4 array.
givenarray = np.arange(0, 16)
print(givenarray) #print [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
givenarrayreshaped = givenarray.reshape(4, 4)
print(givenarrayreshaped)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
'''
find5 = np.where(givenarrayreshaped == 5)
print(find5) #print (array([1]), array([1]))
print(find5[0]) #print [1]
print(list(find5)) #print [array([1]), array([1])]
print(len(list(find5))) #print 2
print((list(find5)[0])) #print [1]
print((list(find5)[1])) #print [1]
#RM:  question is provide a list of indicies in the array to return a slice of numbers.
print0and5and11 = givenarrayreshaped[[0, 1, 2], [0, 1, 3]]
print(print0and5and11) #print [ 0  5 11]

import numpy as np

#123. Write a NumPy program to create two arrays of size bigger and smaller than a given array.  RM:  I told myself there must be a resize function.  Actually, there is.
initialsizearray = np.arange(0, 16).reshape(4, 4)
print(initialsizearray)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
'''
zeroonetwothree = np.resize(initialsizearray, (2, 2))
print(zeroonetwothree)
'''
[[0 1]
 [2 3]]
'''
sixbysixsixrowscolumsn = np.resize(initialsizearray, (6, 6))
print(sixbysixsixrowscolumsn)
'''
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15  0  1]
 [ 2  3  4  5  6  7]
 [ 8  9 10 11 12 13]
 [14 15  0  1  2  3]]
'''
resizefourrowssixcolumns = np.resize(initialsizearray, (4, 6))
print(resizefourrowssixcolumns)
'''
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15  0  1]
 [ 2  3  4  5  6  7]]
'''

#124. Write a NumPy program to broadcast on different shapes of arrays where p(3,3) + q(3).
originalarray1 = np.array([[0, 0, 0], [1, 2, 3], [4, 5, 6]])
print(originalarray1)
'''
[[0 0 0]
 [1 2 3]
 [4 5 6]]
'''
originalarray2 = np.array([10, 11, 12])
print(originalarray2) #print [10 11 12]
newarray = originalarray1 + originalarray2
print(newarray)
'''
[[10 11 12]
 [11 13 15]
 [14 16 18]]
'''

#125. Write a NumPy program to broadcast on different shapes of arrays where a(,3) + b(3).
originalarray1 = np.array([[0], [10], [20]])
print(originalarray1)
'''
[[ 0]
 [10]
 [20]]
'''
originalarray2 = np.array([10, 11, 12])
print(originalarray2) #print [10 11 12]
newarray = originalarray1 + originalarray2
print(newarray)
'''
[[10 11 12]
 [20 21 22]
 [30 31 32]]
'''

#126. Write a NumPy program to rearrange the dimensions of a given array.
originalarray = np.arange(0, 24).reshape(6, 4)
print(originalarray)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]
 [16 17 18 19]
 [20 21 22 23]]
'''
transposemethod = originalarray.transpose()
print(transposemethod)
'''
[[ 0  4  8 12 16 20]
 [ 1  5  9 13 17 21]
 [ 2  6 10 14 18 22]
 [ 3  7 11 15 19 23]]
'''

#127. Write a NumPy program to stack arrays in sequence horizontally (column wise).  #RM:  concatenate, combine
originalarray1 = np.arange(0, 9).reshape(3, 3)
print(originalarray1)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
'''
originalarray2 = np.arange(0, 25, 3).reshape(3, 3)
print(originalarray2)
'''
[[ 0  3  6]
 [ 9 12 15]
 [18 21 24]]
'''
concatenatehorizontally = np.concatenate((originalarray1, originalarray2), axis=1)
print(concatenatehorizontally)
'''
[[ 0  1  2  0  3  6]
 [ 3  4  5  9 12 15]
 [ 6  7  8 18 21 24]]
'''

#128. Write a NumPy program to stack arrays in sequence vertically.  #RM:  concatenate, combine
originalarray1 = np.arange(0, 9).reshape(3, 3)
print(originalarray1)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
'''
originalarray2 = np.arange(0, 25, 3).reshape(3, 3)
print(originalarray2)
'''
[[ 0  3  6]
 [ 9 12 15]
 [18 21 24]]
'''
concatenatehorizontally = np.concatenate((originalarray1, originalarray2), axis=0)
print(concatenatehorizontally)
'''
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 0  3  6]
 [ 9 12 15]
 [18 21 24]]
'''

#129. Write a NumPy program to stack 1-D arrays as columns wise.
arrayone = np.array([1, 2, 3])
arraytwo = np.array([2, 3, 4])
stackcolumnwise = np.concatenate((arrayone, arraytwo), axis=0)
print(stackcolumnwise) #print [1 2 3 2 3 4]
incorrectstackcolumnwise = stackcolumnwise.reshape(3, 2)
print(incorrectstackcolumnwise)
'''
[[1 2]
 [3 2]
 [3 4]]
'''
correctstackcolumnwise = np.column_stack((arrayone, arraytwo))
print(correctstackcolumnwise)
'''
[[1 2]
 [2 3]
 [3 4]]
'''

#130. Write a NumPy program to stack 1-D arrays as row wise.
arrayone = np.array([1, 2, 3])
arraytwo = np.array([2, 3, 4])
stackcolumnwise = np.concatenate((arrayone, arraytwo), axis=0)
print(stackcolumnwise) #print [1 2 3 2 3 4]
print(stackcolumnwise.reshape(2, 3))
'''
[[1 2 3]
 [2 3 4]]
'''
correctstackrowwise = np.row_stack((arrayone, arraytwo))
print(correctstackrowwise)
'''
[[1 2 3]
 [2 3 4]]
'''

#131. Write a NumPy program to split a given array into multiple sub-arrays vertically (row-wise).
originalarray = np.arange(0, 16, dtype=np.float16)
print(originalarray) #print [ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12. 13. 14. 15.]
verticalsplit = np.split(originalarray, 4)
print(verticalsplit) #print [array([0., 1., 2., 3.], dtype=float16), array([4., 5., 6., 7.], dtype=float16), array([ 8.,  9., 10., 11.], dtype=float16), array([12., 13., 14., 15.], dtype=float16)]
#official solution
fourbyfourarray = originalarray.reshape(4, 4)
print(fourbyfourarray)
'''
[[ 0.  1.  2.  3.]
 [ 4.  5.  6.  7.]
 [ 8.  9. 10. 11.]
 [12. 13. 14. 15.]]
'''
verticalsplit = np.vsplit(fourbyfourarray, 2)
print(verticalsplit) #print [array([[0., 1., 2., 3.], [4., 5., 6., 7.]], dtype=float16), array([[ 8.,  9., 10., 11.], [12., 13., 14., 15.]], dtype=float16)]

#132. Write a NumPy program to split array into multiple sub-arrays along the 3rd axis.
originalarray = np.arange(0, 16, dtype=np.float16)
print(originalarray) #print [ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12. 13. 14. 15.]
fourbyfourarray = originalarray.reshape(2, 2, 4)
print(fourbyfourarray)
'''
[[[ 0.  1.  2.  3.]
  [ 4.  5.  6.  7.]]

 [[ 8.  9. 10. 11.]
  [12. 13. 14. 15.]]]
'''
multiplesubarrays = np.dsplit(fourbyfourarray, 2)
print(multiplesubarrays)
'''
[array([[[ 0.,  1.],
        [ 4.,  5.]],

       [[ 8.,  9.],
        [12., 13.]]], dtype=float16), array([[[ 2.,  3.],
        [ 6.,  7.]],

       [[10., 11.],
        [14., 15.]]], dtype=float16)]
'''

#133. Write a NumPy program to count the number of dimensions, number of elements and number of bytes for each element in a given array.
samplearray1 = np.arange(0, 12)
samplearray2 = np.arange(12, 24)
samplearray = np.concatenate((samplearray1, samplearray2))
print(samplearray) #print [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
samplearray = samplearray.reshape(2, 12)
print(samplearray) #print [[ 0  1  2  3  4  5  6  7  8  9 10 11] [12 13 14 15 16 17 18 19 20 21 22 23]]
fastersamplearray = np.arange(0, 24).reshape(2, 12)
print(fastersamplearray) #print [[ 0  1  2  3  4  5  6  7  8  9 10 11] [12 13 14 15 16 17 18 19 20 21 22 23]]
print(fastersamplearray.ndim) #print 2
print(fastersamplearray.size) #print 24
print(fastersamplearray.itemsize) #print 8

#134. Write a NumPy program to extract all the elements of the first row from a given (4x4) array.
givenarray = np.arange(0, 16).reshape(4, 4)
print(givenarray)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
'''
extractfirstrow = givenarray[0, :]
print(extractfirstrow) #print [0 1 2 3]

#135. Write a NumPy program to extract all the elements of the second row from a given (4x4) array.
givenarray = np.arange(0, 16).reshape(4, 4)
extractsecondrow = givenarray[1, :]
print(extractsecondrow) #print [4 5 6 7]

#136. Write a NumPy program to extract all the elements of the third column from a given (4x4) array.
givenarray = np.arange(0, 16).reshape(4, 4)
extractthirdcolumn = givenarray[:, 2]
print(extractthirdcolumn) #print [ 2  6 10 14]

#137. Write a NumPy program to extract first and second elements of the first and second rows from a given (4x4) array.
givenarray = np.arange(0, 16).reshape(4, 4)
extractfirstsecond = givenarray[0:2, 0:2]
print(extractfirstsecond)
'''
[[0 1]
 [4 5]]
'''

#138. Write a NumPy program to extract third and fourth elements of the first and second rows from a given (4x4) array.
givenarray = np.arange(0, 16).reshape(4, 4)
extractthirdfourth = givenarray[0:2, 2:4]
print(extractthirdfourth)
'''
[[2 3]
 [6 7]]
'''

#139. Write a NumPy program to extract first and third elements of the first and third rows from a given (4x4) array.
givenarray = np.arange(0, 16).reshape(4, 4)
extractfirstthird = givenarray[0::2, 0:3:2]
print(extractfirstthird)
'''
[[ 0 2]
[ 8 10]]
'''

#140. Write a NumPy program to extract second and fourth elements of the second and fourth rows from a given (4x4) array.
givenarray = np.arange(0, 16).reshape(4, 4)
extracsecondfourth = givenarray[1::2, 1::2]
print(extracsecondfourth)
'''
[[ 5  7]
 [13 15]]
'''

#141. Write a NumPy program to extract all the elements of the second and third columns from a given (4x4) array.
givenarray = np.arange(0, 16).reshape(4, 4)
extractsecondthirdcolumns = givenarray[:, 1:3]
print(extractsecondthirdcolumns)
'''
[[ 1  2]
 [ 5  6]
 [ 9 10]
 [13 14]]
'''

#142. Write a NumPy program to extract all the elements of the first and fourth columns from a given (4x4) array.
givenarray = np.arange(0, 16).reshape(4, 4)
extractfirstfourthcolumns = givenarray[:, 0::3]
print(extractfirstfourthcolumns)
'''
[[ 0  3]
 [ 4  7]
 [ 8 11]
 [12 15]]
'''

#143. Write a NumPy program to extract first element of the second row and fourth element of fourth row from a given (4x4) array.
givenarray = np.arange(0, 16).reshape(4, 4)
extract4and15 = givenarray[[1, 3], [0, 3]]
print(extract4and15) #print [ 4 15]  RM:  4 is row 1 column 0.  15 is row 3 column 3.

#144. Write a NumPy program to extract second and third elements of the second and third rows from a given (4x4) array.
givenarray = np.arange(0, 16).reshape(4, 4)
extractsecondthird = givenarray[1:3, 1:3]
print(extractsecondthird)
'''
[[ 5  6]
 [ 9 10]]
'''

#145. Write a NumPy program to extract first, third and fifth elements of the third and fifth rows from a given (6x6) array.
givensixbysixarray = np.arange(0, 36).reshape(6, 6)
print(givensixbysixarray)
'''
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]
 [24 25 26 27 28 29]
 [30 31 32 33 34 35]]
'''
extract135elements = givensixbysixarray[2:5:2, 0:5:2]
print(extract135elements)
'''
[[12 14 16]
 [24 26 28]]
'''

#146. Write a NumPy program to add two arrays A and B of sizes (3,3) and (,3).
arrayones = np.ones((3, 3))
print(arrayones)
'''
[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]
'''
arraytwos = np.arange(0, 3)
print(arraytwos)
addtwoarrays = arrayones + arraytwos
print(addtwoarrays)
'''
[[1. 2. 3.]
 [1. 2. 3.]
 [1. 2. 3.]]
'''

#147. Write a NumPy program to create an array that represents the rank of each item of a given array.
#source https://stackoverflow.com/questions/5284646/rank-items-in-an-array-using-python-numpy-without-sorting-array-twice
originalarray = np.array([24, 27, 30, 29, 18, 14])
order = originalarray.argsort()
print(order) #print [5 4 0 1 3 2]
ranks = order.argsort()
print(ranks) #print [2 3 5 4 1 0]
#official solution
argsortoriginalarray = originalarray.argsort()
print(argsortoriginalarray) #print [5 4 0 1 3 2]
ranksarray = np.empty_like(argsortoriginalarray)
print(ranksarray) #print [     140640521526592             46648160      140640270794400 -7007658560076954526      140640270369328      140640270794536]  #RM:  ranksarray is random numbers printed
ranksarray[argsortoriginalarray] = np.arange(len(originalarray))
print(ranksarray) #print [2 3 5 4 1 0]

#148. Write a NumPy program to copy data from a given array to another array.
originalarray = np.array([24, 27, 30, 29, 18, 14])
#official solution
copydata = np.empty_like(originalarray)
print(copydata) #print [24 27 30 29 18 14]
copydata[:] = originalarray
print(copydata) #print [24 27 30 29 18 14]

#149. Write a NumPy program to find elements within range from a given array of numbers.  RM:  find the index positions for the numbers between 7 and 20 inclusive.
givenarray = np.array([1, 3, 7, 9, 10, 31, 14, 17, 29])
print(givenarray) #print [ 1  3  7  9 10 31 14 17 29]
indexnumbers7and20 = np.where(np.logical_and(givenarray >= 7, givenarray <= 20))
print(indexnumbers7and20) #print (array([2, 3, 4, 6, 7]),)
print(indexnumbers7and20[0]) #print [2 3 4 6 7]

#150. Write a NumPy program to swap columns in a given array.
originalarray = np.arange(0, 12).reshape(3, 4)
print(originalarray)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''
#first column and second column switch columns
originalarray[:, [1, 0]] = originalarray[:, [0, 1]]
print(originalarray)
'''
[[ 1  0  2  3]
 [ 5  4  6  7]
 [ 9  8 10 11]]
'''
#bonus swap a row.  first row and third row switch rows
originalarray = np.arange(0, 12).reshape(3, 4)
originalarray[[2, 0], :] = originalarray[[0, 2], :]
print(originalarray)
'''
[[ 8  9 10 11]
 [ 4  5  6  7]
 [ 0  1  2  3]]
'''

#151. Write a NumPy program to get the row numbers in given array where at least one item is larger than a specified value.
rowgreaterthan10 = np.arange(0, 36).reshape(4, 9)
print(rowgreaterthan10)
'''
[[ 0  1  2  3  4  5  6  7  8]
 [ 9 10 11 12 13 14 15 16 17]
 [18 19 20 21 22 23 24 25 26]
 [27 28 29 30 31 32 33 34 35]]
'''
whererowcolumngreaterthan10 = np.where(rowgreaterthan10 > 10)
print(whererowcolumngreaterthan10)
'''
(array([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3,
       3, 3, 3]), array([2, 3, 4, 5, 6, 7, 8, 0, 1, 2, 3, 4, 5, 6, 7, 8, 0, 1, 2, 3, 4, 5,
       6, 7, 8]))
'''
whererowsreaterthan10 = np.where(rowgreaterthan10 > 10)[0]
print(whererowsreaterthan10) #print [1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3]
print(set(whererowsreaterthan10)) #print {1, 2, 3}
#official solution
resultrows = np.where(np.any(rowgreaterthan10 > 10, axis=1))
print(resultrows) #print (array([1, 2, 3]),)
resultcolumns = np.where(np.any(rowgreaterthan10 > 10, axis=0))
print(resultcolumns) #print (array([0, 1, 2, 3, 4, 5, 6, 7, 8]),)  RM:  columns?  I didn't confirm.
resultnoaxis = np.where(np.any(rowgreaterthan10 > 10))
print(resultnoaxis) #print (array([0]),)

#152. Write a NumPy program to calculate the sum of all columns of a 2D NumPy array.
sumcolumns = np.arange(0, 36).reshape(4, 9)
print(sumcolumns)
'''
[[ 0  1  2  3  4  5  6  7  8]
 [ 9 10 11 12 13 14 15 16 17]
 [18 19 20 21 22 23 24 25 26]
 [27 28 29 30 31 32 33 34 35]]
'''
sumbycolumn = sumcolumns.sum(axis=0)
print(sumbycolumn) #print [54 58 62 66 70 74 78 82 86]

#153. Write a NumPy program to extract upper triangular part of a NumPy matrix.
triangle = np.arange(0, 18).reshape(6, 3)
print(triangle)
'''
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]
 [12 13 14]
 [15 16 17]]
'''
#official solution
righttrianglezeroapexthreerows = triangle[np.triu_indices(3)]
print(righttrianglezeroapexthreerows) #print [0 1 2 4 5 8]
righttrianglezeroapextworows = triangle[np.triu_indices(2)]
print(righttrianglezeroapextworows) #print [0 1 4]
#bonus
righttriangleeightapexthreerows = triangle[np.tril_indices(3)]
print(righttriangleeightapexthreerows) #print [0 3 4 6 7 8]
righttriangleeightapextworows = triangle[np.tril_indices(2)]
print(righttriangleeightapextworows) #print print [0 3 4]
triangle[np.triu_indices(3)] = 111
print(triangle)
'''
[[111 111 111]
 [  3 111 111]
 [  6   7 111]
 [  9  10  11]
 [ 12  13  14]
 [ 15  16  17]]
'''
triangle[np.tril_indices(3)] = 888
print(triangle)
'''
[[888 111 111]
 [888 888 111]
 [888 888 888]
 [  9  10  11]
 [ 12  13  14]
 [ 15  16  17]]
'''

#154. Write a NumPy program to get a copy of a matrix with the elements below the k-th diagonal zeroed.
originalarray = np.arange(1, 13).reshape(4, 3)
print(originalarray)
'''
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
'''
zerodiagonaluppertriangle = np.triu(originalarray, 0)
print(zerodiagonaluppertriangle)
'''
[[1 2 3]
 [0 5 6]
 [0 0 9]
 [0 0 0]]
'''
#bonus
originalarray = np.arange(1, 13).reshape(4, 3)
zerodiagonallowertriangle = np.tril(originalarray, -1)
print(zerodiagonallowertriangle)
'''
[[ 0  0  0]
 [ 4  0  0]
 [ 7  8  0]
 [10 11 12]]
'''

#155. Write a NumPy program to check whether a Numpy array contains a specified row.
generalrow = np.arange(0, 20).reshape(4, 5)
print(generalrow)
'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
'''
generalrowzerotofour = [0, 1, 2, 3, 4]
generalrowzerofive = [0, 1, 2, 3, 5]
generalrow15to19 = [15, 16, 17, 18, 19]
print(generalrowzerotofour in generalrow.tolist()) #print True
print(generalrowzerofive in generalrow.tolist()) #print True
print(generalrow15to19 in generalrow.tolist()) #print True
#bonus
print(generalrowzerotofour in generalrow) #print True
print(generalrowzerofive in generalrow) #print True
print(generalrow15to19 in generalrow) #print True

#156. Write a NumPy program to calculate averages without NaNs along a given array.
originalarray = np.array([[10, 20, 30], [40, 50, np.nan], [np.nan, 6, np.nan], [np.nan, np.nan, np.nan]])
print(originalarray)
'''
[[10. 20. 30.]
 [40. 50. nan]
 [nan  6. nan]
 [nan nan nan]]
'''
print(originalarray.mean) #print <built-in method mean of numpy.ndarray object at 0x7f6c80601e40>
averageoriginalarray = originalarray.mean()
print(averageoriginalarray) #print nan
averageoriginalarrayrow = originalarray.mean(axis=1)
print(averageoriginalarrayrow) #print [20. nan nan nan]
averageoriginalarrayrowignorenan = np.nanmean(originalarray, axis=1) #ignore null
print(averageoriginalarrayrowignorenan) #print [20. 45.  6. nan]

#157. Write a NumPy program to create a new array which is the average of every consecutive triplet of elements of a given array.  RM:  Every three numbers are averaged.  There are 12 numbers.  Return four averages.  Average of every consecutive triplet of elements.
originalarray = np.array([1, 2, 3, 2, 4, 6, 1, 2, 12, 0, -12, 6])
sumeverythree = np.add.reduceat(originalarray, np.arange(0, len(originalarray), 3))
print(sumeverythree) #print [ 6 12 15 -6]
reshapethreecolumnsevenly = originalarray.reshape(-1, 3) #RM:  -1 means parameter determined based on actual condition automatically
print(reshapethreecolumnsevenly)
'''
[[  1   2   3]
 [  2   4   6]
 [  1   2  12]
 [  0 -12   6]]
'''
averagethreenumberseachrow = reshapethreecolumnsevenly.mean(axis=1)
print(averagethreenumberseachrow) #print [ 2.  4.  5. -2.]  #RM:  it appears there's no numpy function
#bonus
reshapetworowsevenly = originalarray.reshape(2, -1) #RM:  -1 means parameter determined based on actual condition automatically
print(reshapetworowsevenly)
'''
[[  1   2   3   2   4   6]
 [  1   2  12   0 -12   6]]
'''

#158. Write a NumPy program to calculate average values of two given NumPy arrays.  RM:  Question is not average both arrays individually.  Add the two arrays and then average by dividing by two.
firstarray = np.array([[0, 1], [2, 3]])
secondarray = np.array([[4, 5], [0, 3]])
print(firstarray)
'''
[[0 1]
 [2 3]]
'''
print(secondarray)
'''
[[4 5]
 [0 3]]
'''
combinearrays = (firstarray + secondarray)
print(combinearrays)
'''
[[4 6]
 [2 6]]
'''
averagevauuecombinearrays = combinearrays / 2
print(averagevauuecombinearrays)
'''
[[2. 3.]
 [1. 3.]]
'''

#159. Write a NumPy program to rearrange columns of a given NumPy 2D array using given index positions.
arrange = np.array([[11, 22, 33, 44, 55], [66, 77, 88, 99, 100]])
print(arrange)
'''
[[ 11  22  33  44  55]
 [ 66  77  88  99 100]]
'''
#rearrange = arrange[[0:2, [1, 3, 0, 4, 2]]  #error
#rearrange = arrange[:, [1, 3, 0, 4, 2]]  #also correct
rearrange = arrange[0:2, [1, 3, 0, 4, 2]]
print(rearrange)
'''
[[ 22  44  11  55  33]
 [ 77  99  66 100  88]]
'''

#160. Write a NumPy program to find the k smallest values of a given NumPy array.
originalarray = np.array([1, 7, 8, 2, 0.1, 3, 15, 2.5])
print(originalarray) #print [ 1.   7.   8.   2.   0.1  3.  15.   2.5]
numberofsmallestvaluesk = 4
#smallestvalues = originalarray.min(n=numberofsmallestvaluesk) #RM:  there's no function
originalarray.sort()
smallestvalues = originalarray[0:numberofsmallestvaluesk]
print(smallestvalues) #print [0.1 1.  2.  2.5]

#161. Write a NumPy program to create a white image of size 512x256.
#official solution
from PIL import Image
a = np.full((512, 256, 3), 255, dtype=np.uint8)
image = Image.fromarray(a, "RGB")
image.save("white.png", "PNG")

#162. Create an array (a) of shape 3, 4, 8 (K=3, J=4, I=8). tidx is an array of the same length as a.shape[1], i.e. contains J = 4 elements where each index denotes which element of K should be chosen.  Write a NumPy program to select from the first axis (K) by the indices tidx to get an array of shape (J=4, I=8) back.  #RM:  Create a random array between 0 and 10 inclusive three dimensions or three arrays each array four rows and eight columns.  Source:  https://opensourceoptions.com/blog/numpy-array-shapes-and-reshaping-arrays/.  Then extract dimension array selected, rows selected, and all the columns.
arraya = np.random.randint(0, 10, (3, 4, 8))
print(arraya)
'''
[[[6 2 2 0 6 7 6 7]
  [1 0 0 2 9 2 9 5]
  [2 3 8 1 1 0 3 4]
  [0 7 1 1 1 8 0 9]]

 [[9 0 4 4 8 9 5 5]
  [3 6 1 2 1 2 5 0]
  [9 1 2 9 6 1 1 1]
  [6 4 1 5 3 2 4 1]]

 [[4 1 4 7 4 2 5 0]
  [6 1 5 3 5 3 9 1]
  [7 4 9 6 7 7 2 7]
  [1 3 7 8 8 7 9 9]]]
'''
print(arraya.shape) #print (3, 4, 8)  RM:  three layers, four rows, eighth columns
tidx = arraya[[0, 1, 2, 1], [0, 1, 2, 3], 0:]
print(tidx) #first dimension, first row; second diemsion, second row, third dimension, third row, second dimension, fourth row.  All columns.
'''
[[6 2 2 0 6 7 6 7]
 [3 6 1 2 1 2 5 0]
 [7 4 9 6 7 7 2 7]
 [6 4 1 5 3 2 4 1]]
'''

#163. Create two arrays of six elements. Write a NumPy program to count the number of instances of a value occurring in one array on the condition of another array.  #RM:  stupid question I don't understand.
firstarraysixelements = np.array([10, -10, 10, -10, -10, 10])
secondarraysixelements = np.array([0.85, 0.45, 0.9, 0.8, 0.12, 0.6])
print(firstarraysixelements) #print [ 10 -10  10 -10 -10  10]
print(secondarraysixelements) #print [0.85 0.45 0.9  0.8  0.12 0.6 ]
resultfromofficialsolution = np.sum((firstarraysixelements == 10) & (secondarraysixelements > .5))
print(resultfromofficialsolution) #print 3

#164. Write a NumPy program to save as text a matrix which has in each row 2 float and 1 string at the end.  Sample Output:
'''
Sample Output:
string
1 0 aaa
0 1 bbb
0 1 ccc
'''
textmatrixincorrect = np.array([[1, 0, "aaa"], [0, 1, "bbb"], [0, 1, "ccc"]])
print(textmatrixincorrect)
'''
[['1' '0' 'aaa']
 ['0' '1' 'bbb']
 ['0' '1' 'ccc']]
'''
print(textmatrixincorrect.dtype) #print <U21
textmatrixdtypeobject = np.array([[1, 0, "aaa"], [0, 1, "bbb"], [0, 1, "ccc"]], dtype=object)
print(textmatrixdtypeobject)
'''
[[1 0 'aaa']
 [0 1 'bbb']
 [0 1 'ccc']]
'''
print(textmatrixdtypeobject.dtype) #print object  RM:  Lose practically all of the benefits of using numpy in the first place.  https://www.reddit.com/r/learnpython/comments/2tnldq/how_to_mix_strings_and_floats_in_a_numpy_array/
#official solution
officialsolutionmatrix = [[1, 0, 'aaa'], [0, 1, 'bbb'], [0, 1, 'ccc']]
np.savetxt('test', officialsolutionmatrix, delimiter='  ', header='string', comments='', fmt='%s')
print(np.savetxt('test', officialsolutionmatrix, delimiter='  ', header='string', comments='', fmt='%s')) #print None

#165. Write a NumPy program to merge three given NumPy arrays of same shape.  Concatenate.
onearray = np.array([[1, 2], [3, 4]])
twoarray = np.array([[11, 22], [33, 44]])
threearray = np.array([[100, 200], [300, 400]])
print(onearray)
'''
[[1 2]
 [3 4]]
'''
print(twoarray)
'''
[[11 22]
 [33 44]]
'''
print(threearray)
'''
[[100 200]
 [300 400]]
'''
combinearray = np.array([onearray, twoarray, threearray])
print(combinearray)
'''
[[[  1   2]
  [  3   4]]

 [[ 11  22]
  [ 33  44]]

 [[100 200]
  [300 400]]]
'''
concatenatearray = np.concatenate((onearray, twoarray, threearray))
print(concatenatearray)
'''
[[  1   2]
 [  3   4]
 [ 11  22]
 [ 33  44]
 [100 200]
 [300 400]]
'''
concatenatearrayone = np.concatenate((onearray, twoarray, threearray), axis=1)
print(concatenatearrayone)
'''
[[  1   2  11  22 100 200]
 [  3   4  33  44 300 400]]
'''
concatenatearraynegativeone = np.concatenate((onearray, twoarray, threearray), axis=-1)
print(concatenatearraynegativeone)
'''
[[  1   2  11  22 100 200]
 [  3   4  33  44 300 400]]
'''
concatenatearrayzero = np.concatenate((onearray, twoarray, threearray), axis=0)
print(concatenatearrayzero)
'''
[[  1   2]
 [  3   4]
 [ 11  22]
 [ 33  44]
 [100 200]
 [300 400]]
'''

#166. Write a NumPy program to combine last element with first element of two given ndarray with different shapes.
'''
Original arrays:
['PHP', 'JS', 'C++']
['Python', 'C#', 'NumPy']
After Combining:
['PHP' 'JS' 'C++Python' 'C#' 'NumPy']
'''
ndonearray = np.array(['PHP', 'JS', 'C++'])
ndtwoarray = np.array(['Python', 'C#', 'NumPy'])
print(ndonearray) #print ['PHP' 'JS' 'C++']
print(ndtwoarray) #print ['Python' 'C#' 'NumPy']
print(ndonearray[2] + ndtwoarray[0]) #print C++Python
print(ndonearray[:-1]) #print ['PHP' 'JS']
print(ndtwoarray[1:]) #print ['C#' 'NumPy']
combinearraybruteforce = np.concatenate(([ndonearray[:-1]], [[ndonearray[-1] + ndtwoarray[0]]], [ndtwoarray[1:]]), axis=1)  #RM:  Use -1 instead of 2 for the last element in case ndtwoarry has more than two elements.
print(combinearraybruteforce) #print [['PHP' 'JS' 'C++Python' 'C#' 'NumPy']]
print(type(combinearraybruteforce)) #print <class 'numpy.ndarray'>
print(combinearraybruteforce.shape) #print (1,5)
#official solution
result = np.r_[ndonearray[:-1], [ndonearray[-1] + ndtwoarray[0]], ndtwoarray[1:]]

#167. Write a NumPy program to convert a Python dictionary to a NumPy ndarray.
originaldictionary = {'column0': {'a': 1, 'b': 0.0, 'c': 0.0, 'd': 2.0}, 'column1': {'a': 3.0, 'b': 1, 'c': 0.0, 'd': -1.0}, 'column2': {'a': 4, 'b': 1, 'c': 5.0, 'd': -1.0}, 'column3': {'a': 3.0, 'b': -1.0, 'c': -1.0, 'd': -1.0}}
print(originaldictionary) #print {'column0': {'a': 1, 'b': 0.0, 'c': 0.0, 'd': 2.0}, 'column1': {'a': 3.0, 'b': 1, 'c': 0.0, 'd': -1.0}, 'column2': {'a': 4, 'b': 1, 'c': 5.0, 'd': -1.0}, 'column3': {'a': 3.0, 'b': -1.0, 'c': -1.0, 'd': -1.0}}
print(type(originaldictionary)) #print <class 'dict'>
convertdictionarytolist = list(originaldictionary.items())
converttoarray = np.array(convertdictionarytolist)
print(converttoarray)
'''
[['column0' {'a': 1, 'b': 0.0, 'c': 0.0, 'd': 2.0}]
 ['column1' {'a': 3.0, 'b': 1, 'c': 0.0, 'd': -1.0}]
 ['column2' {'a': 4, 'b': 1, 'c': 5.0, 'd': -1.0}]
 ['column3' {'a': 3.0, 'b': -1.0, 'c': -1.0, 'd': -1.0}]]
'''
print(type(converttoarray)) #print <class 'numpy.ndarray'>
for key, value in originaldictionary.items():
    print(value)
    print(type(value))
    '''
    {'a': 1, 'b': 0.0, 'c': 0.0, 'd': 2.0}
    <class 'dict'>
    {'a': 3.0, 'b': 1, 'c': 0.0, 'd': -1.0}
    <class 'dict'>
    {'a': 4, 'b': 1, 'c': 5.0, 'd': -1.0}
    <class 'dict'>
    {'a': 3.0, 'b': -1.0, 'c': -1.0, 'd': -1.0}
    <class 'dict'>
    '''
lovelist = []
for key, value in originaldictionary.items():
    for key2, value2 in value.items():
        print(key2, value2)
        lovelist.append(value2)
        '''
        a 1
        b 0.0
        c 0.0
        d 2.0
        a 3.0
        b 1
        c 0.0
        d -1.0
        a 4
        b 1
        c 5.0
        d -1.0
        a 3.0
        b -1.0
        c -1.0
        d -1.0
        '''
print(lovelist) #print [1, 0.0, 0.0, 2.0, 3.0, 1, 0.0, -1.0, 4, 1, 5.0, -1.0, 3.0, -1.0, -1.0, -1.0]
lovenumpy = np.array(lovelist)
print(lovenumpy) #print [ 1.  0.  0.  2.  3.  1.  0. -1.  4.  1.  5. -1.  3. -1. -1. -1.]
lovenumpypropershape = lovenumpy.reshape(4, 4)
print(lovenumpypropershape)
'''
[[ 1.  0.  0.  2.]
 [ 3.  1.  0. -1.]
 [ 4.  1.  5. -1.]
 [ 3. -1. -1. -1.]]
'''
#official solution
from ast import literal_eval
udict = """{"column0":{"a":1,"b":0.0,"c":0.0,"d":2.0},
   "column1":{"a":3.0,"b":1,"c":0.0,"d":-1.0},
   "column2":{"a":4,"b":1,"c":5.0,"d":-1.0},
   "column3":{"a":3.0,"b":-1.0,"c":-1.0,"d":-1.0}
  }"""
t = literal_eval(udict)
print(t)
'''
{'column0': {'a': 1, 'b': 0.0, 'c': 0.0, 'd': 2.0},
'column1': {'a': 3.0, 'b': 1, 'c': 0.0, 'd': -1.0},
'column2': {'a': 4, 'b': 1, 'c': 5.0, 'd': -1.0},
'column3': {'a': 3.0, 'b': -1.0, 'c': -1.0, 'd': -1.0}}
'''
result_nparra = np.array([[v[j] for j in ['a', 'b', 'c', 'd']] for k, v in t.items()])
print(result_nparra)
'''
[[ 1.  0.  0.  2.]
 [ 3.  1.  0. -1.]
 [ 4.  1.  5. -1.]
 [ 3. -1. -1. -1.]]
'''

#168. Write a NumPy program to convert Pandas dataframe to NumPy array with headers.
randomarrayzeroandone = np.random.random([10, 3])
print(randomarrayzeroandone)
'''
[[0.57040229 0.33884097 0.36503109]
 [0.55733304 0.10148827 0.4447412 ]
 [0.27649829 0.21411954 0.07312804]
 [0.14551202 0.79299874 0.76791595]
 [0.70152258 0.61970134 0.85688042]
 [0.80843699 0.42029969 0.80267961]
 [0.55452229 0.68742074 0.81325516]
 [0.46940317 0.83664713 0.55429078]
 [0.73475988 0.33697874 0.2761464 ]
 [0.25335262 0.68685251 0.50920046]]
'''
#https://stackoverflow.com/questions/53816008/how-to-convert-numpy-array-to-panda-dataframe
import pandas as pd
numpytopandacolumnslabels = ["column" + str(number) for number in range(3)]
numpytopandaindexslabels = ["index" + str(number) for number in range(10)]
numpytopandadataframe = pd.DataFrame(randomarrayzeroandone, columns=numpytopandacolumnslabels, index=numpytopandaindexslabels)
print(numpytopandadataframe)
'''
         column0   column1   column2
index0  0.570402  0.338841  0.365031
index1  0.557333  0.101488  0.444741
index2  0.276498  0.214120  0.073128
index3  0.145512  0.792999  0.767916
index4  0.701523  0.619701  0.856880
index5  0.808437  0.420300  0.802680
index6  0.554522  0.687421  0.813255
index7  0.469403  0.836647  0.554291
index8  0.734760  0.336979  0.276146
index9  0.253353  0.686853  0.509200
'''

#169. Write a NumPy program to get all 2D diagonals of a 3D NumPy array.
originalarray = np.arange(0, 60)
print(originalarray)
'''
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 50 51 52 53 54 55 56 57 58 59]
'''
threedimensionsfourrowsfivecolumns = originalarray.reshape(3, 4, 5)  #3 dimensions, each dimension 4 rows 5 columns
print(threedimensionsfourrowsfivecolumns)
'''
[[[ 0  1  2  3  4]
  [ 5  6  7  8  9]
  [10 11 12 13 14]
  [15 16 17 18 19]]

 [[20 21 22 23 24]
  [25 26 27 28 29]
  [30 31 32 33 34]
  [35 36 37 38 39]]

 [[40 41 42 43 44]
  [45 46 47 48 49]
  [50 51 52 53 54]
  [55 56 57 58 59]]]
'''
print(threedimensionsfourrowsfivecolumns[0])
'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
'''
twodimensiondiagonals = np.array([], dtype=np.uint8)
for dimension in range(0, 3):
    temparray = np.array([], dtype=np.uint8)
    for n in range(0, 4):
        temparray = np.append(temparray, threedimensionsfourrowsfivecolumns[dimension][n][n])
    twodimensiondiagonals = np.append(twodimensiondiagonals, temparray)
print(twodimensiondiagonals) #print [ 0  6 12 18 20 26 32 38 40 46 52 58]
print(twodimensiondiagonals.reshape(3, 4))
'''
[[ 0  6 12 18]
 [20 26 32 38]
 [40 46 52 58]]
'''
print(twodimensiondiagonals.reshape(1, 3, 4))
'''
[[[ 0  6 12 18]
  [20 26 32 38]
  [40 46 52 58]]]
'''
#official solution
npdiagonalarray = np.diagonal(threedimensionsfourrowsfivecolumns, axis1=1, axis2=2)
print(npdiagonalarray)
'''
[[ 0  6 12 18]
 [20 26 32 38]
 [40 46 52 58]]
'''

#170. Create a 2-dimensional array of size 2 x 3, composed of 4-byte integer elements. Write a NumPy program to find the number of occurrences of a sequence in the said array.  #RM:  count the number of times a sequence appears
originalarray = np.array([[1, 2, 3], [2, 1, 2]])
print(originalarray)
'''
[[1 2 3]
 [2 1 2]]
'''
#https://www.geeksforgeeks.org/find-the-number-of-occurrences-of-a-sequence-in-a-numpy-array/
find23sequence = repr(originalarray).count("2, 3")
print(find23sequence) #print 1
find23sequence = repr(originalarray).count("1, 2")
print(find23sequence) #print 2

#171. Write a NumPy program to search the index of a given array in another given array.
originalonetotwelve = np.arange(1, 13).reshape(4, 3)
print(originalonetotwelve)
'''
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
'''
search456array = np.where(originalonetotwelve == [[4, 5, 6]])
print(search456array) #print (array([1, 1, 1]), array([0, 1, 2]))
print(search456array[0]) #print [1 1 1]
#official solution
originalonetotwelve = np.arange(1, 13).reshape(4, 3)
search456array = np.array([4, 5, 6])
indexsearch456arrayall = np.where((originalonetotwelve == search456array))
print(indexsearch456arrayall) #print (array([1, 1, 1]), array([0, 1, 2]))
indexsearch456arrayall = np.where((originalonetotwelve == search456array).all)
print(indexsearch456arrayall) #print (array([0]),)
indexsearch456arrayall = np.where((originalonetotwelve == search456array).all(1))
print(indexsearch456arrayall) #print (array([1]),)
indexsearch456array = np.where((originalonetotwelve == search456array).all(1))[0]
print(indexsearch456array) #print [1]

#172. Write a NumPy program to find and store non-zero unique rows in an array after comparing each row with other row in a given matrix.  #RM:  given a matrix.  Return the rows where there is a non-zero.  There are no unique rows in the sample array.
originalarray = np.array([[1, 1, 0], [0, 0, 0], [0, 2, 3], [0, 0, 0], [0, -1, 1], [0, 0, 0]])
print(originalarray)
'''
[[ 1  1  0]
 [ 0  0  0]
 [ 0  2  3]
 [ 0  0  0]
 [ 0 -1  1]
 [ 0  0  0]]
'''
for eachoriginalarray in originalarray:
    print(eachoriginalarray)
    print(np.where(eachoriginalarray == [[0, 0, 0]]))
    print(type(np.where(eachoriginalarray == [[0, 0, 0]])))
    print(np.where(eachoriginalarray == [[0, 0, 0]])[0])
    print(np.where((eachoriginalarray == [[0, 0, 0]]).all()))
    print(np.where((eachoriginalarray == [[0, 0, 0]]).all(1)))
    print(np.where((eachoriginalarray == [[0, 0, 0]]).all(1))[0])
    print(np.where((eachoriginalarray == [[0, 0, 0]]).all(1))[0] == [0])
    print(type(np.where((eachoriginalarray == [[0, 0, 0]]).all(1))[0] == [0]))
    if np.where((eachoriginalarray == [[0, 0, 0]]).all(1))[0] == np.array([0]):
        print("love")
    print("\n")
    '''
    [1 1 0]
    (array([0]), array([2]))
    <class 'tuple'>
    [0]
    (array([], dtype=int64),)
    (array([], dtype=int64),)
    []
    []
    <class 'numpy.ndarray'>


    [0 0 0]
    (array([0, 0, 0]), array([0, 1, 2]))
    <class 'tuple'>
    [0 0 0]
    (array([0]),)
    (array([0]),)
    [0]
    [ True]
    <class 'numpy.ndarray'>
    love
    '''
for eachoriginalarray in originalarray:
    print(eachoriginalarray)
    print(np.where((eachoriginalarray == [0, 0, 0]).all()))
    print(np.where((eachoriginalarray == [0, 0, 0]).all(0)))
    print(np.where((eachoriginalarray == [0, 0, 0]).all(0))[0])
    print(np.where((eachoriginalarray == [0, 0, 0]).all(0))[0] == np.array([0]))
    if np.where((eachoriginalarray == [0, 0, 0]).all(0))[0] == np.array([0]):
        print("love2")
    print("\n")
    '''
    [1 1 0]
    (array([], dtype=int64),)
    (array([], dtype=int64),)
    []
    []


    [0 0 0]
    (array([0]),)
    (array([0]),)
    [0]
    [ True]
    love2
    '''
nonzeronumpyarray = np.array([], dtype=np.int8)
for eachoriginalarray in originalarray:
    print(eachoriginalarray)
    print(np.where((eachoriginalarray == [0, 0, 0]).all())[0] == np.array([0]))
    if not np.where((eachoriginalarray == [0, 0, 0]).all())[0] == np.array([0]):
        print("true love")
        nonzeronumpyarray = np.append(nonzeronumpyarray, eachoriginalarray)
    '''
    [1 1 0]
    []
    true love
    [0 0 0]
    [ True]
    '''
print(nonzeronumpyarray) #print [ 1  1  0  0  2  3  0 -1  1]
print(nonzeronumpyarray.reshape(3, 3))
'''
[[ 1  1  0]
 [ 0  2  3]
 [ 0 -1  1]]
'''
print("\n")
#official solution  #RM:  Convert numpy array to tuple.  Convert answer in tuple to numpy array.
nonzeronotnumpyarray = []
for indexnumber, arrayrowastuple in enumerate(map(tuple, originalarray)):
    print(indexnumber)
    print(arrayrowastuple)
    if arrayrowastuple != (0, 0, 0):
        nonzeronotnumpyarray.append(arrayrowastuple)
    '''
    0
    (1, 1, 0)
    1
    (0, 0, 0)
    2
    (0, 2, 3)
    3
    (0, 0, 0)
    4
    (0, -1, 1)
    5
    (0, 0, 0)
    '''
print(nonzeronotnumpyarray) #print [(1, 1, 0), (0, 2, 3), (0, -1, 1)]
print(np.array(nonzeronotnumpyarray))
'''
[[ 1  1  0]
 [ 0  2  3]
 [ 0 -1  1]]
'''

#173. Write a NumPy program to set zero to lower triangles along the last two axes of a three-dimensional of a given array.
triangleones = np.ones([1, 8, 8], dtype="uint8")
print(triangleones.ndim) #print 3
print(triangleones)
'''
[[[1 1 1 1 1 1 1 1]
  [1 1 1 1 1 1 1 1]
  [1 1 1 1 1 1 1 1]
  [1 1 1 1 1 1 1 1]
  [1 1 1 1 1 1 1 1]
  [1 1 1 1 1 1 1 1]
  [1 1 1 1 1 1 1 1]
  [1 1 1 1 1 1 1 1]]]
'''
#official solution
#RM:  You had the correct train of thought np.tril_indices.  np.triu is correct.   Upper triangle of an array.  Return a copy of an array with the elements below the k-th diagonal zeroed.  https://numpy.org/doc/stable/reference/generated/numpy.triu.html
triangleoneszeroes = np.triu(triangleones, k=1)
print(triangleoneszeroes)
'''
[[[0 1 1 1 1 1 1 1]
  [0 0 1 1 1 1 1 1]
  [0 0 0 1 1 1 1 1]
  [0 0 0 0 1 1 1 1]
  [0 0 0 0 0 1 1 1]
  [0 0 0 0 0 0 1 1]
  [0 0 0 0 0 0 0 1]
  [0 0 0 0 0 0 0 0]]]
'''

#174. Write a NumPy program to get the number of items, array dimensions, number of array dimensions and the memory size of each element of a given array.
samplearray = np.arange(1, 13).reshape(3, 4)
print(samplearray)
'''
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
'''
print(f"Number of elements", samplearray.size) #print Number of elements 12
print(f"Array dimensions", samplearray.shape) #print Array dimensions (3, 4)
print(f"Dimensions", samplearray.ndim) #print Dimensions 2
print(f"Memory size each element", samplearray.itemsize) #print Memory size each element 8

#175. Write a NumPy program to create an 1-D array of 20 elements. Now create a new array of shape (5, 4) from the said array, then restores the reshaped array into a 1-D array.
twentyelements = np.arange(0, 40, 2)
print(twentyelements) #print [ 0  2  4  6  8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38]
fivefournewshape = twentyelements.reshape(5, 4)
print(fivefournewshape)
'''
[[ 0  2  4  6]
 [ 8 10 12 14]
 [16 18 20 22]
 [24 26 28 30]
 [32 34 36 38]]
'''
twodimensiontoonedimension = fivefournewshape.flatten()
print(twodimensiontoonedimension) #print [ 0  2  4  6  8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38]

#176. Write a NumPy program to create an array of 4,5 shape and swap column1 with column4.  Exchange columns
originalarray = np.arange(0, 20).reshape(4, 5)
print(originalarray)
'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
'''
originalarray[:, [3, 0]] = originalarray[:, [0, 3]]
print(originalarray)
'''
[[ 3  1  2  0  4]
 [ 8  6  7  5  9]
 [13 11 12 10 14]
 [18 16 17 15 19]]
'''
#bonus exchange rows 2 and 4
originalarray = np.arange(0, 20).reshape(4, 5)
originalarray[[3, 1], :] = originalarray[[1, 3], :]
print(originalarray)
'''
[[ 0  1  2  3  4]
 [15 16 17 18 19]
 [10 11 12 13 14]
 [ 5  6  7  8  9]]
'''

#177. Write a NumPy program to create an array of 4,5 shape and to reverse the rows of the said array. After reversing 1st row will be 4th and 4th will be 1st, 2nd row will be 3rd row and 3rd row will be 2nd row.
originalarray = np.arange(0, 20).reshape(4, 5)
print(originalarray)
'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
'''
originalarray[::-1] = originalarray[::1]
print(originalarray)
'''
[[15 16 17 18 19]
 [10 11 12 13 14]
 [ 5  6  7  8  9]
 [ 0  1  2  3  4]]
'''

#178. Write a NumPy program to replace all the nan (missing values) of a given array with the mean of another array.
arraynonan = np.arange(0, 20).reshape(4, 5)
print(arraynonan)
'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
'''
arrayyesnan = np.array([[1, 2, np.nan], [4, 5, 6], [np.nan, 7, np.nan]], dtype=float) #DeprecationWarning: `np.float` is a deprecated alias for the builtin `float`.  arrayyesnan = np.array([[1, 2, np.nan], [4, 5, 6]], dtype=np.float)
print(arrayyesnan)
'''
[[ 1.  2. nan]
 [ 4.  5.  6.]
 [nan  7. nan]]
'''
print(np.mean(arraynonan)) #print 9.5
arrayyesnan[arrayyesnan == np.nan] = np.mean(arraynonan) #RM:  didn't work
print(arrayyesnan)
'''
[[ 1.  2. nan]
 [ 4.  5.  6.]
 [nan  7. nan]]
'''
arraynantozero = np.nan_to_num(arrayyesnan)
print(arraynantozero)
'''
[[1. 2. 0.]
 [4. 5. 6.]
 [0. 7. 0.]]
'''
arraynantozero[arraynantozero == 0] = np.mean(arraynonan)
print(arraynantozero)
'''
[[1.  2.  9.5]
 [4.  5.  6. ]
 [9.5 7.  9.5]]
'''
#official solution with my variables
arrayyesnan[np.isnan(arrayyesnan)] = np.mean(arraynonan)
print(arrayyesnan)
'''
[[1.  2.  9.5]
 [4.  5.  6. ]
 [9.5 7.  9.5]]
'''

#179. Write a NumPy program to fetch all items from a given array of 4,5 shape which are either greater than 6 and a multiple of 3.
originalarray = np.arange(0, 20).reshape(4, 5)
print(originalarray)
'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
'''
print(originalarray[(originalarray % 3 == 0) & (originalarray > 6)]) #print [ 9 12 15 18]  #RM:  && is invalid syntax

#180. Write a NumPy program to check whether the dimensions of two given arrays are same or not.
array1 = np.arange(0, 20).reshape(4, 5)
array2 = np.arange(0, 20).reshape(4, 5)
print(np.array_equal(array1, array2)) #print True

#181. Write a NumPy program to place a specified element in specified time randomly in a specified 2D array.
zeros4x4 = np.zeros([4, 4], dtype=float)
print(zeros4x4)
'''
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
'''
zeros4x4rows, zeros4x4columns = zeros4x4.shape
zeros4x4elements = zeros4x4.size
print(zeros4x4rows) #print 4
print(zeros4x4columns) #print 4
print(zeros4x4elements) #print 16
randomhowmnayreplace = np.random.randint(0, zeros4x4elements)
for counter in range(0, randomhowmnayreplace):
    randomrow = np.random.randint(0, zeros4x4rows - 1)
    randomcolumn = np.random.randint(0, zeros4x4columns - 1)
    zeros4x4[randomrow, randomcolumn] = 10
    counter += 1
print(zeros4x4)
'''
[[10.  0. 10.  0.]
 [10.  0.  0.  0.]
 [10.  0.  0.  0.]
 [ 0.  0.  0.  0.]]
'''

#182. Write a NumPy program to subtract the mean of each row of a given matrix.
randomintegers = np.random.randint(1, 9, size=(5, 10))
print(randomintegers)
'''
[[8 1 1 4 6 5 1 1 4 8]
 [5 7 5 1 7 8 6 6 2 7]
 [2 8 2 8 7 8 1 2 4 8]
 [3 5 8 8 6 6 5 6 1 1]
 [4 1 3 8 7 8 7 5 5 4]]
'''
randomintegersmean = np.mean(randomintegers)
print(randomintegersmean) #print 4.88
randomintegersmeanuptodown = np.mean(randomintegers, axis=0)
print(randomintegersmeanuptodown) #print [4.4 4.4 3.8 5.8 6.6 7.  4.  4.  3.2 5.6]
randomintegersmeanlefttoright = np.mean(randomintegers, axis=1)
print(randomintegersmeanlefttoright) #print [3.9 5.4 5.  4.9 5.2]
randomintegersmeanlefttorightsubtracteachrow = np.mean(randomintegers, axis=1, keepdims=True) #keepdims=True If this is set to True, the axes which are reduced are left in the result as dimensions with size one.  https://numpy.org/doc/stable/reference/generated/numpy.mean.html
print(randomintegersmeanlefttorightsubtracteachrow)
'''
[[3.9]
 [5.4]
 [5. ]
 [4.9]
 [5.2]]
 '''
answer = randomintegers - randomintegersmeanlefttorightsubtracteachrow
print(answer)
'''
[[ 4.1 -2.9 -2.9  0.1  2.1  1.1 -2.9 -2.9  0.1  4.1]
 [-0.4  1.6 -0.4 -4.4  1.6  2.6  0.6  0.6 -3.4  1.6]
 [-3.   3.  -3.   3.   2.   3.  -4.  -3.  -1.   3. ]
 [-1.9  0.1  3.1  3.1  1.1  1.1  0.1  1.1 -3.9 -3.9]
 [-1.2 -4.2 -2.2  2.8  1.8  2.8  1.8 -0.2 -0.2 -1.2]]
'''

#183. Write a NumPy program to test whether a given 2D array has null columns or not.
randomintegers = np.random.randint(0, 3, size=(5, 10))
print(randomintegers)
'''
[[2 0 1 0 1 0 0 0 2 0]
 [1 1 0 0 2 2 0 0 2 2]
 [0 0 1 1 2 0 0 1 0 2]
 [1 0 2 2 0 2 1 2 2 0]
 [1 0 0 2 2 2 1 1 0 0]]
'''
print(np.isnan(randomintegers))
'''
[[False False False False False False False False False False]
 [False False False False False False False False False False]
 [False False False False False False False False False False]
 [False False False False False False False False False False]
 [False False False False False False False False False False]]
'''
print(np.isnan(randomintegers).any()) #print False

#184. Write a NumPy program to create an array using generator function that generates 15 integers.
fifteenintegers = np.arange(0, 15)
print(fifteenintegers) #print [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
#question asked to create a function to generate 15 integers.  Official solution with my edits.
def generatefunction(numberofintegers):
    for n in range(0, numberofintegers):
        yield n


x = 15
fifteenintegers = np.fromiter(generatefunction(x), dtype=int, count=-1) #fromiter function creates a one dimensional array from an iterable object.  https://numpy.org/doc/stable/reference/generated/numpy.fromiter.html
print(fifteenintegers) #print [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

#185. Write a NumPy program to create a new vector with 2 consecutive 0 between two values of a given vector.
initialarray = np.arange(1, 9, dtype=int)
print(initialarray) #print [1 2 3 4 5 6 7 8]
initialarrayinsertzerossecondindex = np.insert(initialarray, 2, 0)
print(initialarrayinsertzerossecondindex) #print [1 2 0 3 4 5 6 7 8]
initialarrayinsertzeroseverysecondindex = np.insert(initialarray, (1, 2, 3), [0, 0, 0], axis=None)
print(initialarrayinsertzeroseverysecondindex) #print [1 0 2 0 3 0 4 5 6 7 8]
# initialarrayinsertzeroseverysecondindex2 = np.insert(initialarray, (1, 2, 3), [[0, 0], [0, 0]], axis=None)
# print(initialarrayinsertzeroseverysecondindex2) #print ValueError: shape mismatch: value array of shape (2,2) could not be broadcast to indexing result of shape (3,)
#official solution
initialarray = np.arange(1, 9, dtype=int)
print(initialarray) #print [1 2 3 4 5 6 7 8]
consecutivenumber = 2
zerosarray = np.zeros(np.size(initialarray) + np.size(initialarray) - 1)
print(zerosarray) #print [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
initialarrayinsertzeroseverysecondindex = np.zeros(np.size(initialarray) + (np.size(initialarray) - 1) * consecutivenumber)
print(initialarrayinsertzeroseverysecondindex) #print [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
initialarrayinsertzeroseverysecondindex[::consecutivenumber + 1] = initialarray
print(initialarrayinsertzeroseverysecondindex) #print [1. 0. 0. 2. 0. 0. 3. 0. 0. 4. 0. 0. 5. 0. 0. 6. 0. 0. 7. 0. 0. 8.]

#186. Write a NumPy program to multiply an array of dimension (2,2,3) by an array with dimensions (2,2).  #RM:  Broadcasting.  The term broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations. Subject to certain constraints, the smaller array is “broadcast” across the larger array so that they have compatible shapes.  https://numpy.org/doc/stable/user/basics.broadcasting.html
ones = np.ones([2, 2, 3])
print(ones)
'''
[[[1. 1. 1.]
  [1. 1. 1.]]

 [[1. 1. 1.]
  [1. 1. 1.]]]
'''
onesfirst = np.ones([2, 2])
print(onesfirst)
'''
[[1. 1.]
 [1. 1.]]
'''
onesnowthrees = onesfirst * 3
print(onesnowthrees)
'''
[[3. 3.]
 [3. 3.]]
'''
print(onesnowthrees[0:2, 0:1])
'''
[[3.]
 [3.]]
'''
print(ones * onesnowthrees[0:2, 0:1])  #I used the onesnowthrees two rows and one column array to multiply the ones two rows and three columns array by three.  Look at print(onesnowthrees[0:2, 0:1]).
'''
[[[3. 3. 3.]
  [3. 3. 3.]]

 [[3. 3. 3.]
  [3. 3. 3.]]]
'''
print(onesnowthrees[0:2, 0:1] * ones)
'''
[[[3. 3. 3.]
  [3. 3. 3.]]

 [[3. 3. 3.]
  [3. 3. 3.]]]
'''
#official solution
newarray = ones * onesnowthrees[:, :, None]
print(newarray)
'''
[[[3. 3. 3.]
  [3. 3. 3.]]

 [[3. 3. 3.]
  [3. 3. 3.]]]
'''

#187. Write a NumPy program to convert a given vector of integers to a matrix of binary representation.  #RM:  answer is a new numpy array for which each row is the binary representation of each number in original array
originalarray = np.array([0, 1, 3, 5, 7, 9, 11, 13, 15])
print(originalarray) #print [ 0  1  3  5  7  9 11 13 15]
binaryrepresentation = np.binary_repr(15, width=8)
print(binaryrepresentation) #print 00001111
binaryrepresentationarray = np.array([])
print(binaryrepresentationarray) #print []
print(type(binaryrepresentationarray)) #print []
for x in range(0, np.size(originalarray)):
    binaryrepresentationarray = np.append(binaryrepresentationarray, np.binary_repr(originalarray[x], width=8))
print(binaryrepresentationarray) #print ['00000000' '00000001' '00000011' '00000101' '00000111' '00001001' '00001011' '00001101' '00001111']
#official solution
binnums = ((originalarray.reshape(-1, 1) & (2**np.arange(8))) != 0).astype(int)
print(binnums)
'''
[[0 0 0 0 0 0 0 0]
 [1 0 0 0 0 0 0 0]
 [1 1 0 0 0 0 0 0]
 [1 0 1 0 0 0 0 0]
 [1 1 1 0 0 0 0 0]
 [1 0 0 1 0 0 0 0]
 [1 1 0 1 0 0 0 0]
 [1 0 1 1 0 0 0 0]
 [1 1 1 1 0 0 0 0]]
'''

#188. Write a NumPy program to extract rows with unequal values (e.g. [1,1,2]) from 10x3 matrix.  #RM:  In other words, remove rows which has the same number [0 0 0] [1 1 1] [2 2 2] [3 3 3]. #RM:  https://numpy.org/doc/stable/reference/generated/numpy.logical_and.html.
#official solution
originalarray = np.random.randint(0, 4, size=(10, 3))
print(originalarray)
'''
[[2 2 0]
 [1 0 2]
 [3 2 3]
 [3 2 0]
 [1 2 0]
 [1 2 0]
 [1 0 3]
 [1 1 0]
 [1 1 0]
 [2 2 2]]
'''
equalvalues = np.logical_and.reduce(originalarray[:, 1:] == originalarray[:, :-1], axis=1)
print(equalvalues) #print [False False False False False False False False False  True]
answer = originalarray[~equalvalues]
print(answer)
'''
[[2 2 0]
 [1 0 2]
 [3 2 3]
 [3 2 0]
 [1 2 0]
 [1 2 0]
 [1 0 3]
 [1 1 0]
 [1 1 0]]
'''

#189. Write a NumPy program to find rows of a given array of shape (8,3) that contain elements of each row of another given array of shape (2,2).  #RM:  official solution is given array shape (6,4) and another given array shape (2,3).
#official solution
givenarray = np.random.randint(0, 6, size=(6, 4))
anothergivenarray = np.random.randint(0, 6, size=(2, 3))
print(givenarray)
'''
[[0 4 1 0]
 [2 1 5 0]
 [5 3 0 4]
 [0 2 3 2]
 [4 4 5 0]
 [2 2 5 5]]
'''
print(anothergivenarray)
'''
[[5 3 4]
 [5 5 5]]
'''
temp = (givenarray[..., np.newaxis, np.newaxis] == anothergivenarray)
#print(temp) #RM:  prints a numpy array of True and False multiple dimensions
rows = (temp.sum(axis=(1, 2, 3)) >= anothergivenarray.shape[1]).nonzero()[0]
print(rows) #print [1 2 4 5]

