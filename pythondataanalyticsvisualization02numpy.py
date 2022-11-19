#Python Data Analytics And Visualization by Phuong Vo.T.H Chapter 02 NumPy Arrays And Vectorized Computation
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
import numpy as np
indexarray = np.arange(7)
print(indexarray) #print [0 1 2 3 4 5 6]
print(indexarray[1]) #print 0
print(indexarray[4]) #print 4
print(indexarray[-1]) #print 6
indexarraymultidimension = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(indexarraymultidimension)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''
print(indexarraymultidimension[1]) #print [4 5 6]
print(indexarraymultidimension[0:2])
'''
[[1 2 3]
 [4 5 6]]
'''
print(indexarraymultidimension[:2])
'''
[[1 2 3]
 [4 5 6]]
'''
print(indexarraymultidimension[0][2]) #print 3
print(indexarraymultidimension[2][1]) #print 8
indexarraymultidimension[2][1] = 188
print(indexarraymultidimension)
'''
[[  1   2   3]
 [  4   5   6]
 [  7 188   9]]
'''
extractrow = indexarraymultidimension[2]
print(extractrow) #print [  7 188   9]
extractrow[-1] = 9991
print(extractrow) #print [   7  188 9991]
divisiblebyfive = np.array([3, 5, 1, 10])
print(divisiblebyfive) #print [3 5 1 10]
divisiblebyfivetruefalse = (divisiblebyfive % 5 == 0)
print(divisiblebyfivetruefalse) #print [False  True False  True]
print(type(divisiblebyfivetruefalse)) #print <class 'numpy.ndarray'>
integermask = np.arange(1, 17).reshape(4, 4)
print(integermask)
'''
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]]
'''
print(integermask[divisiblebyfivetruefalse]) #from print(divisiblebyfivetruefalse) #print [False  True False  True]
'''
[[ 5  6  7  8]
 [13 14 15 16]]
'''
print(integermask[2]) #print [ 9 10 11 12]
print(integermask[2][1]) #print 10
print(integermask[[2, 3], [3, 1]]) #print [12 14]
print(integermask[[2, 1]]) #RM:  notice the double brackets
'''
[[ 9 10 11 12]
 [ 5  6  7  8]]
'''
print(integermask[[1, 2]]) #RM:  notice the double brackets
'''
[[ 5  6  7  8]
 [ 9 10 11 12]]
'''
print(integermask[-1]) #print [13 14 15 16]
print(integermask[[-1, -2]])
'''
[[13 14 15 16]
 [ 9 10 11 12]]
'''
print(integermask[0][3]) #print 4
print(integermask[0:3])
'''
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
'''
print(integermask[[0], [3]]) #print [4]
onesarray = np.ones(4)
print(onesarray) #print [1. 1. 1. 1.]
print(onesarray * 2) #print [2. 2. 2. 2.]
print(onesarray + 3) #print [4. 4. 4. 4.]
arithmeticarrays = np.ones([2, 4])
print(arithmeticarrays)
'''
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]]
'''
print(arithmeticarrays * arithmeticarrays)
'''
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]]
'''
print(arithmeticarrays + arithmeticarrays)
'''
[[2. 2. 2. 2.]
 [2. 2. 2. 2.]]
'''
arithmeticarraysbetter = np.arange(1, 7).reshape(2, 3)
print(arithmeticarraysbetter)
'''
[[1 2 3]
 [4 5 6]]
'''
print(arithmeticarraysbetter + arithmeticarraysbetter)
'''
[[ 2  4  6]
 [ 8 10 12]]
'''
print(arithmeticarraysbetter * arithmeticarraysbetter)
'''
[[ 1  4  9]
 [16 25 36]]
'''
logicaloperationone = np.array([1, 2, 3, 4, 5])
logicaloperationtwo = np.array([1, 1, 3, 5, 8])
print(logicaloperationone == logicaloperationtwo) #print [ True False  True False False]
print(np.array_equal(logicaloperationone, logicaloperationtwo)) #print False
print(np.array_equal(onesarray, onesarray * 1)) #print True.  From onesarray = np.ones(4) print(onesarray) #print [1. 1. 1. 1.]
c = np.array([1, 0])
d = np.array([1, 1])
print(c) #print [1 0]
print(d) #print [1 1]
print(np.logical_and(c, d)) #print [ True False]
print(logicaloperationone) #print [1 2 3 4 5]
print(logicaloperationtwo) #print [1 1 3 5 8]
print(np.logical_and(logicaloperationone, logicaloperationtwo)) #print [ True  True  True  True  True] #RM:  I don't understand logical_and()
transpose = np.arange(0, 26, 5).reshape(3, 2)
print(transpose)
'''
[[ 0  5]
 [10 15]
 [20 25]]
'''
print(transpose.T)  #The dot T .T is the transpose function
'''
[[ 0 10 20]
 [ 5 15 25]]
'''
swapaxesarray = np.array([[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]])
print(swapaxesarray)
'''
[[[ 0  1  2]
  [ 3  4  5]
  [ 6  7  8]
  [ 9 10 11]]]
'''
print(swapaxesarray.swapaxes(1, 2)) #the column becomes the row
'''
[[[ 0  3  6  9]
  [ 1  4  7 10]
  [ 2  5  8 11]]]
'''
print(swapaxesarray.swapaxes(2, 1)) #the column becomes the row
'''
[[[ 0  3  6  9]
  [ 1  4  7 10]
  [ 2  5  8 11]]]
'''
print(swapaxesarray.swapaxes(1, 1))
'''
[[[ 0  1  2]
  [ 3  4  5]
  [ 6  7  8]
  [ 9 10 11]]]
'''
print(swapaxesarray.swapaxes(1, 0)) #RM:  I'm guessing swapaxes is another way to transpose.  I don't understand fully.
'''
[[[ 0  1  2]]

 [[ 3  4  5]]

 [[ 6  7  8]]

 [[ 9 10 11]]]

'''
sortarray = np.array([[6, 34, 1, 6], [0, 5, 2, -1]])
print(sortarray)
'''
[[ 6 34  1  6]
 [ 0  5  2 -1]]
'''
print(np.sort(sortarray)) #sort by rows sort row
'''
[[ 1  6  6 34]
 [-1  0  2  5]]
'''
print(np.sort(sortarray, axis=0)) #sort by columns sort column  RM:  how to sort descending?  Reverse the output?
'''
[[ 0  5  1 -1]
 [ 6 34  2  6]]
'''
sortarraydescending = np.sort(sortarray, axis=0) #sort by columns sort column  RM:  how to sort descending?  Reverse the output?
print(sortarraydescending)
'''
[[ 0  5  1 -1]
 [ 6 34  2  6]]
'''
print(sortarraydescending[-1:-2]) #print []
print(sortarraydescending[[-1, -2]]) #notice the double brackets
'''
[[ 6 34  2  6]
 [ 0  5  1 -1]]
'''
print("\n")
integermask = np.arange(1, 17).reshape(4, 4)
print(integermask)
'''
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]]
'''
print(integermask[-1]) #print [13 14 15 16]
print(integermask[[-1, -2]])
'''
[[13 14 15 16]
 [ 9 10 11 12]]
'''
print(integermask[0:3])
'''
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
'''
print(integermask[-1:]) #print [[13 14 15 16]]
#print(integermask[[-1:]]) #print SyntaxError: invalid syntax
#print(integermask[[-1:-2]]) #print SyntaxError: invalid syntax
print(integermask[-1:-2]) #print []
print(integermask[-1, ]) #print [13 14 15 16]
print(integermask[[-1, -2, -3]])
'''
[[13 14 15 16]
 [ 9 10 11 12]
 [ 5  6  7  8]]
'''
roundingarray = np.array([0.34, 1.49, 1.65])
print(np.round(roundingarray)) #print [0. 1. 2.]
print(np.floor(roundingarray)) #print [0. 1. 1.]
print(np.ceil(roundingarray)) #print [1. 2. 2.]
print(np.trunc(roundingarray)) #print [0. 1. 1.]
arithemeticfunctionsone = np.arange(1, 7).reshape(2, 3)
arithemeticfunctionstwo = np.arange(1, 4)
print(arithemeticfunctionsone)
'''
[[1 2 3]
 [4 5 6]]
'''
print(arithemeticfunctionstwo) #print [1 2 3]
print(np.add(arithemeticfunctionsone, arithemeticfunctionstwo))
'''
[[2 4 6]
 [5 7 9]]
'''
print(np.subtract(arithemeticfunctionsone, arithemeticfunctionstwo))
'''
[[0 0 0]
 [3 3 3]]
'''
print(np.multiply(arithemeticfunctionsone, arithemeticfunctionstwo))
'''
[[2 4 6]
 [5 7 9]]
 '''
