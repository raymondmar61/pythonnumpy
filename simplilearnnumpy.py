#www.Simplilearn.com
#Numpy is the core library for scientific and numerical computing in python.  It provides high-performance multidimensional array objects and tools for working with arrays.
#There are modules built on Numpy.
#Input a list in Numpy.  Multi-dimension numpy array contained in paranthesis ([(array1), (array2), ...])
#Numpy array is fast, convenient, and less memory compared to Python list.
#Dimensions are also called axis.
#F stands for Fortran
import numpy as np

#Part One
onedimensionalarray = np.array([1, 2, 3, 4, 5, 6, 7])
twodimensionalarray = np.array([(0, 1, 2, 3), (4, 5, 6, 7)])
print(onedimensionalarray) #print [1 2 3 4 5 6 7]
print(onedimensionalarray.shape) #print (7,) #seven horizontal
print(twodimensionalarray) #print [[0 1 2 3]\n [4 5 6 7]]
print(twodimensionalarray.shape) #print (2, 4) #two veritcal, four horizontal
print(onedimensionalarray[1]) #print 2

import sys
b = range(0,1000)
print("Memory size",sys.getsizeof(5)*len(b)) #print Memory size 28000
c = np.arange(0, 1000)
print("Memory size",c.itemsize*c.size) #print Memory size 8000
import time
size = 100000
list1 = range(0, size)
list2 = range(0, size)
startlist1list2 = time.time()
sumlist1list2 = [(x+y) for x, y in zip(list1, list2)]  #Combines list1 and list2 to one list, add each index, return sum in list comprehension sumlist1list2; e.g. if size = 10, then sumlist1list2 is [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print("Python list sumlist1list2 took", (time.time() - startlist1list2)*100000) #print Python list sumlist1list2 took 3026.3185501098633
array1 = np.arange(0, size)
array2 = np.arange(0, size)
startarray1array2 = time.time()
sumarray1array2 = array1 + array2
print(sumarray1array2)  #print [     0      2      4 ..., 199994 199996 199998]
print("Python array sumarray1array2 took", (time.time() - startarray1array2)*100000) #print Python array sumarray1array2 took 66.61415100097656
array3 = np.array([(1, 2), (3, 4), (5, 6)])
print(array3)
'''
[[1 2]
 [3 4]
 [5 6]]
'''
array3 = np.array([[1, 2], [3, 4], [5, 6]])
print(array3)
'''
[[1 2]
 [3 4]
 [5 6]]
'''
print("Dimensions",array3.ndim) #print Dimensions 2
print("Memory Item size",array3.itemsize) #print Memory Item size 8
print("Data type",array3.dtype) #print Data type int64
print("Shape (up down vertical, left right horizontal)",array3.shape) #print Shape (up down vertical, left right horizontal) (3, 2)
array4 = np.array([[1, 2], [3, 4], [5, 6]], dtype=np.float64) #Changed data type to float
print(array4)
'''
[[ 1.  2.]
 [ 3.  4.]
 [ 5.  6.]]
'''
array5 = np.array([[1, 2], [3, 4], [5, 6]], dtype=np.complex) #Changed data type to complex
print(array5)
'''
[[ 1.+0.j  2.+0.j]
 [ 3.+0.j  4.+0.j]
 [ 5.+0.j  6.+0.j]]
'''
zerosarray = np.zeros((3,4))
print(zerosarray)
'''
[[ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]]
'''
print("Dimensions",zerosarray.ndim) #print Dimensions 2
zerosarray = np.zeros((3,4), dtype=np.int)
print(zerosarray)
'''
[[0 0 0 0]
 [0 0 0 0]
 [0 0 0 0]]
'''
print("Data type",zerosarray.dtype) #print Data type int64
onesarray = np.ones((3,4))
print(onesarray)
'''
[[ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]]
'''
print(np.arange(0,5)) #print [0 1 2 3 4]
zerotofive = np.arange(0,5)
print(zerotofive) #print [0 1 2 3 4]
zerotofivelist = list(zerotofive)
print(zerotofivelist) #print [0, 1, 2, 3, 4]
print(type(zerotofivelist)) #print <class 'list'>
zerotofivelist = [x for x in range(0,5)]
print(zerotofivelist) #print [0, 1, 2, 3, 4]
print(type(zerotofivelist)) #print <class 'list'>

