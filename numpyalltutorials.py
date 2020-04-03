#RM:  find time for the w3resoruce numpy
#w3numpybasic.py includes lessons not learned in YouTube videos such as element-wise comparison
#Numpy is the core Python library for scientific and numercial computing.  It provides array objects.
#Single data type; e.g. all floats or all integers.  Less memory.  NumPy data types:  int8 bit -128 to 127, int16 bit -32768 to 32,767, int32, int64, uint8 unsigned integer 0 to 255, uint16 0 to 65535, uint32, uint64, float16 half precision signed float, float32 single precision signed lfoat, float64 double precision signed float, complex, compex64, complex 128.  Also boolean bool_, string, datetime, and python object.  Default is float64.

#Python_ NUMPY _ Numerical Python Arrays Tutorial [720p] Joe James
#numpy tutorial - introduction channel codebasics, numpy tutorial - basic array operations, numpy tutorial - slicingstacking arrays, indexing with boolean arrays
#Numpy and Loops in Python
#Python NumPy Tutorial _ NumPy Array _ Python Tutorial For Beginners _ Python Training _ Edureka [720p]
#NumPy Tutorial Part - 1 _ NumPy Array _ Python NumPy Tutorial Part -1_ Python Tutorial _ Simplilearn [720p], NumPy Tutorial Part - 2 _ NumPy Array _ Python NumPy Tutorial Part -2_ Python Tutorial _ Simplilearn [720p]

#print(help(np.linspace)) #RM:  press q to exit or quit
import numpy as np

#Numpy is a multidimensional array object.  anarray is a two-dimensional array because it contains rows and columns.
anarray = np.array([[1,2,3],[5,6,7],[8,9,10],[11,12,13]])
print(anarray)
'''
[[ 1  2  3]
 [ 5  6  7]
 [ 8  9 10]
 [11 12 13]]
'''
print(anarray.flatten()) #print [ 1  2  3  5  6  7  8  9 10 11 12 13]
print(anarray.flatten(order="F"))  #print [ 1  5  8 11  2  6  9 12  3  7 10 13].  F stands for Fortran or column-major.  Flattens by column 1, column 2, column 3 top to bottom.
print(anarray.flatten(order="C"))  #print [ 1  2  3  5  6  7  8  9 10 11 12 13].  C stands for C code or row-major the default.
print(anarray.flatten(order="A"))  #print [ 1  2  3  5  6  7  8  9 10 11 12 13].  A stands for C and Fortran.
print(anarray[0,0]) #print 1
print(anarray[0,1]) #print 2
print(anarray[1,1]) #print 6
print(anarray[1,2]) #print 7
print(anarray[2,0]) #print 8
print(anarray[2,2]) #print 10
print(anarray[3,1]) #print 12
print(anarray[3,2]) #print 13
print(anarray.dtype) #print int64
print(anarray.shape) #print (4,3)
print(anarray.ndim) #print 2
print(anarray.itemsize) #print 8
print(anarray.size) #print 12
print(anarray.itemsize*anarray.size) #print 96
anarray = np.array([[1,2,3],[5,6,7],[8,9,10],[11,12,13]], dtype=np.int8)
print(anarray.dtype) #print int8
print(anarray.itemsize) #print 1
print(anarray.size) #print 12
print(anarray.itemsize*anarray.size) #print 12

