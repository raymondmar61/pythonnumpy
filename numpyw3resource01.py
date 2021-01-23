#https://www.w3resource.com/python-exercises/
#https://www.w3resource.com/python-exercises/numpy/index.php
#https://www.w3resource.com/python-exercises/numpy/basic/index.php

import numpy as np

#https://www.w3resource.com/python-exercises/numpy/basic/index.php
#1.Write a NumPy program to get the numpy version and show numpy build configuration.
#Source: https://appdividend.com/2020/05/05/how-to-check-numpy-version-on-mac-linux-and-windows/
print(np.__version__)
#commmand line type python3 -c "import numpy; print(numpy.__version__)".  Also pip3 show numpy.  pip3 list shows all modules and version numbers.

#2. Write a NumPy program to  get help on the add function.
print(help(np.add))
#official solution
print(np.info(np.add))

#3. Write a NumPy program to test whether none of the elements of a given array is zero.
#np.all() Test whether all array elements along a given axis evaluate to True.  0 is False; otherwise True.
nozeroes = np.array([1, 2, 3, 4, 5])
print(nozeroes) #print [1 2 3 4 5]
checknozeroes = nozeroes == 0
print(checknozeroes) #print [False False False False False]
#official solution
yeszeroes = np.array([0, 1, 2, 3, 4])
print(np.all(yeszeroes)) #print False
print(np.all(nozeroes)) #print True

#4. Write a NumPy program to test whether any of the elements of a given array is non-zero.
#np.all() Test whether all array elements along a given axis evaluate to True.  0 is False; otherwise True.
nozeroes = np.array([1, 2, 3, 4, 5])
print(nozeroes) #print [1 2 3 4 5]
checknozeroes = nozeroes != 0
print(checknozeroes) #print [ True  True  True  True  True]
#official solution
yeszeroes = np.array([0, 1, 2, 3, 4])
print(np.all(yeszeroes)) #print False
print(np.all(nozeroes)) #print True

#5. Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a Number).
#Source https://numpy.org/doc/stable/reference/generated/numpy.isfinite.html
nozeroes = np.array([1, 2, 3, 4, 5])
print(np.isfinite(nozeroes)) #print [ True  True  True  True  True]
#official solution
a = np.array([1, 0, np.nan, np.inf])  #np.nan is a floating point Not A Number.  np.inf is a floating point positive infinity.
print(np.isfinite(a)) #print [ True  True False False]

#6. Write a NumPy program to test element-wise for positive or negative infinity
#Source https://numpy.org/doc/stable/reference/generated/numpy.isinf.html
a = np.array([1, 0, np.nan, np.inf])  #np.nan is a floating point Not A Number.  np.inf is a floating point positive infinity.
#isinf() tests element-wise for positive or negative infinity; returns True for positive or negative infinity, False otherwise.
print(np.isinf(a)) #print [False False False  True]

#7. Write a NumPy program to test element-wise for NaN of a given array.
#Source https://numpy.org/doc/stable/reference/generated/numpy.isnan.html
a = np.array([1, 0, np.nan, np.inf])  #np.nan is a floating point Not A Number.  np.inf is a floating point positive infinity.
print(np.isnan(a)) #print [False False  True False]

#8. Write a NumPy program to test element-wise for complex number, real number of a given array. Also test whether a given number is a scalar type or not.
a = np.array([100, -999, 0, 1, np.nan, np.inf, 45 + 2j, 45 + 2j])
print(np.iscomplex(a)) #print [False False False False False False  True  True]
print(a.imag) #print [0. 0. 0. 0. 0. 0. 2. 2.]
print(np.isreal(a)) #print [ True  True  True  True  True  True False False]
print(a.real) #print [ 100. -999.    0.    1.   nan   inf   45.   45.]
print(np.isscalar(a)) #print False
print(np.isscalar((3.1))) #print True
print(np.isscalar([3.1])) #print False

#9. Write a NumPy program to test whether two arrays are element-wise equal within a tolerance.
#Source https://numpy.org/doc/stable/reference/generated/numpy.isclose.html, https://numpy.org/doc/stable/reference/generated/numpy.allclose.html
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.isclose(a, b)) #print [False False False]
a = np.array([1, 1, 1])
b = np.array([2, 2, 2])
print(np.isclose(a, b)) #print [False False False]
a = np.array([1, 1, 1])
b = np.array([1.001, 1.001, 1.001])
print(np.isclose(a, b)) #print [False False False]
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.allclose(a, b)) #print False
a = np.array([1, 1, 1])
b = np.array([2, 2, 2])
print(np.allclose(a, b)) #print False
a = np.array([1, 1, 1])
b = np.array([1.001, 1.001, 1.001])
print(np.allclose(a, b)) #print False
#official solution
print(np.allclose([1e10, 1e-7], [1.00001e10, 1e-8])) #print False
print(np.allclose([1e10, 1e-8], [1.00001e10, 1e-9])) #print True
print(np.allclose([1e10, 1e-8], [1.0001e10, 1e-9])) #print False
print(np.allclose([1.0, np.nan], [1.0, np.nan])) #print False
print(np.allclose([1.0, np.nan], [1.0, np.nan], equal_nan=True)) #print True

