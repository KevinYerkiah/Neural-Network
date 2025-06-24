# #using tensors for performing mathematical operations specifically geared towards deep learning

import torch as tp
tensor_a = tp.tensor([1,2,3,4,5])
tensor_b = tp.tensor([6,7,8,9,10])
#short hand addition
tensor_c = tensor_a + tensor_b
#Second option tensor.add built in function 
tensor_d = tp.add(tensor_a,tensor_b)
print("This is tensor_c: \n"+str(tensor_c))
print("This is tensor_d: \n"+str(tensor_d))
#subtraction of various tensors:
print("tensor_a - tensor_b = "+str((tensor_a - tensor_b)))
#subratction of various tensors using built in function
print("Using tensor.sub() = "+str((tp.sub(tensor_a,tensor_b))))
#multiplication of tensors:
print("tensor_a * tensor_b = "+str((tensor_a*tensor_b)))
#multiplication of tensors by the use of the built in method
print("tensor.mul = "+str((tp.mul(tensor_a,tensor_b))))
#division of the various tensors
print("tensor_a/tensor_b = "+str((tensor_a/tensor_b)))
#division of the various tensors using the built in function
print("tensor.div()= "+str(tp.div(tensor_a,tensor_b)))
#modulo operation (remainder)
print("tensor_a % tensor_b = "+str((tensor_a % tensor_b)))
print("tensor_b % tensor_c = "+str((tensor_b % tensor_c))) #<- simple inverse of the previous operation
#Modulo operation(remainder) using the built in function
print("tensor.remainder() = "+str((tp.remainder(tensor_a,tensor_b))))
print("tensor.remainder() <tensor_b % tensor_a> = "+str((tp.remainder(tensor_b,tensor_a))))
#Exponents aka P O W E R S 
#Exponent using the built in function 
print("tensor.pow() "+str((tp.pow(tensor_a,tensor_b))))

# another and faster way to write the following:
# tensor_a.add(tensor_b)...etcanother and faster way to write the following:
# tensor_a.add(tensor_b)...etc
tensor_a = tensor_a+tensor_b
print("the new values of temsor_a = "+str((tensor_a)))