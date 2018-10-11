import math
import copy
def isArbitrageExist(G):
    O=copy.deepcopy(G)
    for i,j in enumerate(G):
            G[j][0] = -math.log(G[j][0])
            G[j][1] = -math.log(G[j][1])
    return bellmanford(G,O,0)

def bellmanford(G,O, i):
    R = {}
    R['Sheep'] = [0,0]
    R['Goat'] = [1000,1000]
    R['Wheat'] = [1000,1000]    
    for i,j in enumerate(G):
        update=False
        for k in range(2):
            if R[j][k] != 1000:
                if R[j][k] > G[j][k] + O[j][k]:
                    update=True
                    R[j][k] = G[j][k] + O[j][k]
        
        if not update:
            return False
            
    for i,j in enumerate(G):
        for k in range(2):
            if R[j][k] != 1000:
                if R[j][k] > O[j][k] + G[j][k]:
                    return True
    return False            
                
G = {}
G['Sheep'] = [2.34,116]
G['Goat'] = [0.43,50]
G['Wheat'] = [0.02,0.0086]
isArbitrageExist(G)