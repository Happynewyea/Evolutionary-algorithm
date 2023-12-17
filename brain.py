import numpy as np

def compat(infolist, Enviro):
    
    compact = iscomp(infolist, Enviro)
    compact = sorted(compact, key=abs)

    del compact[2:]
    compact = [x + Enviro for x in compact]
    return compact
    

def iscomp(infolist, Enviro):
    cpdata = []
    for i in range(len(infolist)):
        cpdata.append((infolist[i] - Enviro)) 
    return cpdata

def mutanted(lifedata, w):
    weight = np.random.randint(-1 * int(w/100) - 1, 1 * int(w/100) + 2)
    lifedata = lifedata + weight
    return lifedata