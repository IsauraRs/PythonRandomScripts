import numpy as np

w =  np.array([[1.], [2]])
b = 1.5

# X is using 3 examples, with 2 features each
# Each example is stacked column-wise
X = np.array([[1., -2., -1.], [3., 0.5, -3.2]])
Y = np.array([[1, 1, 0]])

def sigmoid(z):

    # YOUR CODE STARTS HERE
    s = 1/(1+np.exp(-z))
    
    # YOUR CODE ENDS HERE
    
    return s

def propagate(w, b, X, Y):

    m = X.shape[1]
    A = sigmoid(np.dot(w.T, X) + b)
    print(f'Yshape {Y.shape} , logShape {np.log(A).shape}')
    cost = np.dot((-1/m),np.sum(np.dot(Y,np.log(A).T)+np.dot((1-Y),np.log(1-A).T)))
    print(f'costShape {cost.shape}')
    dw = np.dot((1/m),np.dot(X,np.subtract(A,Y).T))
    db = np.dot((1/m),np.sum((A-Y)))
    cost = np.squeeze(np.array(cost))

    
    grads = {"dw": dw,
             "db": db}
    
    return grads, cost

cost = propagate(w, b, X, Y)
print(cost)



[[ 0.14449502]
 [-0.1429235 ]
 [-0.19867517]
 [ 0.21265053]] 


[[ 0.08639757] ,  [-0.08231268]
 [-0.11798927]
 [ 0.12866053]]

