#YouTube Joeyajames
#YouTube edureka
#YouTube www.Simplilearn.com
#YouTube Introduction to Numerical Computing with NumPy SciPy 2019 Tutorial Alex Chabot-Leclerc www.enthought.com

#RM:  find time for the w3resoruce numpy
#w3numpybasic.py includes lessons not learned in YouTube videos such as element-wise comparison
#NumPy data types:  int8 bit -128 to 127, int16 bit -32768 to 32,767, int32, int64, uint8 unsigned integer 0 to 255, uint16 0 to 65535, uint32, uint64, float16 half precision signed float, float32 single precision signed lfoat, float64 double precision signed float, complex, compex64, complex 128.  Also boolean bool_, string, datetime, and python object.  Default is float64.
import numpy as np

numpyarray = np.array([2,3,4])
print(numpyarray) #print [2 3 4]
numpyrange = np.arange(1,13,2)
print(numpyrange) #print [ 1  3  5  7  9 11].  Print numbers starting at 1 exclusive at 13 increment by 2
numpyrandom = np.random.random(3)  #Random numbers between 0 and 1
print(numpyrandom) #print [0.31309967 0.7921456  0.78090792].  
numpyrandominteger = np.random.randint(0,10,5) #Random integers between 0 and 10 inclusive five elements
print(numpyrandominteger) #print [3 0 4 7 9]
numpylinspace = np.linspace(1,12,6)
print(numpylinspace) #print [ 1.   3.2  5.4  7.6  9.8 12. ].  Print six numbers starting a 1 equal separation at 12 inclusive
numpylinspace = np.linspace(1,12,6, dtype=np.int8)
print(numpylinspace) #print [ 1  3  5  7  9 12].  Print six numbers starting a 1 almost equal separation at 12 inclusive
numpyreshape = numpylinspace.reshape(3,2)
print(numpyreshape) #print [[ 1  3]\n  [ 5  7]\n  [ 9 12]].  Reshape to three dimension two elements each or three rows two elements each.  Three rows, two columns.
numpyflatten = numpyreshape.flatten()
print(numpyflatten) #print [ 1  3  5  7  9 12]

numpyarray = np.array([6, 4, -5, 8, 99, 1000000, -53])
print(numpyarray.size) #print 7.  Number of elements
print(numpyarray.shape) #print (7,).  Always returns a tuple.  If there's no rows, then first number is columns or number of elements.
print(numpyarray.dtype) #print int64
print(numpyarray.ndim) #print 1 number of dimensions
numpyarray = np.array([(-1, -3), (0, 5), (8, 44)])
print(numpyarray.size) #print 6.  Number of elements
print(numpyarray.shape) #print (3,2).  Always returns a tuple.  If there's no rows, then first number is columns or number of elements.  Three rows, two columns.
print(numpyarray.dtype) #print int64
print(numpyarray.itemsize) #print 8 prints memory size in bytes
print(numpyarray.ndim) #print 2 number of dimensions
numpyarray = np.array([6, 4, -5, 8, 99, 1000000, -53])
print(numpyarray > 0) #print [ True  True False  True  True  True False]
numpyarray = numpyarray + 70
print(numpyarray) #print [     76      74      65      78     169 1000070      17].  Add 70 to all numbers.
numpyzeroes = np.zeros((5))
print(numpyzeroes) #print [0. 0. 0. 0. 0.]
numpyzeroes = np.zeros((5), dtype=np.int64)
print(numpyzeroes) #print [0 0 0 0 0]
numpyzeroes = np.zeros((2,3), dtype=np.int64)
print(numpyzeroes) #print [[0 0 0]\n [0 0 0]]
numpyones = np.ones((10))
print(numpyones) #print [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
numpyones = np.ones((4,2), dtype=np.int16)
print(numpyones) #print [[1 1]\n  [1 1]\n  [1 1]\n  [1 1]]
numpyk = np.random.random((2,3))
print(numpyk) #print [[0.73414294 0.31502813 0.24473664]\n [0.97007539 0.79083236 0.45979176]]
np.set_printoptions(precision = 2, suppress=True) #print future NumPy two decimal places and no scientific notation.
print(numpyk) #print [[0.73 0.32 0.24]\n [0.97 0.79 0.46]]
np.set_printoptions(edgeitems=3,infstr='inf', linewidth=75, nanstr="nan", precision=8, suppress=False, threshold=1000, formatter=None) #Default options, reset printoptions https://docs.scipy.org/doc/numpy/reference/generated/numpy.set_printoptions.html
print(numpyk) #print [[0.73414294 0.31502813 0.24473664]\n [0.97007539 0.79083236 0.45979176]]
numpyl = np.array([7,1,4,4,1])
print(type(numpyl)) #print <class 'numpy.ndarray'>
print(numpyl.sum()) #print 17
print(numpyl.min()) #print 1
print(numpyl.max()) #print 7
print(numpyl.mean()) #print 3.4.  There is no .average()
print(numpyl.var()) #print 5.039999999999999.  Variance is population.
print(numpyl.std()) #print 2.24499443206.  Standard deviation is population.
print(np.std(numpyl)) #print 2.24499443206.  Standard deviation is population.
print(np.sqrt(numpyl)) #print [2.64575131 1.         2.         2.         1.        ] square root
singlea = np.array([1, 2, 3, 4, 5])
print(singlea) #print [1 2 3 4 5]
singlea[2] = 5432
print(singlea) #print [   1    2 5432    4    5]
singlea[0] = 11.5
print(singlea) #print [11  2  3  4  5]  #type coercion.  Assign a float to integer truncates decimal part.  Assign an integer to float adds decimal.
#Use .copy() to copy an array.
originalarray = np.array([50, 51, 52, 53])
copyarray = originalarray.copy()
print(originalarray) #print [50 51 52 53]
print(copyarray) #print [50 51 52 53]
copyarray[0] = -100
print(originalarray) #print [50 51 52 53]
print(copyarray) #print [-100 51 52 53]
print("\n")