concatenatestringadd = np.char.add(["hello","hi"],["abc","xyz"])
print(concatenatestringadd) #print ['helloabc' 'hixyz']
concatenatestringmultiply = np.char.multiply("Hello",3)
print(concatenatestringmultiply) #print HelloHelloHello
concatenatestringcenter = np.char.center("Hello",3,fillchar="-") #print total 3 characters Hello in middle surrounded by hyphens
print(concatenatestringcenter) #print Hel
concatenatestringcenter = np.char.center("Hello",20,fillchar="-") #print total 20 characters Hello in middle surrounded by hyphens
print(concatenatestringcenter) #print -------Hello--------
#more np.char. fill, capatalize, title, lowercase, uppercase, split, split lines, strip, join
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

#Part Two
array6 = np.arange(9)
print(array6) #print [0 1 2 3 4 5 6 7 8]
array7 = array6.reshape(3,3)
print(array7)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
 '''
print("array7 dimensions",array7.ndim) #print array7 dimensions 2
#RM:  array7 = array6.reshape(4,2) is ValueError: cannot reshape array of size 9 into shape (4,2)
array7 = array7.flatten()
print(array7) #print [0 1 2 3 4 5 6 7 8]
array8 = array7.reshape(3,3)
print(array8)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
'''
array8 = array8.flatten(order="F")  #C is row major, F is column-major, A is default
print(array8) #print [0 3 6 1 4 7 2 5 8]
array9 = np.arange(12).reshape(4,3)  #Four vertical four down, three horizontal three across
print(array9)
'''
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
'''
array9 = np.transpose(array9)
print(array9)
'''
[[ 0  3  6  9]
 [ 1  4  7 10]
 [ 2  5  8 11]]
'''
print(list(array9)) #print [array([0, 3, 6, 9]), array([ 1,  4,  7, 10]), array([ 2,  5,  8, 11])]
print(list(array6)) #print [0, 1, 2, 3, 4, 5, 6, 7, 8]
array10 = np.arange(1,9).reshape(2,4)
print(array10)
'''
[[1 2 3 4]
 [5 6 7 8]]
'''
array11 = np.arange(8).reshape(2,2,2)
print(array11)
'''
[[[0 1]
  [2 3]]

 [[4 5]
  [6 7]]]
'''
print("array 11 dimensions",array11.ndim) #print array 11 dimensions 3
print(np.rollaxis(array11,2))
'''
[[[0 2]
  [4 6]]

 [[1 3]
  [5 7]]]
'''
print(np.rollaxis(array11,2,1))
'''
[[[0 2]
  [1 3]]

 [[4 6]
  [5 7]]]
'''
print(np.swapaxes(array11,1,2))
'''
[[[0 2]
  [1 3]]

 [[4 6]
  [5 7]]]
'''
print("\n")

arraymath1 = np.arange(9).reshape(3,3)
print(arraymath1)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
'''
arraymath2 = np.array([10, 11, 12])
print(np.add(arraymath1, arraymath2))  #RM:  the shape horizontal must be the same.  arraymath2 = np.array([10, 11]) error message.
'''
[[10 12 14]
 [13 15 17]
 [16 18 20]]
'''
print(np.subtract(arraymath1, arraymath2))  #RM:  the shape horizontal must be the same.  arraymath2 = np.array([10, 11]) error message.
'''
[[-10 -10 -10]
 [ -7  -7  -7]
 [ -4  -4  -4]]
'''
#RM:  np.multiply() and np.divide() exists
print("\n")

slicearray1 = np.arange(20)
print(slicearray1) #print [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
print(slicearray1[5]) #print 5
print(slicearray1[4:]) #print [ 4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
print(slicearray1[:4]) #print [0 1 2 3]
print(slicearray1[slice(2, 9, 2)]) #print [2 4 6 8]
print(slicearray1[slice(3, 15, 2)]) #print [ 3  5  7  9 11 13]  #RM: slice is slice(inclusive, exclusive, step rate) like range, arange.
print(slicearray1[slice(4, 16, 3)]) #print [ 4  7 10 13]

iteratearray = np.arange(0, 45, 5)
print(iteratearray) #print [ 0  5 10 15 20 25 30 35 40]
print(iteratearray.reshape(3,3))
'''
[[ 0  5 10]
 [15 20 25]
 [30 35 40]]
