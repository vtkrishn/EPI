#Find cycles in directed graph
#init a stack
stack = []
#init visited boolean array
visited = []

def isCyclic(index, v, s):
    #if its not already visited
    if not v[index]:
        #set visited for the index to True
        v[index]=True
        # add to the stack
        s[index]=True
        #in range of all the available neignboring nodes
        for i in range(i.heighbor()):
            #if its not visited and recurse for next neighborin nodes
            if (not v[index] and isCyclic(i, v,s)) or s[index]
                return True
    s[index]=False
    return False

def helper(nodes):
    #in range of all the available nodes
    for i in range(nodes):
        #set visited for the index to True
        visited[i] = True
        # add to the stack
        stack[i] = True
        #check for cycle and print accordninglys
        if isCyclic(i, visited, stack):
            print 'cycle detected'
    print 'cycle not detected'

#for e.g 6 nodes
helper(6)