#10. Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays.
a = np.array([1, 6, 90, -4, 2468, 5209, 10002])
b = np.array([2, 7, 89, -5, 2468, 9999, 10001])
print(len(a)) #print 6
for eachelement in range(0, len(a)):
  print(a[eachelement] > b[eachelement]) #print False\n False\n True\n True\n False\n False\n True
truefalsearraygreater = a > b
print(truefalsearraygreater) #print [False False  True  True False False  True]
truefalsearraygreaterequal = a >= b
print(truefalsearraygreaterequal) #print [False False  True  True  True False  True]
truefalsearrayless = a < b
print(truefalsearrayless) #print [ True  True False False False  True False]
truefalsearraylessequal = a <= b
print(truefalsearraylessequal) #print [ True  True False False  True  True False]
#official solution
print(np.greater(a, b)) #print [False False  True  True False False  True]
print(np.greater_equal(a, b)) #print [False False  True  True  True False  True]
print(np.less(a, b)) #print [ True  True False False False  True False]
print(np.less_equal(a, b)) #print [ True  True False False  True  True False]

#11. Write a NumPy program to create an element-wise comparison (equal, equal within a tolerance) of two given arrays.
a = np.array([1, 6, 90, -4, 2468, 5209, 10002])
b = np.array([2, 7, 89, -5, 2468, 9999, 10001])
equalarrays = a == b
print(equalarrays) #print [False False False False  True False False]
print(np.equal(a, b)) #print [False False False False  True False False]
print(np.allclose(a, b)) #print False.  Comparison equal within a tolerance.

#12. Write a NumPy program to create an array with the values 1, 7, 13, 105 and determine the [total] size of the memory occupied by the array.
thesevalues = np.array([1, 7, 13, 105])
print(thesevalues) #print [  1   7  13 105]
print(thesevalues.itemsize * thesevalues.size) #print 32

#13. Write a NumPy program to create an array of 10 zeros,10 ones, 10 fives.
zerosarray = np.zeros((2, 5))
print(zerosarray)
'''
[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]
'''
onesarray = np.ones((2, 5))
print(onesarray)
'''
[[1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]
'''
number5 = np.full((2, 5), 5, dtype="int16")
print(number5)
'''
[[5 5 5 5 5]
 [5 5 5 5 5]]
'''
officialsolution5 = np.ones((2, 5)) * 5
print(officialsolution5)
'''
[[5. 5. 5. 5. 5.]
 [5. 5. 5. 5. 5.]]
'''

#14. Write a NumPy program to create an array of the integers from 30 to70.
thirtyseventy = np.arange(30, 71)
print(thirtyseventy) #print [30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70]

#15. Write a NumPy program to create an array of all the even integers from 30 to 70.
thirtyseventyeven = np.arange(30, 71, 2)
print(thirtyseventyeven) #print [30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70]

#16. Write a NumPy program to create a 3x3 identity matrix.  #RM:  An identify matrix is always a square with a diagonal 1 in lament terms
identifyarray = np.identity(3, dtype="int8")
print(identifyarray)
'''
[[1 0 0]
 [0 1 0]
 [0 0 1]]
'''

#17. Write a NumPy program to generate a random number between 0 and 1.
numpyrandom = np.random.random()
print(numpyrandom) #print 0.5176968454082396

#18. Write a NumPy program to generate an array of 15 random numbers from a standard normal distribution.  #RM:  mean is zero.  Standard deviation is one.
numpyrandomstandardnormtaldistribution = np.random.standard_normal(size=15)
print(numpyrandomstandardnormtaldistribution)
'''
[ 0.83499974  0.13930662 -0.04351699 -1.2448165   0.94294667 -0.11478617
  0.64405926 -0.20838049 -0.5876138  -0.35229884 -0.04755612  1.22032174
  1.11479368  0.69353702  0.20635629]
'''

