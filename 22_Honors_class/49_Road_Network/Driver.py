#floyd warshall

import random
class HighWay():
    pass

#exixting Highway
existingList = []
for i in range(5):
    h = HighWay()
    h.x=random.choice(range(100))
    h.y=random.choice(range(100))
    h.d=random.choice(range(100))
    existingList.append(h)

#create a graph out of the existing highway
g ={}
for h in existingList:
    g[h.x]=[h.y,h.d]
    g[h.y]=[h.x,h.d]

dictlist=[]
for key, value in g.iteritems():
    temp = [key,value]
    dictlist.append(temp)

#do floyd warshall
# for k in range(len(g)):
#     for i in range(len(g)):            
#         for j in range(len(g)):            
#             if dictlist[i][j] > dictlist[i][k] + dictlist[k][j]:
#                 dictlist[i][j] = dictlist[i][k] + dictlist[k][j]

#proposed highway
proposedList = []
for i in range(5):
    p = HighWay()
    p.x=random.choice(range(100))
    p.y=random.choice(range(100))
    p.d=random.choice(range(100))
    proposedList.append(p)

#find the savings
proposalSavings = 0
bestProposalSavings = 0
for p in proposedList:
    for i in range(5):
        for j in range(5):
            savings=dictlist[i][j] - dictlist[i][p.x] + p.d + dictlist[p.y][j]
            if savings > 0:
                proposalSavings += savings
    if proposalSavings > bestProposalSavings:
        bestProposalSavings = proposalSavings
        bestProposal = p
return bestProposal
