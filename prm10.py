import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print("Original Array \n",arr) 
newArr = np.append(arr, 88)
print("1D Appended Array \n",newArr) 
arr1= np.array([[36,45],[50,52]])
print("Array 1 \n",arr1) 
arr2= np.array([[56,60],[65,73]])
print("Array 2 \n",arr2) 
res=np.append(arr1,arr2,axis=1)
print("2D Appended Array \n",res)

