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