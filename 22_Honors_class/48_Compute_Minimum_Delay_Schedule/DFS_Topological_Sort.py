class Graph:
    map= {}
    def addEdge(self,a,b):
        if self.map.has_key(a):
            if b not in self.map[a]:
                self.map[a].append(b)
        else:
            self.map[a] = [b]
        
        if self.map.has_key(b):
            if a not in self.map[b]:
                self.map[b].append(a)
        else:
            self.map[b] = [a]

g = Graph()
g.addEdge(1,2)
g.addEdge(1,4)
g.addEdge(3,2)
g.addEdge(4,2)
g.addEdge(5,1)
g.addEdge(2,1)

def dfs(val, visited, i,stack):
    if visited[i] == True:
        return
    
    visited[i] = True
    if val.has_key(i):
        if not visited[i]:
            dfs(val[i], visited, i,stack)
    
    #append the topological sort order at the last to the stack
    stack.append(i)
    
visited = []
for _ in range(len(g.map)):
    visited.append(False)

#pass stack for topological sort
stack = []
for i in range(len(g.map)):
    dfs(g.map, visited, i, stack)

#print topological ordering
for i in stack:
    print i
