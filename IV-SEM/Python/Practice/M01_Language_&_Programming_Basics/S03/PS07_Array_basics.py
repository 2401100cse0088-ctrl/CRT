'''
Array: It is collection of homogeneous data elements that can store under a single variable name.
Python does not support arrays. But we can use list or array module to create array in Python.
Python array module example: creating an array, appending elements, and printing the array.
The index value starts from 0 and ends at n-1, where n is the number of elements in the array.
import array
arr = array.array('i', [10, 20, 30, 40, 50])
print(arr,type(arr))
arr.append(60)
print(arr)
arr.append(70)
print(arr)

Num py:
Numpy is a powerful library in Python used for numerical computing. 
It provides support for arrays, matrices, and many mathematical functions to operate on these data structures.
'''
import numpy as np
arr=np.array([10,20,30])
print(arr)
print(np.max(arr))
print(np.min(arr))
print(np.mean(arr))
print(np.sum(arr))
print(np.zeros(8))
print(np.ones(5))
print("Even numbers list is:",np.arange(2,10,2))
print("Odd numbers list is:",np.arange(1,10,2))
print(input("Enter the size of array:"))
ele = list(map(int,input("Enter the elements of array:").split()))
print("Array elements are:",np.array(ele))