#Slicing, slicers
#Extracts a portion of a sequence by specifying a lower bound and an upper bound.  The lower bound is included.  The upper bound is excluded.  Mathematically [upper:lower).  The step value specifies the stride between elements.
#variable[lower:upper:step]  If skipping or stepping, need two colons.
'''
 -5  -4  -3  -2  -1  negative index
  0   1   2   3   4  positive index
 10  11  12  13  14
'''
easierslice = np.array([10, 11, 12, 13, 14])
print(easierslice) #print [10 11 12 13 14]
print(easierslice[3]) #print 13
print(easierslice[3:]) #print [13 14]
print(easierslice[:3]) #print [10 11 12]
print(easierslice[-2]) #print 13
print(easierslice[1:4]) #print [11 12 13]
print(easierslice[-4:4]) #print [11 12 13]
print(easierslice[-4:-1]) #print #print [11 12 13]
print(easierslice[:3]) #print #print [10 11 12]
print(easierslice[::2]) #print #print [10 12 14]
print(easierslice[::-2]) #print #print [14 12 10]
easyslice = np.array([[0, 1, 2, 3], [10, 11, 12, 13]])
print(easyslice) #print [[ 0  1  2  3]\n [10 11 12 13]]
print(easyslice[0]) #print [0 1 2 3]
print(easyslice[0,2]) #print 2
print(easyslice[1,0]) #print 10
print(easyslice[1:2]) #print [[10 11 12 13]]
print(easyslice[1, 0:3]) #print [10 11 12]
print(easyslice[1:2,0:2]) #print [[10 11]]
print(easyslice[0:2,1:]) #print [[ 1  2  3]\n [11 12 13]]
print(easyslice[0:2,1:2]) #print [[ 1]\n [11]]
print(easyslice[[0,1],[1,1]]) #print [ 1 11]
print(easyslice[[0,1],[1,3]]) #print [ 1 13]
print(easyslice[[0,1],[0,3]]) #print [ 0 13]
a4horizontal3vertical2dimension = np.array([(1, 2, 3), (5, 6, 7), (8, 9, 10), (11, 12, 13)])
print(a4horizontal3vertical2dimension)
'''
[[ 1  2  3]
 [ 5  6  7]
 [ 8  9 10]
 [11 12 13]]
'''
print(a4horizontal3vertical2dimension[0]) #print [1 2 3]
print(a4horizontal3vertical2dimension[0:,2]) #print [ 3  7 10 13]
print(a4horizontal3vertical2dimension[0:2])
'''
[[1 2 3]
[5 6 7]]
'''
print(a4horizontal3vertical2dimension[0:2,1]) #print [2 6]
print(a4horizontal3vertical2dimension[2,1:]) #print [ 9 10]
print(a4horizontal3vertical2dimension[0:2,1:2])
'''
[[2] [6]]
'''
print(a4horizontal3vertical2dimension[0:2,1:3])
'''
[[2 3]
 [6 7]]
 '''
