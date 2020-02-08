#Complete Python NumPy Tutorial (Creating Arrays, Indexing, Math, Statistics, Reshaping) [720p]
#keithgalli
#NumPy is a multi-dimensional array library.  One dimensional array shape(4,) four across or four columns.  Two dimensional array shape(2,3) two down, three across or two rows, three columns.  Three dimensional array shape(4,3,2) four down, three towards you, two away.
#Lists and Numpy both insert, delete, append, concatenate, etc.  Numpy does lots more.  e.g., a=[1,3,5] b=[1,2,3] a*b=error.  a=np.array([1,3,5]) b=np.array([1,2,3]) a*b=np.array([1,6,15])
#NumPy applications:  MATLAB replacement, plotting (Matplotlib), Backend (Pandas, Connect 4, Digital Photography store images), Machine Learning.
import numpy as np

a = np.array([1,2,3])
print(a) #print [1 2 3]
b = np.array([[9.0,8.0,7.0],[6.0, 5.0, 4.0]])
print(b)
'''
[[ 9.  8.  7.]
 [ 6.  5.  4.]]
'''
#number of dimensions
print(a.ndim) #print 1
print(b.ndim) #print 2
#numpy array shape count rows count columns
print(a.shape) #print (3,)
print(b.shape) #print (2, 3)
#numpy number of elements
print(a.size) #print 3
print(b.size) #print 6
#get data type
print(a.dtype) #print int64
print(b.dtype) #print float64
#array size, array memory size
print(a.itemsize) #print 8.  Memory size each item.
print(a.size) #print 3.  Total number of elements.
print(a.nbytes) #print 24.  Total memory size or itemsize*size.
print(b.itemsize) #print 8.  Memory size each item.
print(b.size) #print 6.  Total number of elements.
print(b.nbytes) #print 48.  Total memory size or itemsize*size.
#assign data type.  Reduce memory size for integers.
a2 = np.array([1,2,3], dtype=np.int16)
print(a2.dtype) #print int16
print("\n")

#slicing
a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
print(a)
'''
[[ 1  2  3  4  5  6  7]
 [ 8  9 10 11 12 13 14]]
'''
print(a.shape) #print (2, 7)
print(a[1,5]) #print 13
print(a[1,-2]) #print 13
print(a[0]) #print [1 2 3 4 5 6 7]
print(a[0,:]) #print [1 2 3 4 5 6 7]
print(a[0:,2]) #print [ 3 10]
print(a[:,2]) #print [ 3 10]
print(a[0,1:6:2]) #print [2 4 6].  Skip elements in a row.  Row zero.  Start index one.  End index five.  Skip one element or include every other element.
print(a[0,1:-1:2]) #print [2 4 6].  Skip elements in a row.  Row zero.  Start index one.  End index five.  Skip one element or include every other element.

#updating, editing, change
a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
print(a)
'''
[[ 1  2  3  4  5  6  7]
 [ 8  9 10 11 12 13 14]]
'''
a[1,5] = 20
print(a)
'''
[[ 1  2  3  4  5  6  7]
 [ 8  9 10 11 12 20 14]]
'''
a[0:,2] = 5
print(a)
'''
[[ 1  2  5  4  5  6  7]
 [ 8  9  5 11 12 20 14]]
'''
a[0:,2] = [100, 200]
print(a)
'''
[[  1   2 100   4   5   6   7]
 [  8   9 200  11  12  20  14]]
'''

#3-d three dimension array
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)
'''
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
'''
#work outside in
print(b[0,1,1]) #print 4
print(b[:,1,:])
'''
[[3 4]
 [7 8]]
'''
print(b[:,0,:])
'''
[[1 2]
 [5 6]]
'''
print(b[:,0,0]) #print [1 5]
b[:,1,:] = [[9,9], [8,8]]
print(b)
'''
[[[1 2]
  [9 9]]

 [[5 6]
  [8 8]]]
'''

