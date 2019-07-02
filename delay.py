import numpy as np
def delay(data,channel):
    line = data.loc[:,channel]
    pointcloud = np.array([0,0,0])
    
    for i in range(0,len(line)-2):
        tmp = np.array([line[i],line[i+1],line[i+2]]) 
        pointcloud = np.c_[pointcloud,tmp]

    return pointcloud.T