'''
for x in np.nditer(iteratearray):
	print(x) #print 0\n 5\n 10\n 15\n 20\n 25\n 30\n 35\n 40
for x in iteratearray:
	print(x) #print 0\n 5\n 10\n 15\n 20\n 25\n 30\n 35\n 40
for x in np.nditer(iteratearray, order="C"):
	print(x) #print 0\n 5\n 10\n 15\n 20\n 25\n 30\n 35\n 40
for x in np.nditer(iteratearray, order="F"):
	print(x) #print 0\n 5\n 10\n 15\n 20\n 25\n 30\n 35\n 40.  Instructor says 0\n 15\n 30\n 5\n 20\n 35\n 10\n 25\n 40 should be the answer.

joinarray1 = np.array([[1, 2], [3, 4]])
print(joinarray1)
'''
[[1 2]
 [3 4]]
 '''
joinarray2 = np.array([[5, 6], [7, 8]])
print(joinarray2)
'''
[[5 6]
 [7 8]]
'''
joinarray12 = np.concatenate([joinarray1, joinarray2]) #brackets.  Concatenate dimensions must be the same.
print(joinarray12)
'''
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
'''
joinarray12 = np.concatenate((joinarray1, joinarray2), axis=0) #paranthesis.  Concatenate dimensions must be the same.  #concatenate numpy arrays vertical axis = 0 which is default p.concatenate((joinarray1, joinarray2), axis = 0) 
print(joinarray12)
'''
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
'''
print(joinarray12.ndim) #print 2.  Two dimension array  RM:  4x2 four vertical two horizontal
joinarray12axis1 = np.concatenate((joinarray1,joinarray2), axis=1)  #concatenate numpy arrays horizontal axis=1
print(joinarray12axis1)
'''
[[1 2 5 6]
 [3 4 7 8]]
'''

splitarray = np.arange(9)
print(splitarray) #print [0 1 2 3 4 5 6 7 8]
#the np.split() splits the array at the specificied index numbers
print(np.split(splitarray, 3)) #print [array([0, 1, 2]), array([3, 4, 5]), array([6, 7, 8])]
print(np.split(splitarray, [4,5])) #print [array([0, 1, 2, 3]), array([4]), array([5, 6, 7, 8])]
print(np.split(splitarray, [4,7])) #print [array([0, 1, 2, 3]), array([4, 5, 6]), array([7, 8])]
print(np.split(splitarray, [2,4,6])) #print [array([0, 1]), array([2, 3]), array([4, 5]), array([6, 7, 8])]
splitarray2 = np.arange(10, 21)
print(splitarray2) #print [10 11 12 13 14 15 16 17 18 19 20]
print(np.split(splitarray2, [0, 3])) #print [array([], dtype=int64), array([10, 11, 12]), array([13, 14, 15, 16, 17, 18, 19, 20])]
print(np.split(splitarray2, [3])) #print [array([10, 11, 12]), array([13, 14, 15, 16, 17, 18, 19, 20])]
print(np.split(splitarray2, [3,7])) #print [array([10, 11, 12]), array([13, 14, 15, 16]), array([17, 18, 19, 20])]

resizearray = np.array([[1, 2, 3], [4, 5, 6]])
print(resizearray)
'''
[[1 2 3]
 [4 5 6]]
'''
print(resizearray.shape) #print (2, 3)
resizearray2 = np.resize(resizearray, (3,2))
print(resizearray2)
'''
[[1 2]
 [3 4]
 [5 6]]
 '''
print(resizearray2.shape) #print (3, 2)
#resize doesn't have to match dimensions.  resize doesn't have to resize to same shape.  Numpy repeats to fill in blanks in unmatched dimensions rows and columns.
resizearray3 = np.resize(resizearray, (3,3))
print(resizearray3)
'''
[[1 2 3]
 [4 5 6]
 [1 2 3]]
