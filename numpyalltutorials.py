#RM:  find time for the w3resoruce numpy
#w3numpybasic.py includes lessons not learned in YouTube videos such as element-wise comparison
#Single data type; e.g. all floats or all integers.  Less memory.  NumPy data types:  int8 bit -128 to 127, int16 bit -32768 to 32,767, int32, int64, uint8 unsigned integer 0 to 255, uint16 0 to 65535, uint32, uint64, float16 half precision signed float, float32 single precision signed lfoat, float64 double precision signed float, complex, compex64, complex 128.  Also boolean bool_, string, datetime, and python object.  Default is float64.

#Python_ NUMPY _ Numerical Python Arrays Tutorial [720p] Joe James
#numpy tutorial - introduction channel codebasics, numpy tutorial - basic array operations, numpy tutorial - slicingstacking arrays, indexing with boolean arrays
#Numpy and Loops in Python

#print(help(np.linspace)) #RM:  press q to exit or quit
import numpy as np

definenumpyarray = np.array([2,3,4])
print(definenumpyarray) #print [2 3 4]
print(definenumpyarray[2]) #print 4
print(type(definenumpyarray)) #print <class 'numpy.ndarray'>
definenumpyarray = np.array((2,3,4))
print(definenumpyarray) #print [2 3 4]
print(definenumpyarray[2]) #print 4
print(type(definenumpyarray)) #print <class 'numpy.ndarray'>
numpyrange = np.arange(0,12)
print(numpyrange) #print [ 0  1  2  3  4  5  6  7  8  9 10 11]
print(numpyrange[6:9]) #print [6 7 8]
print(numpyrange[-1]) #print 11
print(numpyrange[-1::-1]) #print [11 10  9  8  7  6  5  4  3  2  1  0]
print(numpyrange[-1:-6:-2]) #print [11  9  7]
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
x = np.ones(50, dtype=np.int8)
print(x) #print [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]
print(len(x)) #print 50
#Not functions.  No need for paranthesis.
numberofelements = newdimension.size
print(numberofelements) #print 6
numpyshape = newdimension.shape
print(numpyshape) #print (3, 2)
datatype = newdimension.dtype
print(datatype) #print float64
memoryinbyteseachelementtakes = newdimension.itemsize
print(memoryinbyteseachelementtakes) #print 8
totalitemsize = newdimension.size*newdimension.itemsize
print(totalitemsize) #print 48
twodimensionarray = np.array([(1.5,2,3), (4,5,6)])
print(twodimensionarray)
'''
[[1.5 2.  3. ]
 [4.  5.  6. ]]
'''
numberofdimensions = twodimensionarray.ndim
print(numberofdimensions) #print 2
lessthanfour = twodimensionarray < 4
print(lessthanfour)
'''
[[ True  True  True]
 [False False False]]
'''
print(twodimensionarray[lessthanfour]) #print [1.5 2.  3. ]  RM:  returned numbers less than four in an array
twodimensionarray[lessthanfour] = 1919
print(twodimensionarray)  #RM:  replaced numbers less than four with 1919 in an array
'''
[[1919. 1919. 1919.]
 [   4.    5.    6.]]
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
xtworows = np.ones((2,50), dtype=np.int8)
print(xtworows)
'''
[[1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
  1 1 1 1 1 1 1 1 1 1 1 1 1 1]
 [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
  1 1 1 1 1 1 1 1 1 1 1 1 1 1]]
'''
print(len(xtworows)) #print 2
print("How many number ones?",xtworows.size) #print How many number ones? 100
print("Dimensions?",xtworows.ndim) #print How many number ones? 2
z = np.empty(10)
print(z)
'''
[6.94456331e-310 1.17981216e-316 4.94065646e-324 1.17161225e-316
 1.33360289e+241 6.94456333e-310 1.35507283e+248 2.28563350e+243
 4.66839074e-313 1.33360297e+241]
'''
z = np.empty(50, dtype=np.int8)
print(z)
'''
[1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1]
'''
#Create a while loop to append a random integer between 1 and 10 to mymatrix.  Stop the loop when the random integer is 7 or when there are 30 numbers.
import random
mymatrix = np.ones(1)
print(mymatrix) #print [1.]
i = 1
while mymatrix[-1] != 7:
	randomnumber = random.randint(1,10)
	mymatrix = np.append(mymatrix,randomnumber)
	i += 1
	if i > 29:  #there is one number in mymatrix from mymatrix = np.ones(1) and counter started at 1
		break
print(mymatrix) #print [ 1.  8.  5. 10.  8.  3.  2.  6.  2.  4.  5.  5.  2.  5.  9.  6.  2. 10.  4.  2.  4.  9.  4. 10.  7.]

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
print(np.std(randomarrayintegers)) #print 2.244994432064365
print(np.sqrt(randomarrayintegers)) #print [2.         3.16227766 3.         2.44948974 3.        ]
sumpartofarray = np.array([3,8,4,5,3,8], dtype=np.int8)
print(sumpartofarray) #print [3 8 4 5 3 8]
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
flatnumpyarray = sumpartofarray.ravel()
print(flatnumpyarray) #print [3 8 4 5 3 8]
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

addnumpy1 = np.array([1,2,3])
addnumpy2 = np.array([4,5,6])
print(addnumpy1+addnumpy2) #print [5 7 9]
print(addnumpy1+addnumpy1) #print [2 4 6]
print(addnumpy1*addnumpy2) #print [ 4 10 18]
combinearray = np.array([addnumpy1,addnumpy2])
print(combinearray) 
'''
[[1 2 3]
 [4 5 6]]