print(a4horizontal3vertical2dimension[0,0]) #print 1
print(a4horizontal3vertical2dimension[0,2]) #print 3
print(a4horizontal3vertical2dimension[2,2]) #print 10
print(a4horizontal3vertical2dimension[3,2]) #print 13
print(a4horizontal3vertical2dimension.sum()) #print 87
print(a4horizontal3vertical2dimension.shape) #print (4,3)
print(a4horizontal3vertical2dimension.shape[0]) #print 4
a65 = np.array([[0, 1, 2, 3, 4, 5], [10, 11, 12, 13, 14, 15], [20, 21, 22, 23, 24, 25], [30, 31, 32, 33, 34, 35], [40, 41, 42, 43, 44, 45], [50, 51, 52, 53, 54, 55], [60, 61, 62, 63, 64, 65]])
print(a65)
'''
[[ 0  1  2  3  4  5]
 [10 11 12 13 14 15]
 [20 21 22 23 24 25]
 [30 31 32 33 34 35]
 [40 41 42 43 44 45]
 [50 51 52 53 54 55]
 [60 61 62 63 64 65]
 ]
'''
print(a65[2,4]) #print 24
print(a65[4:]) #print [[40 41 42 43 44 45]\n  [50 51 52 53 54 55]\n  [60 61 62 63 64 65]]
print(a65[0:3]) #print [[ 0  1  2  3  4  5]\n  [10 11 12 13 14 15]\n  [20 21 22 23 24 25]]
print(a65[:3]) #print [[ 0  1  2  3  4  5]\n  [10 11 12 13 14 15]\n  [20 21 22 23 24 25]]
print(a65[1, 2:5]) #print [12 13 14]
print(a65[5,2:5]) #print [52 53 54]
print(a65[5:6,2:5]) #print [[52 53 54]]
print(a65[0:3, 1:3])
'''
[[ 1  2]
 [11 12]
 [21 22]]
'''
print(a65[:,2]) #print [ 2 12 22 32 42 52 62]
print(a65[0:,2]) #print [ 2 12 22 32 42 52 62]
print(a65[1:4,4:5])
'''
[[14]
 [24]
 [34]]
'''
print(a65[:,3:5])
'''
[[ 3  4]
 [13 14]
 [23 24]
 [33 34]
 [43 44]
 [53 54]
 [63 64]]
'''
print(a65[4:, 4:])
'''
[[44 45]
 [54 55]
 [64 65]]
'''
print(a65[3:5,2:4])
'''
[[32 33]
 [42 43]]
'''
print(a65[2::2, ::4]) #RM:  same as print(a65[2::2, 0::4])
'''
[[20 24]
 [40 44]
 [60 64]]
'''
print(a65[0:,1:4:2])
'''
[[ 1  3]
 [11 13]
 [21 23]
 [31 33]
 [41 43]
 [51 53]
 [61 63]]
'''
print(a65[1:4:2, 0:4:2])
'''
[[10 12]
 [30 32]]
'''
slicearray1 = np.arange(0,20)
print(slicearray1) #print [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
#RM: slice is slice(inclusive, exclusive, step rate) like range, arange.
print(slicearray1[slice(2, 9, 2)]) #print [2 4 6 8]
print(slicearray1[slice(3, 15, 2)]) #print [3 5 7 9 11 13]
print(slicearray1[slice(4, 16, 2)]) #print [4 6 8 10 12 14]
print(slicearray1[slice(5, 20, 5)]) #print [ 5 10 15]
splitarray = np.arange(9)
print(splitarray) #print [0 1 2 3 4 5 6 7 8]
#the np.split() splits the array at the specificied index numbers
print(np.split(splitarray, 3)) #print [array([0, 1, 2]), array([3, 4, 5]), array([6, 7, 8])]
print(np.split(splitarray, [4,5])) #print [array([0, 1, 2, 3]), array([4]), array([5, 6, 7, 8])]
print(np.split(splitarray, [4,7])) #print [array([0, 1, 2, 3]), array([4, 5, 6]), array([7, 8])]
print(np.split(splitarray, [2,4,6])) #print [array([0, 1]), array([2, 3]), array([4, 5]), array([6, 7, 8])]
splitarray2 = np.arange(10, 21)
#the np.split() splits the array at the specificied index number
print(splitarray2) #print [10 11 12 13 14 15 16 17 18 19 20]
print(np.split(splitarray2, [0, 3])) #print [array([], dtype=int64), array([10, 11, 12]), array([13, 14, 15, 16, 17, 18, 19, 20])]
print(np.split(splitarray2, [3])) #print [array([10, 11, 12]), array([13, 14, 15, 16, 17, 18, 19, 20])]
print(np.split(splitarray2, [3, 6, 9])) #print [array([10, 11, 12]), array([13, 14, 15]), array([16, 17, 18]), array([19, 20])]
print(np.split(splitarray2, [3,7])) #print [array([10, 11, 12]), array([13, 14, 15, 16]), array([17, 18, 19, 20])]
print("\n")