'''

from matplotlib import pyplot as plt
histogramarray = np.array([20, 87, 4, 40, 53, 74, 56, 51, 11, 20, 40, 15, 79, 25, 27])
#plt.hist(histogramarray, bins = [0, 20, 40, 60, 80, 100])
#plt.title("histogram bins low end inclusive high end exclusive")
plt.show()

linspacearray = np.linspace(1, 3, 10)  #10 entries spread out between 1 and 3
print(linspacearray)
'''
[ 1.          1.22222222  1.44444444  1.66666667  1.88888889  2.11111111
  2.33333333  2.55555556  2.77777778  3.        ]
'''

sumaxis = np.array([(1,2,3),(4,5,6)]) #use brackets
print(sumaxis)
'''
[[1 2 3]
 [4 5 6]]
'''
print(sumaxis.sum(axis=0)) #print [5 7 9].  axix=0 vertical
print(sumaxis.sum(axis=1)) #print [6 15].  axis=1 horizontal
sumaxis = np.array(((1,2,3),(4,5,6))) #use paranthesis
print(sumaxis)
'''
[[1 2 3]
 [4 5 6]]
'''
print(sumaxis.sum(axis=0)) #print [5 7 9].  axix=0 vertical
print(sumaxis.sum(axis=1)) #print [6 15].  axis=1 horizontal
print(np.sqrt(sumaxis))
'''
[[ 1.          1.41421356  1.73205081]
 [ 2.          2.23606798  2.44948974]]
'''
print(np.std(sumaxis)) #print 1.70782512766
print(np.log10(sumaxis)) #RM:  np.log2() is available
'''
[[ 0.          0.30103     0.47712125]
 [ 0.60205999  0.69897     0.77815125]]
'''

ravelarray = np.array(((1,2,3),(3,4,5)))
print(ravelarray)
'''
[[1 2 3]
 [3 4 5]]
'''
print(ravelarray.ravel()) #print [1 2 3 3 4 5]

x = np.arange(0, 3*np.pi, 0.1)
print(x)
'''[ 0.   0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1.   1.1  1.2  1.3  1.4
  1.5  1.6  1.7  1.8  1.9  2.   2.1  2.2  2.3  2.4  2.5  2.6  2.7  2.8  2.9
  3.   3.1  3.2  3.3  3.4  3.5  3.6  3.7  3.8  3.9  4.   4.1  4.2  4.3  4.4
  4.5  4.6  4.7  4.8  4.9  5.   5.1  5.2  5.3  5.4  5.5  5.6  5.7  5.8  5.9
  6.   6.1  6.2  6.3  6.4  6.5  6.6  6.7  6.8  6.9  7.   7.1  7.2  7.3  7.4
  7.5  7.6  7.7  7.8  7.9  8.   8.1  8.2  8.3  8.4  8.5  8.6  8.7  8.8  8.9
  9.   9.1  9.2  9.3  9.4]
'''
y = np.sin(x)
print(y)
'''
[ 0.          0.09983342  0.19866933  0.29552021  0.38941834  0.47942554
  0.56464247  0.64421769  0.71735609  0.78332691  0.84147098  0.89120736
  0.93203909  0.96355819  0.98544973  0.99749499  0.9995736   0.99166481
  0.97384763  0.94630009  0.90929743  0.86320937  0.8084964   0.74570521
  0.67546318  0.59847214  0.51550137  0.42737988  0.33498815  0.23924933
  0.14112001  0.04158066 -0.05837414 -0.15774569 -0.2555411  -0.35078323
 -0.44252044 -0.52983614 -0.61185789 -0.68776616 -0.7568025  -0.81827711
 -0.87157577 -0.91616594 -0.95160207 -0.97753012 -0.993691   -0.99992326
 -0.99616461 -0.98245261 -0.95892427 -0.92581468 -0.88345466 -0.83226744
 -0.77276449 -0.70554033 -0.63126664 -0.55068554 -0.46460218 -0.37387666
 -0.2794155  -0.1821625  -0.0830894   0.0168139   0.1165492   0.21511999
  0.31154136  0.40484992  0.49411335  0.57843976  0.6569866   0.72896904
  0.79366786  0.85043662  0.8987081   0.93799998  0.96791967  0.98816823
  0.99854335  0.99894134  0.98935825  0.96988981  0.94073056  0.90217183
  0.85459891  0.79848711  0.7343971   0.66296923  0.58491719  0.50102086
  0.41211849  0.31909836  0.22288991  0.12445442  0.02477543]