definenumpyarray = np.array([2,3,4])
print(definenumpyarray) #print [2 3 4]
print(definenumpyarray.shape) #print (3,)
print(definenumpyarray.ndim) #print 1
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
print(numpyrange[:4]) #print [0 1 2 3]
slicesoda = slice(2,9,2)
print(numpyrange[slicesoda]) #print [2 4 6 8]
print(numpyrange[2:9:2]) #print [2 4 6 8]
print(numpyrange[-1::-1]) #print [11 10  9  8  7  6  5  4  3  2  1  0]
print(numpyrange[-1:-6:-2]) #print [11  9  7]
numpyrangereshape = numpyrange.reshape(4,3)
print(numpyrangereshape)
'''
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
'''
numpyrangetranspose = numpyrangereshape.transpose()
print(numpyrangetranspose)
'''
[[ 0  3  6  9]
 [ 1  4  7 10]
 [ 2  5  8 11]]
'''
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
bravo = np.arange(0,8).reshape(2,4)
print(bravo)
'''
[[0 1 2 3]
 [4 5 6 7]]
'''
charlie = bravo.reshape(2,2,2)
print(charlie)
'''
[[[0 1]
  [2 3]]

 [[4 5]
  [6 7]]]
'''
print(np.rollaxis(charlie,1,0))
'''
[[[0 1]
  [4 5]]

 [[2 3]
  [6 7]]]
'''
print(np.rollaxis(charlie,2,0))
'''
[[[0 2]
  [4 6]]

 [[1 3]
  [5 7]]]
'''
print(np.rollaxis(charlie,2,1))
'''
[[[0 2]
  [1 3]]

 [[4 6]
  [5 7]]]
'''
print(np.rollaxis(charlie,1,2))
'''
[[[0 1]
  [2 3]]

 [[4 5]
  [6 7]]]
'''
print(np.swapaxes(charlie,1,2))
'''
[[[0 2]
  [1 3]]

 [[4 6]
  [5 7]]]
'''
x = np.ones(50, dtype=np.int8)
print(x) #print [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]
print(len(x)) #print 50
#Not functions.  No need for paranthesis.
numberofelements = newdimension.size
print(numberofelements) #print 6
numpyshape = newdimension.shape
print(numpyshape) #print (3, 2)
#RM:  if a numpy array is one row, then its (number of columns,); e.g. (6,) for one row and six columns
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
print("Dimensions?",xtworows.ndim) #print Dimensions? 2
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

randomintegerstenbyten = np.random.randint(100, size=(10,10)) #https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.randint.html
print(randomintegerstenbyten)
'''
[[95 30  1 77 89  7 68 43 60 48]
 [ 5  2  7 10 10 45 20 55 58 44]
 [31 20 35  0 51 79 93 26 15 39]
 [80 56 32 24  5 42 35  7 25 29]
 [89 83  8 48 24 97 35 71 32 82]
 [90 41 59 48  9 37 51 99 77 50]
 [63 95 71 79 89 30 85 76 20 99]
 [41 59 85 92 44  8 19  5 83 35]
 [31 26 70 70 16 46 53  3 51 77]
 [13 56 51 56 53 97 15 17 29 95]]
'''
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
arraylog10 = np.array([1,2,3])
print(np.log10(arraylog10)) #print [0.         0.30103    0.47712125]
print(np.log2(arraylog10)) #print [0.        1.        1.5849625]
print(np.pi) #print 3.141592653589793
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
flatnumpyarray = sumpartofarray.ravel()  #ravel flat or set up as a one line column
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
print(np.concatenate((fourarray, eightarray)))
'''
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
'''
print(np.concatenate((fourarray, eightarray), axis=1))
'''
[[1 2 5 6]
 [3 4 7 8]]
'''
mathops1 = np.arange(0,9).reshape(3,3)
print(mathops1)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
'''
mathops2 = np.array([10,11,12])
print(mathops2) #print [10 11 12]
print(np.add(mathops1,mathops2))
'''
[[10 12 14]
 [13 15 17]
 [16 18 20]]
'''
print(np.subtract(mathops1,mathops2))
'''
[[-10 -10 -10]
 [ -7  -7  -7]
 [ -4  -4  -4]]
'''
print(np.multiply(mathops1,mathops2))
'''
[[ 0 11 24]
 [30 44 60]
 [60 77 96]]
'''
print(np.divide(mathops1,mathops2))
'''
[[0.         0.09090909 0.16666667]
 [0.3        0.36363636 0.41666667]
 [0.6        0.63636364 0.66666667]]
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

iteratearray = np.arange(0,45,5)
print(iteratearray) #print [ 0  5 10 15 20 25 30 35 40]
iteratearray = iteratearray.reshape(3,3)
print(iteratearray)
'''
[[ 0  5 10]
 [15 20 25]
 [30 35 40]]
'''
for x in np.nditer(iteratearray):
	print(x,end=",") #print 0,5,10,15,20,25,30,35,40,.  Instructor said you can flatten iteratearray.flatten() and run a standard for loop.
