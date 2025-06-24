#totally basic neural network,
#dataset to be used -> iris dataset
import torch 
import torch.nn as nn 
import torch.nn.functional as F
#Creation of a model class tha inherits the nn.Module

class Model(nn.Module):
    #input layer (in our case as we are using the iris dataset we need the properties of the flowers contained in the dataset)
    #basic architecture of the neural network:
    #we are going to have (4 input layers) and the data is sent to the hiddent layer(x number of neurons)where processing occurs 
    #then outputs the final results 
    # hidden layer (hn)
    #input->h1->h2->h3->h4->output(returns a class)
    
    def __init__(self,in_features=4,h1=8,h2=8,out_features=3):
        super().__init__() #instantiate our nn.module
        #in_features == we have 4 input 
        #h1,h2 for now arbitrary, gotta be explained later 
        #out_features =3 because we have 3 different classes of flowers ie :{iris-setosa,iris-versicolor,iris-virginica}
        self.fc1 =nn.Linear(in_features,h1)
        #fc1 refer to fully connected 1
        # we need to do it for each layer since there are 2, we need to do it twice, scales propotionally with the numbers of layers
        self.fc2 = nn.Linear(in_features,h1,h2)
        #from h1 -> h2 (taking output from h1 feed it to h2)
        # linear == linear model 
        self.out=nn.Linear(h2,out_features)
        # take output of h2 and moves it to the output layer 

def forward(self,x):
    x=F.relu(self.fc1(x)) #relu== rectified linear unit-> function: if the output of function < 0 use 0 else use the actual output 
    x=F.relc(self.fc2(x))
    x=F.self.out(x)
    return x
    # neural networks are inheritly random,if no values are inserted from the beginning, well random numbers will
    #therefore we need a seed to give the network a place where to start so that we can get the most accurate output 
#manual seed for randomization 

torch.manual_seed(41) 
#create and instance of our model 
model=Model()