'''
#plt.plot(x, y)
plt.show()

#Create a 6x6 two-dimensional array.  Let 1 and 0 be placed alternatively across the diagonals.
z = np.zeros((6,6), dtype=int)
print(z)
'''
[[0 0 0 0 0 0]
 [0 0 0 0 0 0]
 [0 0 0 0 0 0]
 [0 0 0 0 0 0]
 [0 0 0 0 0 0]
 [0 0 0 0 0 0]]
'''
z[1::2,::2] = 1  #index numbers row 1, row 3, row 5, column 0, column 2, column 4
print(z)
'''
[[0 0 0 0 0 0]
 [1 0 1 0 1 0]
 [0 0 0 0 0 0]
 [1 0 1 0 1 0]
 [0 0 0 0 0 0]
 [1 0 1 0 1 0]]
'''
z[::2,1::2] = 1  #correct answer
print(z)
'''
[[0 1 0 1 0 1]
 [1 0 1 0 1 0]
 [0 1 0 1 0 1]
 [1 0 1 0 1 0]
 [0 1 0 1 0 1]
 [1 0 1 0 1 0]]
'''

randarray = np.random.rand(5)
print(randarray) #print [ 0.64958353  0.03773217  0.53263131  0.23208422  0.27703224]
randarray = np.random.rand(5,5)
print(randarray)
'''
[[ 0.04713012  0.6707242   0.33266207  0.09448784  0.42024965]
 [ 0.4538742   0.9504008   0.07942731  0.13128486  0.08118823]
 [ 0.74576798  0.79382724  0.44226393  0.20710587  0.95821454]
 [ 0.23794432  0.87994923  0.01522441  0.20978884  0.17744174]
 [ 0.10161611  0.60451787  0.271606    0.81648601  0.80088508]]
'''
randintarray = np.random.randint(30, 51)
print(randintarray) #print 33
randintarraycorrect = np.random.randint(30, 51, size=10)
print(randintarraycorrect) #print [39 37 35 46 46 45 41 35 37 41]
randintarraycorrect2d = [np.random.randint(30, 51, size=10), np.random.randint(30, 51, size=10)]
print(randintarraycorrect2d) #print [array([31, 41, 40, 45, 31, 50, 32, 34, 40, 36]), array([49, 31, 42, 50, 36, 35, 45, 30, 48, 42])]
randintarraycorrect = np.random.randint(30, 51, size=100)
print(randintarraycorrect)
'''
[45 45 41 48 42 47 38 47 44 31 42 36 40 41 42 50 41 48 44 44 30 36 33 38 33
 37 33 34 43 32 43 37 32 34 31 42 41 33 33 43 31 41 50 42 50 38 43 42 42 48
 36 33 46 33 32 32 30 48 46 32 32 41 39 32 46 40 48 39 42 36 35 31 39 36 49
 40 33 40 40 45 34 40 49 37 40 33 37 39 44 38 35 43 31 37 31 42 40 37 39 50]
'''
print(randintarraycorrect.reshape(10,10))
'''
[[45 45 41 48 42 47 38 47 44 31]
 [42 36 40 41 42 50 41 48 44 44]
 [30 36 33 38 33 37 33 34 43 32]
 [43 37 32 34 31 42 41 33 33 43]
 [31 41 50 42 50 38 43 42 42 48]
 [36 33 46 33 32 32 30 48 46 32]
 [32 41 39 32 46 40 48 39 42 36]
 [35 31 39 36 49 40 33 40 40 45]
 [34 40 49 37 40 33 37 39 44 38]
 [35 43 31 37 31 42 40 37 39 50]]