a = np.zeros(5)
print(a) #print [ 0.  0.  0.  0.  0.]
aint32 = np.zeros(5, dtype=np.int32)
print(aint32) #print [0 0 0 0 0]
a = np.zeros([2,3])
print(a)
'''
[[ 0.  0.  0.]
 [ 0.  0.  0.]]
'''
a = np.ones([4,4])
print(a)
'''
[[ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]]
'''
a = np.full([2,2], 99, dtype=np.float32)
print(a)
'''
[[ 99.  99.]
 [ 99.  99.]]
'''
a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
print(a)
'''
[[ 1  2  3  4  5  6  7]
 [ 8  9 10 11 12 13 14]]
'''
alike = np.full_like(a, 4)
print(alike)
'''
[[4 4 4 4 4 4 4]
 [4 4 4 4 4 4 4]]
'''
alike = np.full_like(a, .9, dtype=np.float)
print(alike)
'''
[[ 0.9  0.9  0.9  0.9  0.9  0.9  0.9]
 [ 0.9  0.9  0.9  0.9  0.9  0.9  0.9]]
'''
a = np.random.random([4,2])
print(a)
'''
[[ 0.54789021  0.34317282]
 [ 0.93810684  0.88204281]
 [ 0.80214372  0.873687  ]
 [ 0.01499133  0.34825153]]
'''
a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
print(a)
'''
[[ 1  2  3  4  5  6  7]
 [ 8  9 10 11 12 13 14]]
'''
print(a.shape)
a = np.random.random(a.shape)
print(a) #print (2, 7)
'''
[[ 0.16428964  0.34438615  0.06215844  0.56664062  0.24604828  0.26907974
   0.53226375]
 [ 0.09890719  0.31920714  0.02603717  0.50141899  0.10801047  0.96546719
   0.20916181]]
'''
a = np.random.randint(7, size=[4,2]) #number is from 0 to 7 exclusive
print(a)
'''
[[6 2]
 [6 5]
 [0 3]
 [4 6]]
'''
a = np.random.randint(20, 31, size=[2,2]) #number is from 20 to 31 exclusive
print(a)
'''
[[20 30]
 [29 28]]
'''
#an identity matrix is a square matrix
a = np.identity(3)
print(a)
'''
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
'''
a = np.identity(3, dtype="int")
print(a)
'''
[[1 0 0]
 [0 1 0]
 [0 0 1]]
'''
a = np.array([1,2,3])
print(a) #print [1 2 3]
repeata = np.repeat(a,3)
print(repeata) #print [1 1 1 2 2 2 3 3 3]
repeata = np.repeat(a,5)
print(repeata) #print [1 1 1 1 1 2 2 2 2 2 3 3 3 3 3]
a = np.array([[1,2,3]])
print(a) #print [[1 2 3]]
repeata = np.repeat(a,3, axis=0)
print(repeata)
'''
[[1 2 3]
 [1 2 3]
 [1 2 3]]
'''
repeata = np.repeat(a,3, axis=1)
print(repeata) #print [[1 1 1 2 2 2 3 3 3]]

exercise = np.ones([5,5], dtype=np.int)
exercise[2,2] = 9
exercise[1,1:4] = 0
exercise[2,1] = 0
exercise[2,3] = 0
exercise[3,1:4] = 0
print(exercise)
'''
[[1 1 1 1 1]
 [1 0 0 0 1]
 [1 0 9 0 1]
 [1 0 0 0 1]
 [1 1 1 1 1]]
'''
#there must be a faster solution.  Instructor's solution.
output = np.ones([5,5], dtype=np.int)
z = np.zeros([3,3], dtype=np.int)
z[1,1] = 9
output[1:4,1:4] =  z  #replace rows 1-3 and columns 1-3 with z.  Ending number is exclusive.  output[1:-1,1:-1] =  z also works.
print(output)
'''
[[1 1 1 1 1]
 [1 0 0 0 1]
 [1 0 9 0 1]
 [1 0 0 0 1]
 [1 1 1 1 1]]
'''

#use .copy() when copying arrays.  Keep the copied array separate from original source.
a = np.array([1,2,3])
b = a
b[0] = 100
print(a) #print [100   2   3]
a = np.array([1,2,3])
b = a.copy()
b[0] = 100
print(a) #print [1   2   3]
print(b) #print [100   2   3]

#Mathematics
a = np.array([1,2,3,4])
print(a) #print [1 2 3 4]
print(a+2) #print [3 4 5 6]
print(a-2) #print [-1  0  1  2]
print(a*2) #print [2 4 6 8]
print(a/2) #print [ 0.5  1.   1.5  2. ]
b = np.array([1,0,1,0])
print(a+b) #print [2 2 4 4]
print(a**2) #print [ 1  4  9 16]
print(np.sin(a)) #print [ 0.84147098  0.90929743  0.14112001 -0.7568025 ]
#Just watched Linear Algebra
stats = np.array([[1,2,3],[6,5,4]])
print(stats)
'''
[[1 2 3]
 [6 5 4]]
'''
print(np.min(stats)) #print 1
print(np.max(stats)) #print 6
print(np.min(stats, axis=0)) #print [1 2 3]
print(np.min(stats, axis=1)) #print [1 4]
print(np.sum(stats)) #print 21
print(np.sum(stats, axis=0)) #print [7 7 7]
print(np.sum(stats, axis=1)) #print [ 6 15]
#start video at 44:00