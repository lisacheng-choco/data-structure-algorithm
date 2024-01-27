'''
To build a graph, two approaches
1. Adjacent List
2. Adjacent Matrix
'''

class GraphAdjList:
    def __init__(self, directed=False):
        self.adjList = {}
        self.directed = directed
    
    def addNode(self, n):
        self.adjList[n] = []
    
    def addEdge(self, u, v, weight):
        self.adjList[u].append((v, weight))
        if not self.directed:
            self.adjList[v].append((u, weight))
        