'''

#Find the total number and locations of missing values in the array
z = np.random.rand(10,10)
print(z)
'''
[[ 0.59878084  0.70795173  0.34923194  0.41205698  0.46482485  0.78564278
   0.48988541  0.27912327  0.58658696  0.23286221]
 [ 0.34144974  0.26447672  0.29367589  0.01836301  0.98551402  0.38510778
   0.23076437  0.0514859   0.54356891  0.62144944]
 [ 0.71291743  0.45985399  0.26867731  0.7383616   0.752577    0.81022574
   0.23971014  0.6346461   0.77069208  0.76225772]
 [ 0.50044344  0.963673    0.77720183  0.51974305  0.28583125  0.51795509
   0.96029214  0.88369066  0.44197529  0.20392634]
 [ 0.2482179   0.42537316  0.69972105  0.51433383  0.85641182  0.98299004
   0.54506864  0.08198672  0.08024709  0.05944878]
 [ 0.09155386  0.55058041  0.82500727  0.8566419   0.46603914  0.96204524
   0.39357442  0.32448052  0.50896432  0.6602082 ]
 [ 0.60380848  0.90777534  0.49357616  0.471787    0.73631562  0.61894922
   0.84022153  0.85241031  0.89236462  0.70373053]
 [ 0.21581809  0.79099886  0.81159087  0.61344902  0.01186247  0.42940537
   0.38354326  0.49868436  0.86919787  0.61312766]
 [ 0.69475257  0.11321312  0.52261304  0.31443464  0.60354091  0.85115771
   0.55435218  0.28554545  0.10747033  0.01268598]
 [ 0.95819347  0.3018214   0.81763453  0.86113767  0.99341231  0.16177605
   0.94563178  0.17229475  0.48550591  0.05101744]]
'''
z[np.random.randint(0, 10, size=5), np.random.randint(0, 10, size=5)] = np.nan
nanindexes = np.where(np.isnan(z))
print(nanindexes) #print (array([2, 3, 5, 7, 9]), array([6, 1, 0, 0, 2]))
print(z)
'''
[[ 0.59878084  0.70795173  0.34923194  0.41205698  0.46482485  0.78564278
   0.48988541  0.27912327  0.58658696  0.23286221]
 [ 0.34144974  0.26447672  0.29367589  0.01836301  0.98551402  0.38510778
   0.23076437  0.0514859   0.54356891  0.62144944]
 [ 0.71291743  0.45985399  0.26867731  0.7383616   0.752577    0.81022574
          nan  0.6346461   0.77069208  0.76225772]
 [ 0.50044344         nan  0.77720183  0.51974305  0.28583125  0.51795509
   0.96029214  0.88369066  0.44197529  0.20392634]
 [ 0.2482179   0.42537316  0.69972105  0.51433383  0.85641182  0.98299004
   0.54506864  0.08198672  0.08024709  0.05944878]
 [        nan  0.55058041  0.82500727  0.8566419   0.46603914  0.96204524
   0.39357442  0.32448052  0.50896432  0.6602082 ]
 [ 0.60380848  0.90777534  0.49357616  0.471787    0.73631562  0.61894922
   0.84022153  0.85241031  0.89236462  0.70373053]
 [        nan  0.79099886  0.81159087  0.61344902  0.01186247  0.42940537
   0.38354326  0.49868436  0.86919787  0.61312766]
 [ 0.69475257  0.11321312  0.52261304  0.31443464  0.60354091  0.85115771
   0.55435218  0.28554545  0.10747033  0.01268598]
 [ 0.95819347  0.3018214          nan  0.86113767  0.99341231  0.16177605
   0.94563178  0.17229475  0.48550591  0.05101744]]
'''
print("Total number of missing values: ", np.isnan(z).sum())  #print Total number of missing values:  5
print("Indexes of missing values: ",np.argwhere(np.isnan(z)))
'''
Indexes of missing values:  [[2 6]
 [3 1]
 [5 0]
 [7 0]
 [9 2]]
