#---------cycle detection in directed graph -------
#check if cycle exisits
def dfs(vertex):
    if vertex == null:
        return False
    #maintain two arrays of boolean
    visited = [False] * (len(vertex))
    recStack = [False] * (len(vertex))
    #for all the vertexes
    for i in range(vertex):
        #if cycle exisits
        if isCycleExist(i,visited,recStack):
            return True

def isCycleExist(node, visited, recStack):
    visited[node] = True
    recStack[node] = True

    #for all the nighbours of the current node
    for neighbors in node:
        #if the node is not visited
        if visited[neighbors] == False:
            if isCycleExist(neighbors, visited, recStack):
                return True
        #if the node is already visited
        elif recStack[neighbors] == True:
            return True
        
        #popout from the recursion stack
        recStack[neighbors] = False
        return False    
#---------cycle detection in undirected graph -------

def dfs(vertex):
    if vertex == null:
        return False
    visited = [False] * (len(visited))
    for i in range(vertex):
        if isCycleExist(i, visited, -1):
            return True

def isCycleExist(node, visited, parent):
    visited[node] = True

    for neighbors in node:
        if visited[neighbors] == False:
            if isCycleExist(neighbors, visited, node):
                return True
        elif parent != neighbors:
                return True
    
    return False
