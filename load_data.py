import glob
import numpy as np
def data():
    X = []
    Y = []
    X_new = []
    Y_new = []
    for i in range(6):
        files = glob.glob("./datasets/betti{0}/channel1/*".format(i+1))
        for file in files:
    
            with open(file,"r") as f:
                cont= [int(_) for _ in f.read().split()]    
                X.append(cont)
                Y.append(i+1)
        
    for i in range(72):
        for j in range(6):
            X_new.append(X[i+72*j])
            Y_new.append(j)
            
    return np.array(X_new),np.array(Y_new)