#19. Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values except the first and last.
vector15 = np.arange(15, 55)  #RM:  no need for (15,56) because don't want the last number 55
vector15 = vector15[1:]
print(vector15) #print [16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54]

#20. Write a NumPy program to create a 3X4 array using and iterate over it.
numbers12 = np.arange(1, 13).reshape(3, 4)
print(numbers12)
'''
[[ 1  2  3  4]
[ 5  6  7  8]
[ 9 10 11 12]]
'''
for eachnumbers12 in numbers12:
  print(eachnumbers12)
  '''
    [1 2 3 4]
    [5 6 7 8]
    [ 9 10 11 12]
    '''
for eachnumbers12 in numbers12.flat:
  print(eachnumbers12) #print 1\n 2\n 3\n 4\n 5\n 6\n 7\n 8\n 9\n 10\n 11\n 12
numbers12flatten = numbers12.flatten()
for eachnumbers12flatten in numbers12flatten:
  print(eachnumbers12flatten) #print 1\n 2\n 3\n 4\n 5\n 6\n 7\n 8\n 9\n 10\n 11\n 12
for x in np.nditer(numbers12):
  print(x, end=",") #print 1,2,3,4,5,6,7,8,9,10,11,12,

#21. Write a NumPy program to create a vector of length 10 with values evenly distributed between 5 and 50.
evendistribution550 = np.linspace(5, 50, 10, dtype="int8")
print(evendistribution550) #print [ 5 10 15 20 25 30 35 40 45 50]

#22. Write a NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15.
changesign915 = np.arange(0, 21)
print(changesign915) #print [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]
changesign915final = np.concatenate((changesign915[0:9], np.negative((changesign915)[9:16]), changesign915[16:]), axis=0)
print(changesign915final) #print [  0   1   2   3   4   5   6   7   8  -9 -10 -11 -12 -13 -14 -15  16  17  18  19  20]
#officialsolution
changesign915 = np.arange(0, 21)
print(changesign915) #print [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]
changesign915[(changesign915 >= 9) & (changesign915 <= 15)] *= -1
print(changesign915) #print [  0   1   2   3   4   5   6   7   8  -9 -10 -11 -12 -13 -14 -15  16  17  18  19  20]

import numpy as np

#23. Write a NumPy program to create a vector of length 5 filled with arbitrary integers from 0 to 10.
lengthfive = np.random.randint(0, 10, size=(1, 5))
print(lengthfive) #print [[2 9 6 8 6]]
lengthfive = np.random.randint(0, 10, 5)
print(lengthfive) #print [4 7 6 5 8]

#24. Write a NumPy program to multiply the values of two given vectors.
multiplyone = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
multiplytwo = np.array([10, 11, 12])
print(np.multiply(multiplyone, multiplytwo))
'''
[[ 0 11 24]
 [30 44 60]
 [60 77 96]]
'''
result = multiplyone * multiplytwo
print(result)
'''
[[ 0 11 24]
 [30 44 60]
 [60 77 96]]
'''

#25. Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.
threebyfour = np.arange(10, 22).reshape(3, 4)
print(threebyfour)
'''
[[10 11 12 13]
 [14 15 16 17]
 [18 19 20 21]]
'''

#26. Write a NumPy program to find the number of rows and columns of a given matrix.
threebyfour = np.arange(10, 22).reshape(3, 4)
print(threebyfour.shape) #print (3, 4)

#27. Write a NumPy program to create a 3x3 identity matrix, i.e. diagonal elements are 1, the rest are 0.  #RM:  #An identity matrix is always a square with a diagonal 1 in lament terms.
identitymatrix = np.identity(3, dtype="int8")
print(identitymatrix)
'''
[[1 0 0]
 [0 1 0]
 [0 0 1]]
'''

#28. Write a NumPy program to create a 10x10 matrix, in which the elements on the borders will be equal to 1, and inside 0.
bordersones = np.zeros([10, 10], dtype="int8")
bordersones[0:1, ] = 1
bordersones[9:, ] = 1
bordersones[:, 0] = 1
bordersones[:, 9] = 1
print(bordersones)
'''
[[1 1 1 1 1 1 1 1 1 1]
 [1 0 0 0 0 0 0 0 0 1]
 [1 0 0 0 0 0 0 0 0 1]
 [1 0 0 0 0 0 0 0 0 1]
 [1 0 0 0 0 0 0 0 0 1]
 [1 0 0 0 0 0 0 0 0 1]
 [1 0 0 0 0 0 0 0 0 1]
 [1 0 0 0 0 0 0 0 0 1]
 [1 0 0 0 0 0 0 0 0 1]
 [1 1 1 1 1 1 1 1 1 1]]
'''
#official solution
bordersones = np.ones([10, 10], dtype="int8")
bordersones[1:-1, 1:-1] = 0

