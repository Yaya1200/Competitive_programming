class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
       edges = {}
       queue = deque()
       output = []
       graph1 = [[] for _ in graph]
       for i in range(len(graph)):
          edges[i] = len(graph[i])
       for i in range(len(graph)):
         for j in graph[i]:
            graph1[j].append(i)
       for i in edges:
            if edges[i] == 0:
                queue.append(i)
       while queue:
            indegree = queue.popleft()
            output.append(indegree)
            for values in graph1[indegree]:
                edges[values] -= 1
                if edges[values] == 0:
                    queue.append(values) 
       return sorted(output)
        
        