import homcloud as hc
import matplotlib.pyplot as plt

def display_PD(pd,picname=["test1.png","test2.png","test3.png"]):
    for i in range(1):
        pd[i].histogram((0, 1), 26).plot(colorbar={"type": "log"})#Birthの表示範囲を指定
        plt.savefig(picname[i])
        
        return pd