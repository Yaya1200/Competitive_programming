class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        degree = [0] * n
        graph = [[] for _ in range(n)]

        for i, j in edges:
            degree[i] += 1
            degree[j] += 1
            graph[i].append(j)
            graph[j].append(i)

       
        queue = deque()

        for i in range(n):
            if degree[i] == 1:
                queue.append(i)

        remaining = n

        while remaining > 2:
            size = len(queue)
            remaining -= size

            for _ in range(size):
                leaf = queue.popleft()

                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1

                    if degree[neighbor] == 1:
                        queue.append(neighbor)

        return list(queue)