print("\n")
for x in np.nditer(iteratearray, order="C"):
	print(x,end=",") #print 0,5,10,15,20,25,30,35,40,
print("\n")
for x in np.nditer(iteratearray, order="F"):
	print(x,end=",") #print 0,15,30,5,20,35,10,25,40,
print("\n")
slicingarray = np.array([[6,7,8],[1,2,3],[9,3,2]])
print(slicingarray)
'''
[[6 7 8]
 [1 2 3]
 [9 3 2]]
'''
print(slicingarray[1,2]) #print 3.  row 1, column 2
print(slicingarray[0:,2]) #print [8 3 2]  rows 0-, column 2
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
stackarraya = np.array([[1,2,3],[5,6,7]])
stackarrayb = np.array([[8,9,10],[11,12,13]])
print(stackarraya)
'''
[[1 2 3]
 [5 6 7]]
'''
print(stackarrayb)
'''
[[ 8  9 10]
 [11 12 13]]
'''
print(np.vstack((stackarraya,stackarrayb)))
'''
[[ 1  2  3]
 [ 5  6  7]
 [ 8  9 10]
 [11 12 13]]
'''
print(np.vstack((stackarraya,stackarrayb)).shape) #print (4,3)
print(np.hstack((stackarraya,stackarrayb)))
'''
[[ 1  2  3  8  9 10]
 [ 5  6  7 11 12 13]]
'''
print(np.hstack((stackarraya,stackarrayb)).shape) #print (2,6)
print(stackarraya.ravel()) #print [1 2 3 5 6 7]
print(stackarraya.ravel().shape) #print (6,)
splita = np.arange(9)
print(splita) #print [0 1 2 3 4 5 6 7 8]
splitathree = np.split(splita,3)
print(splitathree) #print [array([0, 1, 2]), array([3, 4, 5]), array([6, 7, 8])]
print(splitathree[0]) #print [0 1 2]
print(splitathree[1][2]) #print 5
splita45 = np.split(splita,[4,5])
print(splita45) #print [array([0, 1, 2, 3]), array([4]), array([5, 6, 7, 8])]
splita47 = np.split(splita,[4,7])
print(splita47) #print [array([0, 1, 2, 3]), array([4, 5, 6]), array([7, 8])]
splita47 = np.split(splita,[1,7,4])
print(splita47) #print [array([0]), array([1, 2, 3, 4, 5, 6]), array([], dtype=int64), array([4, 5, 6, 7, 8])]
print(splita47[3]) #print [4 5 6 7 8]
resizea = np.array([[1,2,3], [4,5,6]])
print(resizea)
'''
[[1 2 3]
 [4 5 6]]
'''
print(resizea.shape) #print (2, 3)
resizeb = np.resize(resizea,(3,2))
print(resizeb)
'''
[[1 2]
 [3 4]
 [5 6]]
'''
print(resizeb.shape) #print (3, 2)
resizec = np.resize(resizea,(3,3))
print(resizec)
'''
[[1 2 3]
 [4 5 6]
 [1 2 3]]
'''
print(resizec.shape) #print (3, 3)

