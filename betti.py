betti_number = 150

def generating_betti_sequence(pd):
    betti_sequence = []
    for i in range(0,2):
        for j in range(betti_number):
            tmp = 0
            for k in range(len(pd[i].deaths)):
                if pd[i].births[k] <= int(1/betti_number)*j and pd[i].deaths[k] >= int(1/betti_number)*j:
                    tmp += 1
            betti_sequence.append(tmp)
            
    return betti_sequence