print(np.divide(arithemeticfunctionsone, arithemeticfunctionstwo))
'''
[[1.  1.  1. ]
 [4.  2.5 2. ]]
'''
print(np.power(arithemeticfunctionsone, arithemeticfunctionstwo))
'''
[[  1   4  27]
 [  4  25 216]]
'''
print(np.mod(arithemeticfunctionsone, arithemeticfunctionstwo))
'''
[[0 0 0]
 [0 1 0]]
'''
#logical comparisons logic compare
print(np.greater(arithemeticfunctionsone, arithemeticfunctionstwo))
'''
[[False False False]
 [ True  True  True]]
'''
print(np.greater_equal(arithemeticfunctionsone, arithemeticfunctionstwo))
'''
[[ True  True  True]
 [ True  True  True]]
'''
print(np.less(arithemeticfunctionsone, arithemeticfunctionstwo))
'''
[[False False False]
 [False False False]]
'''
print(np.less_equal(arithemeticfunctionsone, arithemeticfunctionstwo))
'''
[[ True  True  True]
 [False False False]]
'''
print(np.equal(arithemeticfunctionsone, arithemeticfunctionstwo))
'''
[[ True  True  True]
 [False False False]]
'''
print(np.not_equal(arithemeticfunctionsone, arithemeticfunctionstwo))
'''
[[False False False]
 [ True  True  True]]
'''
mathfunctions = np.array([[2, 4], [3, 5]])
print(mathfunctions)
'''
[[2 4]
 [3 5]]
'''
print(np.sum(mathfunctions)) #print 14
print(np.sum(mathfunctions, axis=1)) #print [6 8]
print(np.sum(mathfunctions, axis=0)) #print [5 9]
print(np.prod(mathfunctions)) #print 120
print(np.prod(mathfunctions, axis=1)) #print [ 8 15]
print(np.prod(mathfunctions, axis=0)) #print [ 6 20]
print(np.diff(mathfunctions)) #diff calculates the discrete difference.  RM:  Discrete is absolute value?
'''
[[2]
 [2]]
'''
print(np.diff(mathfunctions, axis=1))
'''
[[2]
 [2]]
'''
print(np.diff(mathfunctions, axis=0)) #print [[1 1]]
print(np.std(mathfunctions))  #print 1.118033988749895.  Standard deviation.
print(np.var(mathfunctions))  #print 1.25.  Variance.
print(np.mean(mathfunctions))  #print 3.5.  Average.
print(np.where([[True, True], [False, True]], [[1, 2], [3, 4]], [[5, 6], [7, 8]]))
'''
[[1 2]
 [7 4]]
'''
print(np.unique(np.array(["a", "b", "c", "c", "d"]))) #print ['a' 'b' 'c' 'd'].  Unique values which are sorted.
commonelementsone = np.array(["a", "b", "a", "c", "d", "c"])
commonelementstwo = np.array(["a", "xyz", "klm", "d"])
print(np.intersect1d(commonelementsone, commonelementstwo)) #print ['a' 'd'] intersect1d is a number one and letter d find commonality
savearray = np.arange(0, 6).reshape(2, 3) #save array
print(savearray)
'''
[[0 1 2]
 [3 4 5]]
'''
np.save("savearraydefault.npy", savearray)
np.savetxt("saveastextcommandelimiter.txt", savearray, delimiter=",")
print(np.load("savearraydefault.npy")) #load array
'''
[[0 1 2]
 [3 4 5]]
'''
print(np.load("savearraydefault.npy")) #load array default file format
print(np.loadtxt("saveastextcommandelimiter.txt", delimiter=",")) #load array text format
'''
[[0. 1. 2.]
 [3. 4. 5.]]
'''
print(np.loadtxt("saveastextcommandelimiter.txt", delimiter=",", dtype="int8")) #DeprecationWarning: loadtxt(): Parsing an integer via a float is deprecated.
'''
[[0 1 2]
 [3 4 5]]
'''
print(np.loadtxt("saveastextcommandelimiter.txt", delimiter=",").astype(int))
'''
[[0 1 2]
 [3 4 5]]
'''
ninerandomnumbersbetweenzeroandone = np.random.rand(9)
print(ninerandomnumbersbetweenzeroandone) #print [0.46812619 0.62819493 0.74545608 0.44201912 0.82829 0.08787559 0.23261542 0.01345379 0.55882796]
twelverandomnumbersintegers = np.random.randint(1, 200, 12)
print(twelverandomnumbersintegers) #print [149 126  60 188 115  22  32 195  43 135  28  81]
rearrangearray = np.arange(10) #move around rearrange numbers
print(np.random.shuffle(rearrangearray)) #print None
binomialdistribution = np.random.binomial(100, 0.2, 7)
poissondistribution = np.random.poisson(lam=2, size=5)
gaussiandistribution = np.random.normal(loc=2.5, scale=0.3, size=9)
uniformdistribution = np.random.uniform(low=0.5, high=2.5, size=7)
