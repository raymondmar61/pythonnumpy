#YouTube Joeyajames
#NumPy data types:  int8 bit -128 to 127, int16 bit -32768 to 32,767, int32, int64, uint8 unsigned integer 0 to 255, uint16 0 to 65535, uint32, uint64, float16 half precision signed float, float32 single precision signed lfoat, float64 double precision signed float, compex64, complex 128.  Also boolean bool_, string, datetime, and python object.  Default is float64.
#Variance calculation is population sample.  Standard deviaiton is population sample.
import numpy as np

mylist = [i for i in range(1,6)]
myarray = mylist
print(mylist) #print [1, 2, 3, 4, 5]
print(myarray) #print [1, 2, 3, 4, 5]
#python list
for i in range(len(mylist)):
	mylist[i] *= 3
	print(mylist[i]) #print 3\n 6\n 9\n 12\n 15
mylist = [i for i in range(1,6)]
mylist *= 3
print(mylist) #print [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

#NumPy Array
numpya = np.array([2, 3, 4])
print(numpya) #print [2 3 4]
numpyb = np.arange(1, 12, 2)
print(numpyb) #print [ 1  3  5  7  9 11] Print numbers starting at 1 increment 2
numpyc = np.linspace(1, 12, 6)
print(numpyc) #print [  1.    3.2   5.4   7.6   9.8  12. ]  Print six floating numbers evenly spaced between 1 and 12 inclusive
numpyd = numpyc.reshape(3,2)
print(numpyd) #print [[  1.    3.2]\n [  5.4   7.6]\n [  9.8  12. ]]  Reshape listc to three dimension two elements each or three rows two elements each.
print(numpyd.size) #print 6  Print number of elements
print(numpyd.shape) #print (3, 2)
print(numpya.size) #print 3  Print number of elements
print(numpya.shape) #print (3,)
print(numpyd.dtype) #print float64
print(numpya.dtype) #print int64
print(numpyd.itemsize) #print 8 prints memory size in bytes
print(numpya.itemsize) #print 8 prints memory size in bytes
numpye = np.array([(1.5, 2, 3), (4, 5, 6)])
print(numpye) #print [[ 1.5  2.   3. ]\n [ 4.   5.   6. ]]
print(numpye < 4) #print [[ True  True  True]\n [False False False]] Prints True or False less than 4
numpyf = numpyd * 3
print(numpyf) #print [[  3.    9.6]\n [ 16.2  22.8]\n [ 29.4  36. ]] Prints all elements multiplied by 3
numpyg = np.zeros((3,4))
print(numpyg) #print [[ 0.  0.  0.  0.]\n [ 0.  0.  0.  0.]\n [ 0.  0.  0.  0.]]
numpyh = np.ones((2,3))
print(numpyh) #print [[ 1.  1.  1.]\n [ 1.  1.  1.]]
numpyi = np.ones((10))
print(numpyi) #print [ 1.  1.  1.  1.  1.  1.  1.  1.  1.  1.]
numpyj = np.array([2, 3, 4], dtype=np.int16)
print(numpyj) #print [2 3 4]
print(numpyj.dtype) #print int16
print(numpyj.itemsize) #print 2 prints memory size in bytes
numpyk = np.random.random((2,3))
print(numpyk) #print [[ 0.42261172  0.45256203  0.0604086 ]\n [ 0.1273987   0.33078599  0.31624098]] prints random numbers between 0 and 1 two dimensions three elements
np.set_printoptions(precision = 2, suppress=True) #print future NumPy two decimal places and no scientific notation.
print(numpyk) #print [[ 0.42  0.45  0.06]\n [ 0.13  0.33  0.32]
numpyl = np.random.randint(0,10,5)  #random integers between 0 and 10 inclusive five elements
print(numpyl) #print [7 1 4 4 1]
print(type(numpyl)) #print <class 'numpy.ndarray'>
listl = list(numpyl) #convert numpy to list.  correct way? 
print(listl) #print [7, 1, 4, 4, 1]
print(type(listl)) #print <class 'list'>
print(numpyl.sum()) #print 17
print(numpyl.min()) #print 1
print(numpyl.max()) #print 7
print(numpyl.mean()) #print 3.4.  There is no .average()
print(numpyl.var()) #print 5.04.  Variance is population.
print(np.array([7, 1, 4, 4, 1]).var()) #print 5.04.  Variance is population.
print(np.array([7, 1, 4, 4, 1]).std()) #print 2.24499443206.  Standard deviation is population.
numpym = np.array([3, 8, 4, 5, 3, 8])
numpymreshape = numpym.reshape(3, 2)  #reshape three dimensions two elements for each dimension
print(numpymreshape) #print [[3 8]\n [4 5]\n [3 8]]
print(numpymreshape.sum(axis=1)) #print [11  9 11]  adds each horizontal rows or each dimension and its elements
print(numpymreshape.sum(axis=0)) #print [10 21]  Adds each vertical column
numpyn = np.arange(0,10)
print(numpyn) #print [0 1 2 3 4 5 6 7 8 9]
for eachnumpyn in numpyn:
	print(eachnumpyn) #print 0 to 9 each line
numpyo = np.random.shuffle(numpyn)
print(numpyo) #print None.  RM:  I don't know why it doesn't work.  No .shuffle in Python3.6?!?
numpyp = np.random.choice(numpyn)
print(numpyp) #print 1.  Numpy randomly chooses one item.
print("\n")

#import text files or csv files
data = np.loadtxt("data.txt", dtype=np.uint8, delimiter=",", skiprows=1)  #skip the first row because the first row is the header.  Assigned data type dtype=np.uint8 to reduce file size.
print(data) #print [[9 3 8 7 6 1 0 4 2 5]\n [1 7 4 9 2 6 8 3 5 0]\n [4 8 3 9 5 7 2 6 0 1]\n [1 7 4 2 5 9 6 8 0 3]\n [0 7 5 2 8 6 3 4 1 9]\n [5 9 1 4 7 0 3 6 8 2]]