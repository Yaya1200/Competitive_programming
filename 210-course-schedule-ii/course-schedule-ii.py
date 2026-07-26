class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        output = []
        queue = deque()
        indegree = {}
        graph = [[] for i in range(numCourses)]
        for i in range(numCourses):
            indegree[i] = 0
        for courses, pre in prerequisites:
            indegree[courses] += 1
        for courses, pre in prerequisites:
            graph[pre].append(courses)
        for i in indegree:
            if indegree[i] == 0:
                queue.append(i)
        if not queue:
            return []
        processed = 0
        while queue:
            course = queue.popleft()
            output.append(course)
            processed += 1
            for neb in graph[course]:
                indegree[neb] -= 1
                if indegree[neb] == 0:
                    queue.append(neb)
        if processed == numCourses:
           return output
        else:
            return []



        
            

        