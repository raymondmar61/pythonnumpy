#Python Data Analytics  And Visualization by Phuong Vo.T.H Chapter 02 NumPy Arrays And Vectorized Computation
import numpy as np
eiffeltowerlocation = np.array([48.858598, 2.294485])
print(eiffeltowerlocation) #print [48.858598  2.294485]
numpydimension = eiffeltowerlocation.ndim
print(numpydimension) #print 1
numpyshape = eiffeltowerlocation.shape
print(numpyshape) #print (2,)
numpylength = len(eiffeltowerlocation)
print(numpylength) #print 2
numpydatatype = eiffeltowerlocation.dtype
print(numpydatatype) #print float64
aintegers = np.array([1, 2, 3, 4])
print(aintegers) #print [1 2 3 4]
print(aintegers.dtype) #print int64
afloat = aintegers.astype(np.float64)
print(afloat) #print [1. 2. 3. 4.]
print(afloat.dtype) #print float64
#Summary create NumPy array objects
noinitializearrayint8 = np.empty([2, 2])
print(noinitializearrayint8)
'''
[[1. 2.]
 [3. 4.]]
'''
noinitializearrayint8 = np.empty([2, 2], dtype=np.int8)
print(noinitializearrayint8)
'''
[[1 1]
 [1 1]]
'''
noinitializearrayint64 = np.empty([2, 3], dtype=np.int64)
print(noinitializearrayint64)
'''
[[       46410240               0 140363434771488]
 [140363257639664 140363434385840 140363435342640]]
'''
noinitializearrayfloat = np.empty([3, 2], dtype=np.float64)
print(noinitializearrayfloat)
'''
[[2.13603788e-316 0.00000000e+000]
 [3.63033829e+024 1.94178988e-231]
 [1.28326475e+116 2.34839580e+251]]
'''
diagonalones = np.identity(4, dtype=np.int8)
print(diagonalones)
'''
[[1 0 0 0]
 [0 1 0 0]
 [0 0 1 0]
 [0 0 0 1]]
'''
onesarray = np.ones(3)
print(onesarray) #print [1. 1. 1.]
onesarray = np.ones(3, dtype=np.int8)
print(onesarray) #print [1 1 1]
converttoonesarray = np.ones_like(aintegers, dtype=np.int8)
print(converttoonesarray) #print [1 1 1 1]
zerosarray = np.zeros(3)
print(zerosarray) #print [0. 0. 0.]
zerosarray = np.zeros(3, dtype=np.int8)
print(zerosarray) #print [0 0 0]
converttozerosarray = np.zeros_like(aintegers, dtype=np.int8)
print(converttozerosarray) #print [0 0 0 0]
arangearray = np.arange(4, 40, 5)
print(arangearray) #print [ 4  9 14 19 24 29 34 39]
yesinitializearray = np.full((3, 3), 55, dtype=np.int16)
print(yesinitializearray)
'''
[[55 55 55]
 [55 55 55]
 [55 55 55]]
'''
print(np.copy(yesinitializearray)) #RM:  what's the idea using np.copy to return an array copy of the given object
'''
[[55 55 55]
 [55 55 55]
 [55 55 55]]
'''
converttoanothervaluearray = np.full_like(aintegers, 123)
print(converttoanothervaluearray) #print [123 123 123 123]
numberslist = [[1.1, 2.2, 3.3, 4.4, 5.5], [6.6, 7.7, 8.8, 9.9, 10.10]]
print(numberslist) #print [[1.1, 2.2, 3.3, 4.4, 5.5], [6.6, 7.7, 8.8, 9.9, 10, 10]]
print(type(numberslist)) #print <class 'list'>
numpyarray = np.array(numberslist, dtype=np.float32)
print(numpyarray)
'''
[[ 1.1  2.2  3.3  4.4  5.5]
 [ 6.6  7.7  8.8  9.9 10.1]]
'''
print(type(numpyarray)) #print <class 'numpy.ndarray'>
print(numpyarray.ravel()) #print [ 1.1  2.2  3.3  4.4  5.5  6.6  7.7  8.8  9.9 10.1] #RM:  convert two dimension to one dimension
print(numpyarray.ravel().ndim) #print 1
floatsasstring = "3.14 2.17 123.987"
print(np.fromstring(floatsasstring, dtype=np.float64, sep=" ")) #print [  3.14    2.17  123.987] #creates a one dimension array from a string or text
inputtoarray = [3.14, 2.46]
print(inputtoarray) #print [3.14, 2.46]
print(np.asarray(inputtoarray)) #print [3.14 2.46]
