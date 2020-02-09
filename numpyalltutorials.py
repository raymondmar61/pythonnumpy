#RM:  find time for the w3resoruce numpy
#w3numpybasic.py includes lessons not learned in YouTube videos such as element-wise comparison
#Single data type; e.g. all floats or all integers.  Less memory.  NumPy data types:  int8 bit -128 to 127, int16 bit -32768 to 32,767, int32, int64, uint8 unsigned integer 0 to 255, uint16 0 to 65535, uint32, uint64, float16 half precision signed float, float32 single precision signed lfoat, float64 double precision signed float, complex, compex64, complex 128.  Also boolean bool_, string, datetime, and python object.  Default is float64.

#Python_ NUMPY _ Numerical Python Arrays Tutorial [720p] Joe James
import numpy as np

definenumpyarray = np.array([2,3,4])
print(definenumpyarray) #print [2 3 4]
print(type(definenumpyarray)) #print <class 'numpy.ndarray'>
definenumpyarray = np.array((2,3,4))
print(definenumpyarray) #print [2 3 4]
print(type(definenumpyarray)) #print <class 'numpy.ndarray'>
numpyrange = np.arange(0,12)
print(numpyrange) #print [ 0  1  2  3  4  5  6  7  8  9 10 11]
numpyrange = np.arange(0,12,2)
print(numpyrange) #print [ 0  2  4  6  8 10]
evenspread = np.linspace(0,12,6) #six elements between 0 and 12 inclusive
print(evenspread) #print [ 0.   2.4  4.8  7.2  9.6 12. ]
newdimension = evenspread.reshape(3,2) #three rows, two columns
print(newdimension)
'''
[[ 0.   2.4]
 [ 4.8  7.2]
 [ 9.6 12. ]]
'''
#Not functions.  No need for paranthesis.
numberofelements = newdimension.size
print(numberofelements) #print 6
numpyshape = newdimension.shape
print(numpyshape) #print (3, 2)
datatype = newdimension.dtype
print(datatype) #print float64
memoryinbyteseachelementtakes = newdimension.itemsize
print(memoryinbyteseachelementtakes) #print 8
twodimensionarray = np.array([(1.5,2,3), (4,5,6)])
print(twodimensionarray)
'''
[[1.5 2.  3. ]
 [4.  5.  6. ]]
'''
lessthanfour = twodimensionarray < 4
print(lessthanfour)
'''
[[ True  True  True]
 [False False False]]
'''
multiplybythree = twodimensionarray * 3
print(multiplybythree)
'''
[[ 4.5  6.   9. ]
 [12.  15.  18. ]]
'''
zeroesarray = np.zeros([3,4])
print(zeroesarray)
'''
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
'''
onesarray = np.ones((10))
print(onesarray) #print [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
print(type(onesarray)) #print <class 'numpy.ndarray'>
onesarrayonerow = np.ones((1,10))
print(onesarrayonerow) #print [[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]]
print(type(onesarrayonerow)) #print <class 'numpy.ndarray'>
onesarraylist = np.ones([10])
print(onesarraylist) #print [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
onesarraylistonerow = np.ones([1,10])
print(onesarraylistonerow) #print [[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]]
onesarrayintegeronerow = np.ones((1,10), dtype=np.int8)
print(onesarrayintegeronerow) #print [[1 1 1 1 1 1 1 1 1 1]]
onesarrayinteger = np.ones([10], dtype=np.int8)
print(onesarrayinteger) #print [1 1 1 1 1 1 1 1 1 1]
randomarraybetweenzeroandone = np.random.random([2,3])
print(randomarraybetweenzeroandone)
'''
[[0.52032048 0.99112424 0.55722295]
 [0.55220491 0.7386064  0.17911793]]
'''
randomarrayintegers = np.random.randint(0,11,5)
print(randomarrayintegers) #print [ 4 10  9  6  9]
onerandomnumber = np.random.choice(randomarrayintegers)
print(onerandomnumber) #print 10
shufflenumbers = np.random.shuffle(randomarrayintegers)
print(shufflenumbers) #print None
sumarray = randomarrayintegers.sum()
print(sumarray) #print 38
minimumnumber = randomarrayintegers.min()
print(minimumnumber) #print 4
maximumnumber = randomarrayintegers.max()
print(maximumnumber) #print 10
averagenumber = randomarrayintegers.mean()
print(averagenumber) #print 7.6
variancenumber = randomarrayintegers.var()
print(variancenumber) #print 5.04
standarddeviationnumber = randomarrayintegers.std()
print(standarddeviationnumber) #print 2.244994432064365
sumpartofarray = np.array([3,8,4,5,3,8], dtype=np.int8)
sumpartofarray = sumpartofarray.reshape(3,2)
print(sumpartofarray)
'''
[[3 8]
 [4 5]
 [3 8]]
'''
sumbyrow = sumpartofarray.sum(axis=1)
print(sumbyrow) #print [11  9 11]
sumbycolumn = sumpartofarray.sum(axis=0)
print(sumbycolumn) #print [10 21]
importtextfile = np.loadtxt("joejamesdata.txt", dtype=np.uint8, delimiter=",", skiprows=1) #The first row is the column headings
print(importtextfile)
'''
[[9 3 8 7 6 1 0 4 2 5]
 [1 7 4 9 2 6 8 3 5 0]
 [4 8 3 9 5 7 2 6 0 1]
 [1 7 4 2 5 9 6 8 0 3]
 [0 7 5 2 8 6 3 4 1 9]
 [5 9 1 4 7 0 3 6 8 2]]
'''
print(importtextfile.dtype) #print uint8
