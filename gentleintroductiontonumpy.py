#A Gentle introduction to NumPy programmingknowledge YouTube channel

import numpy as np
nlist = [1, 2, 3, 4, 5, 6]
print(nlist) #print [1, 2, 3, 4, 5, 6]
nparray = np.array(nlist)
print(nparray) #print [1 2 3 4 5 6]
print(type(nparray)) #print <class 'numpy.ndarray'>
print(nparray.dtype) #print int64
for i in nparray:
	print(i) #print 1\n 2\n 3\n 4\n 5\n 6
nparrayadd7 = nparray + [7]
print(nparrayadd7) #print [ 8  9 10 11 12 13]  #RM:  adds 7 to each value
nparrayappendadd7 = np.append(nparray, 7)
print(nparrayappendadd7) #print [1 2 3 4 5 6 7]
npmultiply2 = nparray * 2
print(npmultiply2) #print [ 2  4  6  8 10 12]
print(np.sqrt(nparray)) #print [ 1.          1.41421356  1.73205081  2.          2.23606798  2.44948974]
print(np.log(nparray)) #print [ 0.          0.69314718  1.09861229  1.38629436  1.60943791  1.79175947]
print(np.exp(nparray)) #print [   2.71828183    7.3890561    20.08553692   54.59815003  148.4131591  403.42879349]
nparrayappendadd7first = np.append(nparray, 7)
print(nparrayappendadd7first) #print [1 2 3 4 5 6 7]

a = np.array([1, 2, 3])
b = np.array([[1, 2], [3, 4], [5, 6]])
print(b)
'''
[[1 2]
 [3 4]
 [5 6]]
'''
print(a[0]) #print 1
print(b[0]) #print [1 2]
print(b[0][0]) #print 1
print(b[0, 0]) #print 1
print(b[1][1]) #print 4
print(b[1, 1]) #print 4
print(b[2]) #print [5 6]
M = np.matrix([[1, 2], [3, 4], [5, 6]])  #instructor said numpy documentation says don't use matrix.  Use arrays.
print(M)
'''
[[1 2]
 [3 4]
 [5 6]]
'''
print(b.T)  #Transpose.  Don't use lower case t.
'''
[[1 3 5]
 [2 4 6]]
'''
print(b.shape) #print (3, 2).  Ignore the b.T result.
c = b.T
print(c)
'''
[[1 3 5]
 [2 4 6]]
'''
print(c.shape) #print (2, 3)
print(c.ndim) #print 2.  Two dimensional array
print(c.size) #print 6.  Prints the number of elements in an array.
print(c.itemsize) #print 8.  Prints the size of each elements.  Size is memory size in bytes.
print(c.dtype) #print int64
print(c.min()) #print 1
print(c.max()) #print 6
print(c.sum()) #print 21
print(c.sum(axis=0)) #print [ 3  7 11].  Axis=0 add by column
print(c.sum(axis=1)) #print [ 9, 12].  Axis=1 add by row
d = np.array([1.1, 1.2])
print(d.dtype) #print float64
e = np.array([1, 2], dtype=np.float64)
print(e) #print [ 1.  2.]
print(e.dtype) #print float64

