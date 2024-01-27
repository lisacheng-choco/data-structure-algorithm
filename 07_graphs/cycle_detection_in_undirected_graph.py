class Graph_DFS():
    def __init__(self, num):
        self.graph = {i: [] for i in range(num)}
        self.num = num
    

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    

    def isCyclicUntil(self, node, visited, parent):
        # base case
        if visited[node]:
            return True
        
        # mark node as visited
        visited[node] = True

        # enter to neighbors
        for nei in self.graph[node]:
            # !!
            if nei == parent:
                continue
            if self.isCyclicUntil(nei, visited, node):
                return True

        return False
        
    
    def checkCycle(self):
        visited = [False] * self.num
        for node in range(self.num):
            # !!
            if visited[node]:
                continue
            if self.isCyclicUntil(node, visited, -1):
                return True
        return False


class Graph_UF():
    def __init__(self, edges):
        self.edges = edges
        self.ancestors = [i for i in range(len(self.edges)+1)]
        self.rankings = [0] * (len(self.edges)+1)
    
    def find(self, n):
        ancestor = self.ancestors[n]
        if ancestor == n:
            return n
        self.ancestors[n] = self.find(ancestor)
        return self.ancestors[n]

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if self.rankings[u] < self.rankings[v]:
            self.ancestors[u] = v
            self.rankings[v] += 1
        else:
            self.ancestors[v] = u
            self.rankings[u] += 1

    def checkCycle(self):
        for u, v in self.edges:
            if self.find(u) == self.find(v):
                return True
            self.union(u, v)
        return False


# test code
if __name__ == '__main__':
    # test case 1
    g = Graph_DFS(8)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(4, 5)
    g.addEdge(5, 6)
    g.addEdge(6, 4)
    g.addEdge(7, 6)
    
    if g.checkCycle():
        print("Test case 1: Graph contains cycle")
    else:
        print("Test case 1: Graph doesn't contain cycle ")
    # ans: Graph contains cycle
    
    # test case 2
    g1 = Graph_DFS(3)
    g1.addEdge(0, 1)
    g1.addEdge(1, 2)
    # ans: Graph doesn't contain cycle
    
    if g1.checkCycle():
        print("Test case 2: Graph contains cycle")
    else:
        print("Test case 2: Graph doesn't contain cycle ")

    # test case 3
    g3 = Graph_UF([
        [0, 1],
        [0, 2],
        [1, 2]
    ])
    if g3.checkCycle():
        print("Test case 3: Graph contains cycle")
    else:
        print("Test case 3: Graph doesn't contain cycle ")


    # test case 3
    g4 = Graph_UF([
        [0, 1],
        [1, 2],
        [1, 3]
    ])
    if g4.checkCycle():
        print("Test case 4: Graph contains cycle")
    else:
        print("Test case 4: Graph doesn't contain cycle ")
