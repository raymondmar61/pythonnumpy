#YouTube edureka
#Numpy is a core library for scientific computing.  It provides a multidimensional array object and tools for arrays.
#Numpy takes less memory, fast, and convenient.
import numpy as np

a4horizontal3vertical2dimension = np.array([(1, 2, 3), (5, 6, 7), (8, 9, 10), (11, 12, 13)])
print(a4horizontal3vertical2dimension)
'''
[[ 1  2  3]
 [ 5  6  7]
 [ 8  9 10]
 [11 12 13]]
'''
print(a4horizontal3vertical2dimension[0,0]) #print 1
print(a4horizontal3vertical2dimension[1,2]) #print 7
print(a4horizontal3vertical2dimension[3,1]) #print 12
maximumsum = 0
for h in range(0,4):
	tempsum = 0
	for v in range(0,3):
		tempsum = tempsum + a4horizontal3vertical2dimension[h,v]
		if tempsum > maximumsum:
			maximumsum = tempsum
print(maximumsum) #print 36
print("\n")

import sys
slist = range(0,1000)
print("memory",sys.getsizeof(slist)*len(slist)) #print memory 48000
snumpy = np.arange(0,1000)
print("memory",snumpy.size*snumpy.itemsize) #print memory 8000

import time
size = 100000
listone = range(size)
listtwo = range(size)
arrayone = np.arange(size)
arraytwo = np.arange(size)
starttimer = time.time()
listresult = [(x+y) for x, y in zip(listone, listtwo)]
#print(listresult) #print [0, 2, 4, ..., 199994, 199996, 199998]
print("timer",(time.time()-starttimer)*1000) #print timer 380.10644912719727
starttimer = time.time()
arrayresult = arrayone + arraytwo
#print(arrayresult) #print [     0      2      4 ..., 199994 199996 199998]
print("timer",(time.time()-starttimer)*1000) #print timer 0.6699562072753906

samplearray = np.array([(1, 2, 3), (2, 3, 4)])
print(samplearray)
'''
[[1 2 3]
 [2 3 4]]
'''
print("dimensional array",samplearray.ndim) #print dimensional array 2
print("memory size array",samplearray.itemsize) #print dimensional array 8
print("type array",samplearray.dtype) #print type array int64
print("number of elements array",samplearray.size) #print number of elements array 6
print("dimension array (rows, columns)",samplearray.shape) #print dimension array (rows, columns) (2, 3)  RM:  one dimension array is (number of elements,*null*)
weirdarray = np.array([(1, 2, 3), (5, 0)])
print(weirdarray) #print [(1, 2, 3) (5, 0)]
print("dimensional array",samplearray.ndim) #print dimensional array 2
print("dimension array (rows, columns)",weirdarray.shape) #print dimension array (rows, columns) (2,)

samplearray2 = np.array([(1, 2, 3, 4),(3, 4, 5, 6)])
print(samplearray2)
'''
[[1 2 3 4]
 [3 4 5 6]]
'''
samplearray2 = samplearray2.reshape(4,2) #reshape dimensions to four rows and two columns
print(samplearray2)
'''
[[1 2]
 [3 4]
 [3 4]
 [5 6]]
'''
samplearray3 = np.array([(1, 2, 3, 4), (3, 4, 5, 6), (7, 8, 9, 10)])
print(samplearray3)
'''
[[ 1  2  3  4]
 [ 3  4  5  6]
 [ 7  8  9 10]]
'''
print("slicing",samplearray3[0,2]) #print slicing 3
print("slicing",samplearray3[0:,3]) #print slicing [4 6 10]
print("slicing",samplearray3[0:2,3]) #print slicing [4 6]
print("slicing",samplearray3[1:,1:3]) #print slicing [[4 5]\n [8 9]]

samplearray4 = np.linspace(1, 3, 5) #one dimension array between 1 and 3 inclusive five elements
print(samplearray4) #print [ 1.   1.5  2.   2.5  3. ]
samplearray4 = np.linspace(1, 3, 10) #one dimension array between 1 and 3 inclusive ten elements
print(samplearray4) #print [ 1.          1.22222222  1.44444444  1.66666667  1.88888889  2.11111111  2.33333333  2.55555556  2.77777778  3.        ]
print("dimensional array",samplearray4.ndim) #print dimensional array 1

matharray = np.array([1, 2, 3])
print("max array value",matharray.max()) #max array value 3
print("min array value",matharray.min()) #min array value 1
print("sum array value",matharray.sum()) #sum array value 6

#Rows are axis 1.  Columns are axis 0
sumaxis = np.array([(1, 2, 3), (3, 4, 5)])
print(sumaxis)
'''
[[1 2 3]
 [3 4 5]]
'''
print(sumaxis.sum(axis=0)) #print [4 6 8]
print(sumaxis.sum(axis=0)[2]) #prin
print(sumaxis.sum(axis=1)) #print [ 6 12]  #RM:  added rows 1+2+3 and 3+4+5
print(sumaxis.sum(axis=1)[0]) #print 6
print(np.sqrt(sumaxis))  #square root
'''
[[ 1.          1.41421356  1.73205081]
 [ 1.73205081  2.          2.23606798]]
'''
print(np.std(sumaxis))  #print 1.29099444874.  Standard deviation.

math1 = np.array([(1, 2, 3), (3, 4, 5)])
math2 = np.array([(1, 2, 3), (3, 4, 5)])
print(math1)
'''
[[1 2 3]
 [3 4 5]]
'''
print(math2)
'''
[[1 2 3]
 [3 4 5]]
'''
print(math1+math2)  #works for subtraction
'''
[[ 2  4  6]
 [ 6  8 10]]
'''
print(math1/math2) #works for multiplication
'''
[[ 1.  1.  1.]
 [ 1.  1.  1.]]
'''
print(np.vstack((math1, math2)))  #vertical concatenate array, combine array
'''
[[1 2 3]
 [3 4 5]
 [1 2 3]
 [3 4 5]]
'''
print(np.hstack((math1, math2)))  #horizontal concatenate array, combine array
'''
[[1 2 3 1 2 3]
 [3 4 5 3 4 5]]
'''
print(math1.ravel())
'''
[1 2 3 3 4 5]
'''
allonedimension = np.array([(1, 2, 3), (5, 4, 3), (5, 9, 2)])
print(allonedimension.ravel())
'''
[1 2 3 5 4 3 5 9 2]
'''

import matplotlib.pyplot as plt
x = np.arange(0,3*np.pi, 0.1)
y = np.sin(x)
#plt.plot(x,y)
#plt.show()
ar = np.array([1, 2, 3])
print(np.exp(ar))  #print [  2.71828183   7.3890561   20.08553692].  Calculate exponential value e^x
naturallog = np.log(ar)
print(naturallog)  #print [ 0.          0.69314718  1.09861229].  Calculate natural log
naturallog10 = np.log10(ar)
print(naturallog10)  #print [ 0.          0.30103     0.47712125].  Calculate based 10 log
