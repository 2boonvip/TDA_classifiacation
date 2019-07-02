import homcloud.interface as hc
import math

def make_PD(pointcloud):
    hc.PDList.from_alpha_filtration(pointcloud, 
                                    save_to="pointcloud.idiagram",
                                    save_boundary_map=True)
    
    pdlist = hc.PDList("pointcloud.idiagram")
    
    pd = [pdlist.dth_diagram(i) for i in range(3)]
    
    for j in range(len(pd)):
        lengths = [math.sqrt(pd[j].deaths[i] ** 2 + pd[j].births[i] ** 2 ) for i in range(len(pd[j].deaths))]
        length_maximum = max(lengths)
        
        for i in range(len(pd[j].deaths)):
            pd[j].births[i] = math.sqrt(2) * pd[j].births[i] / length_maximum
            pd[j].deaths[i] = math.sqrt(2) * pd[j].deaths[i] / length_maximum
            
        return pd
