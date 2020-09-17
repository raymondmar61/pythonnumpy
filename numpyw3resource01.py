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