#29. Write a NumPy program to create a 5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4, 5.
fivesquarezero = np.zeros([5, 5], dtype="int8")
for x in range(0, 5):
  fivesquarezero[x, x] = x + 1
print(fivesquarezero)
'''
[[1 0 0 0 0]
 [0 2 0 0 0]
 [0 0 3 0 0]
 [0 0 0 4 0]
 [0 0 0 0 5]]
'''
#official solution
diagnpfunction = np.diag([1, 2, 3, 4, 5])
print(diagnpfunction)
'''
[[1 0 0 0 0]
 [0 2 0 0 0]
 [0 0 3 0 0]
 [0 0 0 4 0]
 [0 0 0 0 5]]
'''

#30. Write a NumPy program to create a 4x4 matrix in which 0 and 1 are staggered, with zeros on the main diagonal.
zerosmaindiagonal = np.random.randint(0, 2, size=(4, 4))
for x in range(0, 4):
  zerosmaindiagonal[x, x] = 0
print(zerosmaindiagonal)
'''
[[0 0 1 1]
 [1 0 0 1]
 [0 0 0 0]
 [0 1 0 0]]
'''
#official solution
x = np.zeros((4, 4))
x[::2, 1::2] = 1
x[1::2, ::2] = 1
print(x)
'''
[[ 0.  1.  0.  1.]
 [ 1.  0.  1.  0.]
 [ 0.  1.  0.  1.]
 [ 1.  0.  1.  0.]]
'''

#31. Write a NumPy program to create a 3x3x3 array filled with arbitrary values.
randomthreebythreebythree = np.random.randint(0, 9, size=(3, 3, 3))
print(randomthreebythreebythree)
'''
[[[1 2 0]
  [7 3 8]
  [5 6 3]]

 [[4 1 1]
  [1 1 5]
  [1 0 3]]

 [[4 5 8]
  [1 7 6]
  [2 0 7]]]
'''
#official solution
randomfunctionthreebythreebythree = np.random.random([3, 3, 3])
print(randomfunctionthreebythreebythree)
'''
[[[0.03563651 0.07876963 0.44267745]
  [0.20929066 0.67221495 0.64223085]
  [0.89920173 0.66818071 0.69738417]]

 [[0.99229119 0.56717686 0.19997   ]
  [0.63064619 0.18210131 0.67718461]
  [0.91287784 0.26657287 0.75128358]]

 [[0.54943148 0.24040582 0.66841699]
  [0.75833621 0.98582855 0.71226856]
  [0.80292768 0.34143496 0.05404068]]]
'''

#32. Write a NumPy program to compute sum of all elements, sum of each column and sum of each row of a given array.
onedigitarray = np.random.randint(0, 9, size=(3, 4))
print(onedigitarray)
'''
[[7 4 5 7]
 [2 2 4 0]
 [6 2 6 5]]
'''
sumall = onedigitarray.sum()
print(sumall) #print 50
sumbyrow = onedigitarray.sum(axis=1)
print(sumbyrow) #print [23  8 19]
sumbycolumn = onedigitarray.sum(axis=0)
print(sumbycolumn) #print [15  8 15 12]

#33. Write a NumPy program to compute the inner product of two given vectors.  #RM:  dot matrix or dot product
fourarray = np.array([[1, 2], [3, 4]])
eightarray = np.array([[5, 6], [7, 8]])
dotmatrix = fourarray.dot(eightarray)
print(dotmatrix)
'''
[[19 22]  (1*5)+(2*7); (1*6)+(2*8)
 [43 50]]  (3*5)+(4*7); (3*6)+(4*8)
'''