'''
print(combinearray.ndim) #print 2
reshape2down3across = combinearray.reshape(3,2)
print(reshape2down3across)
'''
[[1 2]
 [3 4]
 [5 6]]
'''
#axis 1 is rows left to right.  axis 0 is columns up to down.
print(reshape2down3across.sum(axis=0)) #print [ 9 12]
print(reshape2down3across.sum(axis=1)) #print [ 3  7 11]
#squareroot = combinearray.sqrt()
#print(squareroot) #AttributeError: 'numpy.ndarray' object has no attribute 'sqrt'
print(np.sqrt(reshape2down3across))
'''
[[1.         1.41421356]
 [1.73205081 2.        ]
 [2.23606798 2.44948974]]
'''
fourarray = np.array([[1,2],[3,4]])
eightarray = np.array([[5,6],[7,8]])
print(fourarray)
'''
[[1 2]
 [3 4]]
 '''
print(eightarray)
'''
[[5 6]
 [7 8]]
'''
print(fourarray+eightarray)
'''
[[ 6  8]
 [10 12]]
'''
print(fourarray*eightarray)
'''
[[ 5 12]
 [21 32]]
'''
print(fourarray.dot(eightarray)) #dot product matrix multiplication https://www.mathsisfun.com/algebra/matrix-multiplying.html
'''
[[19 22]  (1*5)+(2*7); (1*6)+(2*8)
 [43 50]]  (3*5)+(4*7); (3*6)+(4*8)
'''
numpya = np.arange(1,10)
print(numpya) #print [1 2 3 4 5 6 7 8 9]
numpya = numpya.reshape(3,3)
print(numpya)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''
numpyx = np.array([[1],[3],[4]])
print(numpyx)
'''
[[1]
 [3]
 [4]]
'''
numpyb = np.array([[-0.1, -0.2, -0.3],[3, 10, 2],[4, 2, 0.5]])
print(numpyb)
'''
[[-0.1 -0.2 -0.3]
 [ 3.  10.   2. ]
 [ 4.   2.   0.5]]
'''
print(np.cross(numpya,numpyb)) #cross product
'''
[[ 1.11022302e-16 -5.55111512e-17  0.00000000e+00]
 [-5.00000000e+01  1.00000000e+01  2.50000000e+01]
 [-1.40000000e+01  3.25000000e+01 -1.80000000e+01]]
'''
print(np.dot(numpya,numpyx)) #dot product matrix multiplication https://www.mathsisfun.com/algebra/matrix-multiplying.html
'''
[[19]  (1*1)+(2*3)+(3*4)
 [43]  (4*1)+(5*3)+(6*4)
 [67]]  (7*1)+(8*3)+(9*4)
'''
#numpya^-1 or numpya-inverse multiply numpyb linear algebra
inversenumpya = np.linalg.inv(numpya)
print(inversenumpya)
'''
[[-4.50359963e+15  9.00719925e+15 -4.50359963e+15]
 [ 9.00719925e+15 -1.80143985e+16  9.00719925e+15]
 [-4.50359963e+15  9.00719925e+15 -4.50359963e+15]]
'''

slicingarray = np.array([[6,7,8],[1,2,3],[9,3,2]])
print(slicingarray)
'''
[[6 7 8]
 [1 2 3]
 [9 3 2]]
'''
print(slicingarray[1,2]) #print 3.  row 1, column 2
print(slicingarray[0:2,2]) #print [8 3].  rows 0-1, column 2
print(slicingarray[-1]) #print [9 3 2].  rows last row
print(slicingarray[-1,0:2]) #print [9 3].  rows last, columns 0-1
print(slicingarray[0:3,1:3])
'''
[[7 8]
 [2 3]
 [3 2]]
'''
print(slicingarray[:,1:3])
'''
[[7 8]
 [2 3]
 [3 2]]
'''
for eachrow in slicingarray:
	print(eachrow)
'''
[6 7 8]
[1 2 3]
[9 3 2]
'''
for cell in slicingarray.flat:
	print(cell) #print 6\n 7\n 8\n 1\n 2\n 3\n 9\n 3\n 2\n
print(slicingarray.ravel()) #print [6 7 8 1 2 3 9 3 2]
print(slicingarray.ravel()[0]) #print 6
print(slicingarray.ravel()[3]) #print 1