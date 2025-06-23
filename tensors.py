#  Tensors -> basically neurons 

import torch 
import numpy as np 

#simple python list

mylist = [1,2,3,4,5] # <- single dimentional 
newList=[[1,2,3,4,5],[6,7,8,9,10]]# <- 2 dimentional 
print(mylist)
print(newList)

#Creation of a numpy array 
#What is the difference between numpy and arraylist? -> numpy is more suited for larger datasets such as 2D arrays >
new_array=[[1,2,3,4,5],[6,7,8,9,10]]
new_numpy_array = np.array(new_array)
print(new_numpy_array)

# Creation of a tensor
# can be any variable name but we shall call it tensor_2d

tensor_2d = torch.rand(3,4)
#Creates a tensor and generates random values in a 3 x 4 matrix 
print(tensor_2d)
# Tensors can be of any size
# Can pass a numpy as a parameter into a tensor to create a new tensor

array_numpy_new = np.random.rand(3,4)
print(array_numpy_new)
# Creation of a new numpy array
# Now pass the numpy array as a paramenter into the tensor 

tensor_2d_v2 = torch.tensor(array_numpy_new)
print(tensor_2d_v2)

# torch.tensor() used here to convert the numpy array into a tensor
