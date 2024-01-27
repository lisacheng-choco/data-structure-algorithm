class UnionFind():
    def __init__(self, numOfNodes):
        self.ancestors = [i for i in range(numOfNodes)]
        self.ranking = [1] * numOfNodes

    def find(self, n):
        '''
        - time complexity: O(log v), v = the number of nodes
        '''
        ancestor = self.ancestors[n]
        if ancestor == n:
            return ancestor
        self.ancestors[n] = self.find(ancestor)

        return self.ancestors[n]

    def union(self, u, v):

        u = self.find(u)
        v = self.find(v)

        if u == v:
            return False

        if self.ranking[u] < self.ranking[v]:
            self.ancestors[u] = v
            self.ranking[v] += 1
        else:
            self.ancestors[v] = u
            self.ranking[u] += 1

        return True
        

def kruskalsAlgo(edges, numOfNodes):
    '''
    - time complexity: O(e*log e + e* log v)
    - space complexity: O(v)
    '''
    edges.sort() # time complexity: O(elog e)
    edgeCount = 0
    MSTedges = []
    uf = UnionFind(numOfNodes)

    minWeight = 0
    for weight, u, v in edges: # O(e)
        if uf.union(u, v): # O(log v)
            minWeight += weight
            edgeCount += 1
            MSTedges.append((u, v))
            if edgeCount == numOfNodes-1:
                return minWeight

    return minWeight


if __name__ == "__main__":
    edges = [
        # weight, node1, node2
        [2, 0, 2],
        [6, 0, 3],
        [5, 1, 2],
        [1, 1, 4],
        [2, 2, 3],
        [3, 3, 4],
    ]
    numOfNodes = 5
    print("minimum total weight", kruskalsAlgo(edges, numOfNodes))
            
"""
output:
('edges in MST', [(1, 4), (0, 2), (2, 3), (3, 4)])
('minimum total weight', 8)
"""