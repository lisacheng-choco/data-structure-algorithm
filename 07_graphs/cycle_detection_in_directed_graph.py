class Graph():
    def __init__(self, num):
        # the vertices is from 0 to (num-1)
        self.graph = {i:[] for i in range(num)}
        self.num = num
        self._imp_cnt = 0 # track how many call of isCycleUntil
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def isCycleUntil(self, node, visited):
        self._imp_cnt += 1
        # print(self._imp_cnt)

        # base case: if the node has be visited, find a cycle!
        if visited[node]:
            return True

        # mark node as visited
        visited[node] = True

        # enter to neighbors
        neighbors = self.graph[node]
        for nei in neighbors:
            if self.isCycleUntil(nei, visited):
                return True

        # if node's neighbors do not have cycle, backtrack
        visited[node] = False

        # optional: this neighbors of this node have been explored, clear the neighbors for performance improvement
        self.graph[node] = []

        # no clcye found
        return False
    
    def checkCycle(self):
        visited = [False] * self.num
        # iterate every node as the start point of path
        for node in range(self.num):
            if self.isCycleUntil(node, visited): 
                return True
        return False

# test code
if __name__ == '__main__':
    g = Graph(8)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(4, 5)
    g.addEdge(5, 6)
    g.addEdge(6, 4)
    g.addEdge(7, 6)
    if g.checkCycle():
        print("Graph has a cycle")
    else:
        print("Graph has no cycle")
    # ans: Graph has a cycle
    
    
            