'''
z = np.random.rand(10,10)
print(z)
'''
[[ 0.67470328  0.63154803  0.55338863  0.29069414  0.98947609  0.24907996
   0.44546211  0.85741596  0.06932815  0.79880991]
 [ 0.04488679  0.69865113  0.88078435  0.61764152  0.64747535  0.67320335
   0.66013188  0.79677345  0.78174116  0.19932967]
 [ 0.04166278  0.3722487   0.45106484  0.24501572  0.52984929  0.71939085
   0.80215551  0.6524967   0.89059766  0.77036583]
 [ 0.42652618  0.71488425  0.42615102  0.86833073  0.70649644  0.53543068
   0.53901429  0.75431409  0.92577445  0.36802313]
 [ 0.59826387  0.21954109  0.68746963  0.67547858  0.03631242  0.52695285
   0.78365797  0.22178394  0.68009181  0.46694177]
 [ 0.26502549  0.68922762  0.51417598  0.57392392  0.92802265  0.50971515
   0.0283386   0.48604257  0.4548957   0.85936953]
 [ 0.36008994  0.79765079  0.71954584  0.1825044   0.72087651  0.43820197
   0.71211712  0.81184295  0.32378285  0.99849482]
 [ 0.19769034  0.34642582  0.66175455  0.35085037  0.08360257  0.45242688
   0.63297204  0.7420574   0.64021655  0.38268965]
 [ 0.88117704  0.30711008  0.9962016   0.90721101  0.50068771  0.339076
   0.60196952  0.70685849  0.57878192  0.60079239]
 [ 0.18805194  0.16046852  0.29215498  0.56589376  0.33230673  0.80261347
   0.60300112  0.19926101  0.83403874  0.868276  ]]
'''
z[np.random.randint(0, 10, size=5), np.random.randint(0, 10, size=5)] = np.nan
nanindexes = np.where(np.isnan(z))
print(nanindexes) #print (array([1, 1, 5, 6, 8]), array([1, 9, 2, 3, 1]))
z[nanindexes] = 0
print(z)
'''
[[ 0.67470328  0.63154803  0.55338863  0.29069414  0.98947609  0.24907996
   0.44546211  0.85741596  0.06932815  0.79880991]
 [ 0.04488679  0.          0.88078435  0.61764152  0.64747535  0.67320335
   0.66013188  0.79677345  0.78174116  0.        ]
 [ 0.04166278  0.3722487   0.45106484  0.24501572  0.52984929  0.71939085
   0.80215551  0.6524967   0.89059766  0.77036583]
 [ 0.42652618  0.71488425  0.42615102  0.86833073  0.70649644  0.53543068
   0.53901429  0.75431409  0.92577445  0.36802313]
 [ 0.59826387  0.21954109  0.68746963  0.67547858  0.03631242  0.52695285
   0.78365797  0.22178394  0.68009181  0.46694177]
 [ 0.26502549  0.68922762  0.          0.57392392  0.92802265  0.50971515
   0.0283386   0.48604257  0.4548957   0.85936953]
 [ 0.36008994  0.79765079  0.71954584  0.          0.72087651  0.43820197
   0.71211712  0.81184295  0.32378285  0.99849482]
 [ 0.19769034  0.34642582  0.66175455  0.35085037  0.08360257  0.45242688
   0.63297204  0.7420574   0.64021655  0.38268965]
 [ 0.88117704  0.          0.9962016   0.90721101  0.50068771  0.339076
   0.60196952  0.70685849  0.57878192  0.60079239]
 [ 0.18805194  0.16046852  0.29215498  0.56589376  0.33230673  0.80261347
   0.60300112  0.19926101  0.83403874  0.868276  ]]
'''

"""
numbers = np.array([[1,2,3],[10, 20, 30],[100, 200, 300]])
print(numbers)
'''
[[  1   2   3]
 [ 10  20  30]
 [100 200 300]]
'''
#print(numbers[0,2]) #print 3
for x in range(0,3):
	for y in range(0,3):
		print(x,y)
		print(x+1, y)
		print(x+2, y)
		print(numbers[x,y]+numbers[x+1,y]+numbers[x+2,y])
		# y = x + 1 
		# print(numbers[x,y]+numbers[x+1,y]+numbers[x+2,y])
		# y = x - 1
		# print(numbers[x,y]+numbers[x+1,y]+numbers[x+2,y])
"""

#How to add a new row to an empty numpy array
#https://stackoverflow.com/questions/22392497/how-to-add-a-new-row-to-an-empty-numpy-array
#Given the way numpy arrays work, you are much better building an empty array then putting [in] the data according to one user.  It's much faster to append to a list the convert to a numpy array at the end because you're not using numpy as intended during the loop.
addarray = np.array([], dtype=np.int64)
addarray = np.append(addarray, np.array([1,2,3]))
print(addarray) #print [1 2 3]
addarray = np.append(addarray, np.array([4,5,6]))
print(addarray) #print [1 2 3 4 5 6]
emptyaddarray = np.empty((0,3), dtype=np.int64)
print(emptyaddarray) #print []
emptyaddarray = np.append(emptyaddarray, np.array([[1,2,3]]), axis=0)
print(emptyaddarray) #print [[1 2 3]]
emptyaddarray = np.append(emptyaddarray, np.array([[4,5,6]]), axis=0)
print(emptyaddarray) #print [[1 2 3]\n [4 5 6]]
addarray = []
addarray.append([1,2,3])
addarray.append([4,5,6])
print(addarray) #print [[1, 2, 3], [4, 5, 6]]
npaddarray = np.array(addarray)
print(npaddarray) #print [[1 2 3]\n [4 5 6]]
addarray = np.array([], dtype=np.int64)
addarray = np.hstack((addarray, np.array([1,2,3])))
print(addarray) #print [1 2 3]
addarray = np.vstack((addarray, np.array([4,5,6])))
print(addarray)
'''
[[1 2 3]
 [4 5 6]]