print(np.char.add(["hello","hi"],["abc","xyz"])) #print ['helloabc' 'hixyz']
print(np.char.multiply("Hello ",3)) #print Hello Hello Hello 
print(np.char.center("Hello",20,fillchar="-")) #print -------Hello--------
#also fillchar can do capitalize, title, lower case, upper case, split, split line, join
print(np.char.capitalize("hello world")) #print Hello world
print(np.char.title("hello world")) #print Hello World
print(np.char.lower(["HELLO","WORLD"])) #print ['hello' 'world']
print(np.char.lower("HELLO")) #print hello
print(np.char.upper(["hello","world"])) #print ['HELLO' 'WORLD']
print(np.char.upper("hello")) #print HELLO
print(np.char.split(["are you coming to the party?"])) #print [list(['are', 'you', 'coming', 'to', 'the', 'party?'])]
print(np.char.split(["are you coming to the party?"])[0]) #print ['are', 'you', 'coming', 'to', 'the', 'party?']
print(np.char.split(["are you coming to the party?"])[0][3]) #print to
print(np.char.splitlines("hello\nhow are you?")) #print ['hello', 'how are you?']
print(np.char.splitlines("hello\n how are you?")) #print ['hello', ' how are you?']
print(np.char.strip(["nina","admin","anaita"],"a")) #print ['nin' 'dmin' 'nait'].  Removes all leading and trailing a.
print(np.char.join([":","-"],["dmy","ymd"])) #print ['d:m:y' 'y-m-d']
print(np.char.replace("He is a good dancer.","is","was")) #print He was a good dancer.
sentence = ["a water","an egg","an umbrella","a dough"]
for eachsentence in sentence:
	print(np.char.replace(eachsentence,"an","the"))
'''
a water
the egg
the umbrella
a dough
'''