maximumsum = 0
a4horizontal3vertical2dimensionhorizontalsum = a4horizontal3vertical2dimension.sum(axis=1) #Adds each horizontal
print(a4horizontal3vertical2dimensionhorizontalsum) #print [ 6 18 27 36]
for x in range(0,a4horizontal3vertical2dimension.shape[0]):
	tempsum = a4horizontal3vertical2dimensionhorizontalsum[x]
	if tempsum > maximumsum:
		maximumsum = tempsum
print(maximumsum) #print 36
numpymparanthesis = np.array([(3,8),(4,5),(3,8)])
print("paranthesis",numpymparanthesis) #print paranthesis [[3 8]\n [4 5]\n [3 8]]
numpym = np.array([[3,8],[4,5],[3,8]])
print(numpym) #print [[3 8]\n [4 5]\n [3 8]]
print(numpym.sum(axis=0)) #print [10 21].  Adds each vertical column.
print(numpym.sum(axis=1)) #print [11  9 11].  Adds each horizontal rows.
print(numpym.sum(axis=1)[1]) #print 9.  Adds each horizontal rows print the index position one.
numpyn = np.arange(1,11,1)
print(numpyn) #print [ 1  2  3  4  5  6  7  8  9 10]
numpyshuffle = np.random.shuffle(numpyn)
print(numpyshuffle) #print None
numpychoice = np.random.choice(numpyn)  #Randomly chooses one item.
print(numpychoice) #print 2
numpyl = np.array([7,1,4,4,1])
listnumpyl = list(numpyl) #convert numpy to list
print(listnumpyl) #print [7, 1, 4, 4, 1]
#upload file, import text file, import csv file
data = np.loadtxt("data.txt", dtype=np.uint8, delimiter=",", skiprows=1)  #skip the first row because the first row is the header.  Assigned data type dtype=np.uint8 to reduce file size.
print(data) #print [[9 3 8 7 6 1 0 4 2 5]\n [1 7 4 9 2 6 8 3 5 0]\n [4 8 3 9 5 7 2 6 0 1]\n [1 7 4 2 5 9 6 8 0 3]\n [0 7 5 2 8 6 3 4 1 9]\n [5 9 1 4 7 0 3 6 8 2]]
print("\n")

math1 = np.array([(1,2,3), (4,5,6)])
math2 = np.array([(7,8,9), (1,2,3)])
print(math1) #print [[1 2 3]\n [4 5 6]]
print(math2) #print [[7 8 9]\n [1 2 3]]
print(np.vstack((math1, math2)))
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]
 [1 2 3]]
'''
print(np.hstack((math1, math2)))
'''
[[1 2 3 7 8 9]
 [4 5 6 1 2 3]]
'''
print(math1+math2)  #works for subtraction, too
'''
[[ 8 10 12]
 [ 5  7  9]]
'''
print(math1/math2) #works for multiplication, too
'''
[[0.14285714 0.25       0.33333333]
 [4.         2.5        2.        ]]
'''
print(math1//math2) #works for multiplication, too
'''
[[0 0 0]
 [4 2 2]]
'''
print(math1**math2)
'''
[[    1   256 19683]
 [    4    25   216]]
'''
print(math1*10)
'''
[[10 20 30]
 [40 50 60]]
