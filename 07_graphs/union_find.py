class UnionFind:
    def __init__(self, num):
        self.parents = [i for i in range(num)] # index: node數字， value: node的大家長
        self.ranks = [0] * num
    
    def find(self, element): # 回傳element的大家長
        '''
        - time complexity: O(1)
        - space complexity: O(1)
        '''
        return self._find(element)

    def _find(self, node):
        # path comression
        parent = self.parents[node]
        if parent == node: # 找到大家長了！ 
            return node
        self.parents[node] = self._find(parent)

        return self.parents[node] 

    def union(self, u, v): # 合併兩棵樹：找到兩棵樹的家長，把ranking小的家長掛到ranking大的家長底下
        '''
        - time complexity: O(1)
        - space complexity: O(1)
        '''
        u_parent = self.find(u)
        v_parent = self.find(v)

        if self.ranks[u_parent] < self.ranks[v_parent]:
            # 把 rank 小的掛到 rank 大的下方
            self.parents[u_parent] = v_parent
            self.ranks[v_parent] += 1
        else:
            self.parents[v_parent] = u_parent
            self.ranks[u_parent] += 1

# Example usage:
num = 5
uf = UnionFind(num)

# Perform some union operations
uf.union(0, 1)
uf.union(2, 3)
uf.union(0, 4)

# Check if elements are in the same set
print(uf.find(1) == uf.find(4))  # True
print(uf.find(2) == uf.find(3))  # True
print(uf.find(0) == uf.find(2))  # False