#Exercises
#Create a 6X6 two-dimensional array.  0s and 1s alternate across the diagonals.  Start with 0 at [0,0]
array6x6 = np.zeros((6,6), dtype=int)
print(array6x6)
'''
[[0 0 0 0 0 0]
 [0 0 0 0 0 0]
 [0 0 0 0 0 0]
 [0 0 0 0 0 0]
 [0 0 0 0 0 0]
 [0 0 0 0 0 0]]
'''
array6x6[1::2,0::2] = 1  #rows start at 1 every 2, columns start at 0 every 2
print(array6x6)
'''
[[0 0 0 0 0 0]
 [1 0 1 0 1 0]
 [0 0 0 0 0 0]
 [1 0 1 0 1 0]
 [0 0 0 0 0 0]
 [1 0 1 0 1 0]]
'''
array6x6[0::2,1::2] = 1  #rows start at 0 every 2, columns start at 1 every 2
print(array6x6)
'''
[[0 1 0 1 0 1]
 [1 0 1 0 1 0]
 [0 1 0 1 0 1]
 [1 0 1 0 1 0]
 [0 1 0 1 0 1]
 [1 0 1 0 1 0]]
'''
#Find the total number and locations of missing values in the array
missingvaluesrandomintegers = np.random.rand(10,10)
print(missingvaluesrandomintegers)
'''
[[0.88751073 0.58949487 0.48114543 0.83262386 0.18668592 0.18267376
  0.89156489 0.3991325  0.80501603 0.76052358]
 [0.23299003 0.58887718 0.25444025 0.62653396 0.87544497 0.24087074
  0.12150625 0.91325496 0.88046513 0.18700451]
 [0.92616198 0.79691826 0.36697385 0.2161998  0.09843074 0.60393916
  0.08024492 0.41214514 0.65896521 0.98395877]
 [0.5645292  0.60887495 0.98013915 0.84297063 0.72834984 0.50315929
  0.47855641 0.65042673 0.37535314 0.52618225]
 [0.84331411 0.92631853 0.29501767 0.85703056 0.81327316 0.18041479
  0.63759755 0.49366616 0.78604887 0.70871793]
 [0.04144435 0.90529237 0.33938827 0.75600622 0.86920404 0.54634517
  0.45698737 0.29209403 0.55879825 0.42461227]
 [0.31357655 0.58221229 0.39642724 0.75557585 0.53948792 0.61255027
  0.24117842 0.60820889 0.02968306 0.3011667 ]
 [0.82931063 0.21898005 0.65101738 0.01306896 0.14099429 0.07138532
  0.63786322 0.22982065 0.97433217 0.09272359]
 [0.65239469 0.30731127 0.63608784 0.28022175 0.98540152 0.72134415
  0.60975797 0.48423801 0.42216619 0.27976922]
 [0.08032698 0.18193074 0.14266158 0.55665796 0.47306999 0.01407798
  0.69330529 0.04943839 0.56891648 0.8083108 ]]
'''
#randomly find five index positions set to Null
missingvaluesrandomintegers[np.random.randint(10, size=5), np.random.randint(10, size=5)] = np.nan
print(missingvaluesrandomintegers)
'''
[[0.88751073 0.58949487 0.48114543 0.83262386 0.18668592 0.18267376
  0.89156489 0.3991325  0.80501603 0.76052358]
 [0.23299003 0.58887718 0.25444025 0.62653396 0.87544497 0.24087074
  0.12150625 0.91325496 0.88046513 0.18700451]
 [0.92616198 0.79691826 0.36697385 0.2161998  0.09843074 0.60393916
  0.08024492 0.41214514        nan 0.98395877]
 [0.5645292  0.60887495 0.98013915 0.84297063        nan 0.50315929
  0.47855641 0.65042673 0.37535314 0.52618225]
 [0.84331411 0.92631853 0.29501767 0.85703056 0.81327316 0.18041479
  0.63759755 0.49366616 0.78604887 0.70871793]
 [0.04144435 0.90529237 0.33938827        nan 0.86920404 0.54634517
  0.45698737 0.29209403 0.55879825 0.42461227]
 [0.31357655 0.58221229 0.39642724 0.75557585 0.53948792 0.61255027
  0.24117842 0.60820889 0.02968306        nan]
 [0.82931063 0.21898005 0.65101738 0.01306896 0.14099429 0.07138532
  0.63786322 0.22982065 0.97433217 0.09272359]
 [       nan 0.30731127 0.63608784 0.28022175 0.98540152 0.72134415
  0.60975797 0.48423801 0.42216619 0.27976922]
 [0.08032698 0.18193074 0.14266158 0.55665796 0.47306999 0.01407798
  0.69330529 0.04943839 0.56891648 0.8083108 ]]
'''
print("Total number of missing values:",np.isnan(missingvaluesrandomintegers).sum()) #print Total number of missing values: 5
print("Indexes of missing values:",np.argwhere(np.isnan(missingvaluesrandomintegers)))
'''
Indexes of missing values: [[2 8]
 [3 4]
 [5 3]
 [6 9]
 [8 0]]
'''
splitarraytotwoarraysrowsandcolumns = np.where(np.isnan(missingvaluesrandomintegers))
print(splitarraytotwoarraysrowsandcolumns) #print (array([2, 3, 5, 6, 8]), array([8, 4, 3, 9, 0]))
missingvaluesrandomintegers[splitarraytotwoarraysrowsandcolumns] = 0
print(missingvaluesrandomintegers)
'''
[[0.88751073 0.58949487 0.48114543 0.83262386 0.18668592 0.18267376
  0.89156489 0.3991325  0.80501603 0.76052358]
 [0.23299003 0.58887718 0.25444025 0.62653396 0.87544497 0.24087074
  0.12150625 0.91325496 0.88046513 0.18700451]
 [0.92616198 0.79691826 0.36697385 0.2161998  0.09843074 0.60393916
  0.08024492 0.41214514 0.         0.98395877]
 [0.5645292  0.60887495 0.98013915 0.84297063 0.         0.50315929
  0.47855641 0.65042673 0.37535314 0.52618225]
 [0.84331411 0.92631853 0.29501767 0.85703056 0.81327316 0.18041479
  0.63759755 0.49366616 0.78604887 0.70871793]
 [0.04144435 0.90529237 0.33938827 0.         0.86920404 0.54634517
  0.45698737 0.29209403 0.55879825 0.42461227]
 [0.31357655 0.58221229 0.39642724 0.75557585 0.53948792 0.61255027
  0.24117842 0.60820889 0.02968306 0.        ]
 [0.82931063 0.21898005 0.65101738 0.01306896 0.14099429 0.07138532
  0.63786322 0.22982065 0.97433217 0.09272359]
 [0.         0.30731127 0.63608784 0.28022175 0.98540152 0.72134415
  0.60975797 0.48423801 0.42216619 0.27976922]
 [0.08032698 0.18193074 0.14266158 0.55665796 0.47306999 0.01407798
  0.69330529 0.04943839 0.56891648 0.8083108 ]]
'''