'''
print(math1.ravel()) #print [1 2 3 4 5 6] multi dimension multidimension to one dimension
print(math2.ravel()) #print [7 8 9 1 2 3] multi dimension to single dimension


#String numpy, character numpy
concatenatestringadd = np.char.add(["hello","abc"],["goodbye","xyz"])
print(concatenatestringadd) #print ['hellogoodbye' 'abcxyz']
concatenatestringmultiply = np.char.multiply("Hello ",3)
print(concatenatestringmultiply) #print Hello Hello Hello
concatenatestringcenter = np.char.center("Hello",3,fillchar="-") #print total 3 characters Hello in middle surrounded by hyphens
print(concatenatestringcenter) #print Hel
concatenatestringcenter = np.char.center("Hello",20,fillchar="-") #print total 20 characters Hello in middle surrounded by hyphens
print(concatenatestringcenter) #print -------Hello--------
print(np.char.lower(["HELLO","WORLD"])) #print ['hello' 'world']
print(np.char.lower("HELLO")) #print hello
love = ["HELLO","WORLD","UNIVERSE"]
lovetitle = [(eachlove).title() for eachlove in love]
print(lovetitle) #print ['Hello', 'World', 'Universe']
print(np.char.title(love)) #print ['Hello' 'World' 'Universe']
print(list(np.char.title(love))) #print ['Hello', 'World', 'Universe']
print(np.char.split("are you coming to the party?")) #print ['are', 'you', 'coming', 'to', 'the', 'party?']
print(("are you coming to the party?").split()) #print ['are', 'you', 'coming', 'to', 'the', 'party?']
print(np.char.splitlines("hello\n how are you?")) #print ['hello', ' how are you?']
print(np.char.strip(["nina","admin","anaita", "anona"],"a")) #print ['nin' 'dmin' 'nait' 'non'] removes the first and last "a"
print(np.char.join([":","-","."],["dmy","ymd","period"])) #print ['d:m:y' 'y-m-d' 'p.e.r.i.o.d']
print(np.char.replace("He is a good dancer","is","was")) #print He was a good dancer
indexstringtest = "The quick brown fox jumped over the lazy dog"
print(indexstringtest[11:37]) #print rown fox jumped over the l
print(indexstringtest[11:-7]) #print rown fox jumped over the l
print(indexstringtest[11:37] == indexstringtest[11:-7]) #print True
print(indexstringtest[-33:37]) #print rown fox jumped over the l
blankstringarray = np.empty((4,3), dtype=np.str)
print(blankstringarray)
'''
[['' '' '']
 ['' '' '']
 ['' '' '']
 ['' '' '']]
'''
blankstringarray[0] = "X"
blankstringarray[2:3,1:] =  "Y"
blankstringarray[1,2] =  "Z"
print(blankstringarray)
'''
[['X' 'X' 'X']
 ['' '' 'Z']
 ['' 'Y' 'Y']
 ['' '' '']]
'''
arraymath1 = np.arange(0,9)
print(arraymath1) #print [0 1 2 3 4 5 6 7 8]
arraymath1 = arraymath1.reshape(3,3)
print(arraymath1)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
'''
arraymath2 = np.array([10,11,12])
print(np.add(arraymath1,arraymath2))  #RM:  the shape horizontal must be the same.  arraymath2 = np.array([10, 11]) error message.
'''
[[10 12 14]
 [13 15 17]
 [16 18 20]]
'''
print(np.subtract(arraymath1,arraymath2))  #RM:  the shape horizontal must be the same.  arraymath2 = np.array([10, 11]) error message.
'''
[[-10 -10 -10]
 [ -7  -7  -7]
 [ -4  -4  -4]]
'''
print(np.multiply(arraymath1,arraymath2))  #RM:  the shape horizontal must be the same.  arraymath2 = np.array([10, 11]) error message.
'''
[[ 0 11 24]
 [30 44 60]
 [60 77 96]]
'''
print(np.divide(arraymath1,arraymath2))  #RM:  the shape horizontal must be the same.  arraymath2 = np.array([10, 11]) error message.
'''
[[0.         0.09090909 0.16666667]
 [0.3        0.36363636 0.41666667]
 [0.6        0.63636364 0.66666667]]
'''