'''
addarray = np.vstack((addarray, np.array([7,8,9])))
print(addarray)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''
#addarray = np.hstack((addarray, np.array([10,11,12])))
#print(addarray)  #print ValueError: all the input arrays must have same number of dimensions

#Python Matrix And Introduction to Numpy
#https://www.programiz.com/python-programming/matrix#numpy
anumpy = np.array([[1, 4, 5, 12], [-5, 8, 9, 0], [-6, -7, 11, 19]])
print(anumpy)
'''
[[ 1  4  5 12]
 [-5  8  9  0]
 [-6 -7 11 19]]
'''
print(anumpy[1]) #print [-5  8  9  0]
print(anumpy[1,0]) #print -5
print(anumpy[1][0]) #print -5
print(anumpy[0,2]) #print 5
print(anumpy[0][2]) #print 5
print(anumpy[:,1]) #print [ 4  8 -7]
print(anumpy[2,3]) #print 19
print(anumpy[2][3]) #print 19
print(anumpy[-1][-3]) #print -7
print(anumpy[0][1:3]) #print [4 5]
print(anumpy[1][0:2]) #print [-5  8]
print(anumpy[1][-1:]) #print [0]
print(anumpy[1][-1:-3]) #print []
print(anumpy[1][-3:]) #print [8 9 0]
print(anumpy[1][-1::-1]) #print [ 0  9  8 -5]
print(anumpy[:2, :3])
'''
[[ 1  4  5]
 [-5  8  9]]
'''
print(anumpy[:1,]) #print [[ 1  4  5 12]]
print(anumpy[:,2]) #print [ 5  9 11]
print(anumpy[:,2:4])
'''
[[ 5 12]
 [ 9  0]
 [11 19]]
'''
complexnumpy = np.array([[1,2,3],[4,5,6]], dtype=np.complex)
print(complexnumpy)
'''
[[ 1.+0.j  2.+0.j  3.+0.j]
 [ 4.+0.j  5.+0.j  6.+0.j]]
'''
a = np.array([[2,4], [5,-6]])
b = np.array([[9,-3], [3,6]])
c = a + b
print(c)
'''
[[11  1]
 [ 8  0]]
'''
c = a * b
print(c)
'''
[[ 18 -12]
 [ 15 -36]]
'''
atranspose = np.array([[1,1], [2,5], [3,-3]])
print(atranspose)
'''
[[ 1  1]
 [ 2  5]
 [ 3 -3]]
'''
print(atranspose.transpose())
'''
[[ 1  2  3]
 [ 1  5 -3]]
'''

#https://www.tutorialspoint.com/numpy/numpy_dot.htm#
#This function returns the dot product of two arrays. For 2-D vectors, it is the equivalent to matrix multiplication. For 1-D arrays, it is the inner product of the vectors. For N-dimensional arrays, it is a sum product over the last axis of a and the second-last axis of b.
a = np.array([[1,2],[3,4]]) 
b = np.array([[11,12],[13,14]])
print(a)
print(b)
'''
[[1 2]
 [3 4]]
[[11 12]
 [13 14]]
'''
c = np.dot(a,b)
print(c)
'''
[[37 40]
 [85 92]]
'''
#The dot product is [[1*11+2*13, 1*12+2*14],[3*11+4*13, 3*12+4*14]]
#RM:  I can't figure it out