print(np.zeros((2, 3)))
'''
[[ 0.  0.  0.]
 [ 0.  0.  0.]]
'''
print(np.ones((3, 2)))
'''
[[ 1.  1.]
 [ 1.  1.]
 [ 1.  1.]]
'''
print(np.ones((3, 2), dtype=np.int16))
'''
[[1 1]
 [1 1]
 [1 1]]
'''
#these np.empty are random numbers
print(np.empty((3, 3)))
'''
[[  6.91493376e-310   6.91493376e-310   0.00000000e+000]
 [  0.00000000e+000   7.69843740e+218   5.98189658e-154]
 [  4.47593816e-091   6.01334512e-154   2.88980588e+204]]
'''
print(np.empty([3, 3]))
'''
[[  6.90319868e-310   6.90319868e-310   0.00000000e+000]
 [  0.00000000e+000   2.00995441e-309   1.69186817e-309]
 [  1.63002224e-070   7.22423520e-312   6.83770537e-302]]
'''
print(np.empty((3, 3), dtype=np.int16))
'''
[[-13152  11626  32606]
 [     0 -13152  11626]
 [ 32606      0      0]]
'''
#however, set dtype to string
print(np.empty((3, 3), dtype=np.str))
'''
[['' '' '']
 ['' '' '']
 ['' '' '']]
'''
print(np.arange(1,5)) #print [1 2 3 4]
print(np.arange(1,5,.5)) #print [ 1.   1.5  2.   2.5  3.   3.5  4.   4.5]
print(np.linspace(1, 5)) #50 empty numbers evenly spaced between 1 and 5.  50 is the default.
'''
[ 1.          1.08163265  1.16326531  1.24489796  1.32653061  1.40816327
  1.48979592  1.57142857  1.65306122  1.73469388  1.81632653  1.89795918
  1.97959184  2.06122449  2.14285714  2.2244898   2.30612245  2.3877551
  2.46938776  2.55102041  2.63265306  2.71428571  2.79591837  2.87755102
  2.95918367  3.04081633  3.12244898  3.20408163  3.28571429  3.36734694
  3.44897959  3.53061224  3.6122449   3.69387755  3.7755102   3.85714286
  3.93877551  4.02040816  4.10204082  4.18367347  4.26530612  4.34693878
  4.42857143  4.51020408  4.59183673  4.67346939  4.75510204  4.83673469
  4.91836735  5.        ]
'''
print(np.linspace(1, 5, 10))
'''
[ 1.          1.44444444  1.88888889  2.33333333  2.77777778  3.22222222
  3.66666667  4.11111111  4.55555556  5.        ]
'''
print(np.random.random((2, 3)))
'''
[[ 0.99541518  0.55213256  0.35697326]
 [ 0.40153022  0.54301159  0.06467299]]
'''
c = np.arange(1,7).reshape(2,3)[::-1]
print(c)
'''
[[4 5 6]
 [1 2 3]]
'''
c = np.arange(1,7).reshape(3,2)
print(c)
'''
[[1 2]
 [3 4]
 [5 6]]
 '''
c = c.T
print(c)
'''
[[1 3 5]
 [2 4 6]]
'''
c = np.arange(1,7).reshape(3,2)
print(c)
'''
[[1 2]
 [3 4]
 [5 6]]
'''
print(c.reshape(6,1))
'''
[[1]
 [2]
 [3]
 [4]
 [5]
 [6]]
'''
d = np.arange(1,10)
print(d) #print [1 2 3 4 5 6 7 8 9]
print(d.reshape(3,3))
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''
print(d.reshape(3,-1))
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''
e = np.random.randint(0, 10, size=(2,4))
f = np.random.randint(0, 10, size=(1,4))
print(e)
'''
[[5 0 1 4]
 [5 0 2 3]]
'''
print(f)
'''
[[7 5 5 2]]
'''
g = np.vstack((e,f))
print(g)
'''
[[5 0 1 4]
 [5 0 2 3]
 [7 5 5 2]]
'''
h = np.random.randint(0, 10, size=(3,2))
i = np.random.randint(0, 10, size=(3,5))
print(h)
'''
[[9 9]
 [8 4]
 [0 1]]
'''
print(i)
'''
[[8 3 6 0 9]
 [8 0 6 9 0]
 [5 7 4 3 4]]
'''
j = np.hstack((i,h))
print(j)
'''
[[8 3 6 0 9 9 9]
 [8 0 6 9 0 8 4]
 [5 7 4 3 4 0 1]]
'''
k = np.random.randint(0, 10, size=(3,5))
print(k)
'''
[[0 2 5 1 5]
 [8 7 1 1 2]
 [2 5 3 8 5]]
'''
print(np.vsplit(k,3)) #print [array([[0, 2, 5, 1, 5]]), array([[8, 7, 1, 1, 2]]), array([[2, 5, 3, 8, 5]])]
print(np.vsplit(k,3)[1]) #print [[8, 7, 1, 1, 2]]
print(sum(np.vsplit(k,3)[1])) #print [8, 7, 1, 1, 2]
print((np.vsplit(k,3)[1]).sum()) #print 19
l = np.random.randint(0, 10, size=(2,4))
print(l)
'''
[[5 9 3 3]
 [2 0 5 1]]
'''
print(np.hsplit(l,4))
'''
[array([[5],
       [2]]), array([[9],
       [0]]), array([[3],
       [5]]), array([[3],
       [1]])]
'''