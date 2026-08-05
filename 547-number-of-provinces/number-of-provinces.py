class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union_set(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            self.parent[rootY] = rootX
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = UnionFind(n)
        numberOfComponents = n
        for i in range(n):
           for j in range(i+1, n):
               if  isConnected[i][j] and dsu.find(i) != dsu.find(j):
                    numberOfComponents -= 1
                    dsu.union_set(i, j)
        return numberOfComponents