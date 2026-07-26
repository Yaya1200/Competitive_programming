class Solution:
    def canFinish(self, numCourses, prerequisites):

        indegree = {}
        Queue = deque()
        for i in range(numCourses):
            indegree[i] = 0
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
              graph[pre].append(course)
        for course, pre in prerequisites:
            indegree[course] += 1

        for i in indegree:
            if indegree[i]== 0:
                Queue.append(i)
        if not Queue:
            return False
        
        processed = 0
        while Queue:
            course = Queue.popleft()
            processed += 1
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    Queue.append(neighbor)
        return processed == numCourses