print("-------------------------------")
#How to add a new row to an empty numpy array
#https://stackoverflow.com/questions/22392497/how-to-add-a-new-row-to-an-empty-numpy-array
#Given the way numpy arrays work, you are much better building an empty array then putting [in] the data according to one user.  It's much faster to append to a list the convert to a numpy array at the end because you're not using numpy as intended during the loop.
blankarray = np.array([], dtype=np.int16)
counter = 0
numberofrows = 6
for x in range(0,numberofrows):	
	addarray = np.random.randint(0, 20, 5)
	blankarray = np.append(blankarray, addarray, axis=0)	
print(blankarray) #print [19  6 12  6 16 12 12  0  8 15  1 14 11  8 16 19 10  8  0  7 18  5 11 17  3  4  9 15  0 17]
blanklist = []
import random
for x in range(0,numberofrows):
	addlist = [random.randint(0,20) for x in range(0,5)]
	blanklist.append(addlist)
print(blanklist) #print [[8, 20, 4, 20, 6], [0, 9, 5, 1, 0], [12, 20, 3, 6, 14], [4, 4, 20, 16, 19], [9, 18, 10, 10, 14], [20, 6, 11, 9, 11]]
blanklistnp = np.array(blanklist)
print(blanklistnp)
'''
[[ 8 20  4 20  6]
 [ 0  9  5  1  0]
 [12 20  3  6 14]
 [ 4  4 20 16 19]
 [ 9 18 10 10 14]
 [20  6 11  9 11]]
'''
print(blanklistnp.ravel()) #print [ 8 20  4 20  6  0  9  5  1  0 12 20  3  6 14  4  4 20 16 19  9 18 10 10 14 20  6 11  9 11] combine multi dimension to single dimension one dimension
print("\n")

numpyflatten = numpyreshape.flatten() #reference line 25
print(numpyflatten) #print [ 1  3  5  7  9 12]
array8 = numpyflatten.reshape(2,3)
print(array8)
'''
[[ 1  3  5]
 [ 7  9 12]]
'''
numpyflatten2 = array8.flatten(order="F") #C is row major, F is column-major, A is default
print(numpyflatten2) #print [ 1  7  3  9  5 12]
array9 = np.arange(0,12)
print(array9) #print [ 0  1  2  3  4  5  6  7  8  9 10 11]
array9 = array9.reshape(4,3)
print(array9)
'''
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
'''
numpytranspose = np.transpose(array9)
print(numpytranspose)
'''
[[ 0  3  6  9]
 [ 1  4  7 10]
 [ 2  5  8 11]]
'''
array11 = np.arange(8).reshape(2,2,2)  #three dimension array.
print(array11)
'''
[[[0 1]
  [2 3]]

 [[4 5]
  [6 7]]]
'''
iteratearray = np.array([[0,5,10], [15,20,25], [30,35,40]])
print(iteratearray)
'''
[[ 0  5 10]
 [15 20 25]
 [30 35 40]]
'''
for x in iteratearray:
	print(x) #print noting
for x in np.nditer(iteratearray):
	print(x) #print 0\n 5\n 10\n 15\n 20\n 25\n 30\n 35\n 40
for x in np.nditer(iteratearray, order="C"):  #C is row major, F is column-major, A is default
	print(x) #print 0\n 5\n 10\n 15\n 20\n 25\n 30\n 35\n 40
for x in np.nditer(iteratearray, order="F"):  #C is row major, F is column-major, A is default
	print(x) #print 0\n 15\n 30\n 5\n 20\n 35\n 10\n 25\n 40 
for x in np.nditer(iteratearray, order="A"):  #C is row major, F is column-major, A is default
	print(x) #print 0\n 5\n 10\n 15\n 20\n 25\n 30\n 35\n 40
joinarray1 = np.array([[1,2],[3,4]])
joinarray2 = np.array([[5,6],[7,8]])
print(joinarray1)
'''
[[1 2]
 [3 4]]
 '''
print(joinarray2)
'''
[[5 6]
 [7 8]]
'''
joinarray12 = np.concatenate([joinarray1, joinarray2])
print(joinarray12)
'''
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
'''
joinarray12 = np.concatenate([joinarray1, joinarray2], axis=0) #Concatenate dimensions must be the same.  Axis=0 is default.
print(joinarray12)
'''
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
'''
joinarray12 = np.concatenate([joinarray1, joinarray2], axis=1) #Concatenate dimensions must be the same.  horizontal axis=1.
print(joinarray12)
'''
[[1 2 5 6]
 [3 4 7 8]]
'''
