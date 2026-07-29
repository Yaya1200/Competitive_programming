class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for  i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        visited = set()
        queue = deque()
        visited.add(source)
        queue.append(source)
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            for neb in graph[node]:
                if neb in visited:
                    continue
                queue.append(neb)
                visited.add(neb)
        return False
            
        