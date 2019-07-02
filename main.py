# -*- coding: utf-8 -*-
#PDの計算及びbetti系列の計算を行うプログラム
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas
import delay
import math
import homcloud.interface as hc
import glob

betti_number = 150 #betti系列の1つの次元あたりのデータ数
target_channel = "channel1"#解析対象のチャンネル

def display_PD(pd,picname=["test1.png","test2.png","test3.png"]):
    for i in range(3):
        pd[i].histogram((0, 1.0), 50).plot(colorbar={"type": "log"})#Birthの表示範囲を指定
        plt.savefig(picname[i])

def data_input(path): 
    data = pandas.read_csv(path)
    return data

def make_PD(pointcloud):
    hc.PDList.from_alpha_filtration(pointcloud, 
                                    save_to="pointcloud.idiagram",
                                    save_boundary_map=True)
    
    pdlist = hc.PDList("pointcloud.idiagram")
    
    PD = []
    
    for j in range(3):
        pd = pdlist.dth_diagram(j)
        
        death_max = max(pd.deaths)
        birth_max = max(pd.births)
        
        #0-1区間で正規化
        for i in range(len(pd.deaths)):
            pd.births[i] = pd.births[i] / birth_max if pd.births[i] != 0 else 0
            pd.deaths[i] = pd.deaths[i] / death_max if pd.deaths[i] != 0 else 0
        
        PD.append(pd)
        
    return PD

def betti_sequence(pd):
    betti_sequence = []
    for i in range(0,2):
        for j in range(betti_number):
            tmp = 0
            for k in range(len(pd[i].deaths)):
                if pd[i].births[k] <= (1/betti_number)*j and pd[i].deaths[k] >= (1/betti_number)*j:
                    tmp += 1
            betti_sequence.append(tmp)
            
    return betti_sequence

def output_betti_text(betti,txt_name):
    with open(txt_name,'w') as f:
        for i in betti:
            f.write('{0} '.format(i))


def main(path):
    data = data_input(path)
    pointcloud = delay.delay(data,target_channel)
    PD = make_PD(pointcloud)
    betti = betti_sequence(PD)
    
    return betti

count = 1
for i in range(1,7):
    files = glob.glob("./datasets/status{0}/*".format(i))
    for file in files:
        betti = main(file)
        output_betti_text(betti,
                          "./datasets/betti{0}/".format(i)+ target_channel +"/betti{0}.txt".format(count))
        count += 1

print("==DONE==")