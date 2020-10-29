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