#Code1 To print 2D array
print("Pranik Nikose Edit")
print("To print 2D array")
from numpy import *
arr1=array([
            [1,2,3,4,5,6],
            [6,5,4,3,2,1]
           ])
print(arr1)
print()

#Code2 Print Datatype,dimension,rows&columns ,size
print("Dataype",arr1.dtype)
print("Dimension",arr1.ndim)
print("Rows & Columns",arr1.shape)
print("Numbers of Elemenet",arr1.size)
print()

#Code3 Convert 2D array to 1D array
print("To print 2D array to 1D array")
arr2=arr1.flatten()
print("2D to 1D = ",arr2)
print()

#Code4 1D to 2D array
print("To print 1D to 2D array:")
from numpy import *
arr4=array([1,2,3,4,5,6,7,8])
arr5 = arr4.reshape(2,4) # (Rows,Columns)
print(arr5)
print()

#Code5 Convert 2D Array to matrix
print("Convert 2D Array to matrix:")
m= matrix(arr5)
print(m)
print()

#code6 Matrix
from numpy import *
m1= matrix('1 2 4 ; 5 6 8 ; 3 7 9')
print(m1)
print()

# cod7 To print Diagonal,min,max of m1
print('diagonal of m1 =',diagonal(m1))
print('min of m1 =',m1.min())
print('max of m1 =',m1.max())