#34. Write a NumPy program to add a vector to each row of a given matrix.
mainarray = np.array([[0, 0, 0], [10, 10, 10], [20, 20, 20], [30, 30, 30]])
print(mainarray)
'''
[[ 0  0  0]
 [10 10 10]
 [20 20 20]
 [30 30 30]]
'''
theaddarray = np.array([[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]])
print(theaddarray)
'''
[[0 1 2]
 [0 1 2]
 [0 1 2]
 [0 1 2]]
'''
print(mainarray + theaddarray)
'''
[[ 0  1  2]
 [10 11 12]
 [20 21 22]
 [30 31 32]]
'''
#https://numpy.org/doc/stable/reference/generated/numpy.empty_like.html
whatisempty_like = np.empty_like(mainarray + theaddarray) #Return a new array with the same shape and type as a given array.
print(whatisempty_like)
'''
[[140680753409328        41397456 140680753630488]
 [140680753656240 140680753630432 140680753656176]
 [140680753656368 140680753656432 140680503476720]
 [140680503477056 140680503477224 140680730845288]]
'''
whatisempty_like = np.ones_like(mainarray + theaddarray) #Return a new array with the same shape and type as a given array.
print(whatisempty_like)
'''
[[1 1 1]
 [1 1 1]
 [1 1 1]
 [1 1 1]]
'''
whatisempty_like = np.zeros_like(mainarray + theaddarray) #Return a new array with the same shape and type as a given array.
print(whatisempty_like)
'''
[[0 0 0]
 [0 0 0]
 [0 0 0]
 [0 0 0]]
'''

#35. Write a NumPy program to save a given array to a binary file.
savethearray = np.random.randint(0, 9, 6)
print(savethearray) #print [3 2 3 8 2 7]
np.save("tempnumpyarray.txt", savethearray) #saves file as tempnumpyarray.txt.npy

#36. Write a NumPy program to save two given arrays into a single file in compressed format (.npz format) and load it.
#Source:  https://numpy.org/devdocs/reference/generated/numpy.savez_compressed.html
givenarrayone = np.array([1, 2, 3])
givenarraytwo = np.array([4, 5, 6])
np.savez_compressed("/home/mar/python/savednumpyfilename.npz", filename1=givenarrayone, filename2=givenarraytwo)
loadcompressednumpy = np.load("/home/mar/python/savednumpyfilename.npz")
print(np.array_equal(givenarrayone, loadcompressednumpy["filename1"])) #print True
print(np.array_equal(givenarrayone, loadcompressednumpy["filename2"])) #print False
print(np.array_equal(givenarraytwo, loadcompressednumpy["filename2"])) #print True
with np.load("/home/mar/python/savednumpyfilename.npz") as loadnumpydata:
  printgivenarrayone = loadnumpydata["filename1"]
  print(printgivenarrayone) #print [1 2 3]
  printgivenarraytwo = loadnumpydata["filename2"]
  print(printgivenarraytwo) #print [4 5 6]

#37. Write a NumPy program to save a given array to a text file and load it.
#Source:  https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html, https://www.geeksforgeeks.org/how-to-save-a-numpy-array-to-a-text-file/
arraytextfile = np.array([[100, 200, 300], [345, 678, 901]])
np.savetxt("/home/mar/python/savetextarray.txt", arraytextfile)
displaynumpytext = np.loadtxt("/home/mar/python/savetextarray.txt")
print(displaynumpytext) #print [[100. 200. 300.]\n [345. 678. 901.]]

#38. Write a NumPy program to convert a given array into bytes, and load it as array.
#Source:  https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tobytes.html
arraytobytes = np.array([[0, 1], [2, 3]])
arraytobytes.tobytes()
print(arraytobytes.tobytes("C"))  #C language print b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00'
print(arraytobytes.tobytes("F"))  #Fortran language print b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00'

#39. Write a NumPy program to convert a given array into a list and then convert it into a list again.
givenarray = np.array([2, 3, 4, 5, 6])
print(givenarray) #print [2 3 4 5 6]
print(list(givenarray)) #print [2, 3, 4, 5, 6]
numpyfunctiontolist = givenarray.tolist()
print(numpyfunctiontolist) #print [2, 3, 4, 5, 6]
print(type(numpyfunctiontolist)) #print < class 'list' >

#40. Write a NumPy program to compute the x and y coordinates for points on a sine curve and plot the points using matplotlib.

#41. Write a NumPy program to convert numpy dtypes to native python types.
#Source:  https://stackoverflow.com/questions/9452775/converting-numpy-dtypes-to-native-python-types
numpynumber = np.array([5, 7, 9])
print(numpynumber) #print [5 7 9]
numpyfloat = np.float32([5, 7, 9])
print(numpyfloat) #print [5. 7. 9.]
print(np.float64(numpyfloat)) #print [5. 7. 9.]
#print(type(np.float64(numpyfloat).item())) #print ValueError: can only convert an array of size 1 to a Python scalar
print(type(np.float64(0).item())) #print <class 'float'>
print(np.uint32(numpyfloat)) #print [5 7 9]
print(type(np.uint32(0).item())) #print <class 'int'>
print(np.cfloat(numpyfloat)) #print [5.+0.j 7.+0.j 9.+0.j]  RM:  complex
print(type(np.cfloat(0).item())) #print <class 'complex'>
