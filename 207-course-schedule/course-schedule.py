class Solution:
    def canFinish(self, numCourses, prerequisites):

        indegree = {}

        for i in range(numCourses):
            indegree[i] = 0

        for course, pre in prerequisites:
            indegree[course] += 1

        processed = 0

        while True:

            found = False

            for course in indegree:

                if indegree[course] == 0:

                    found = True
                    processed += 1

                    indegree[course] = -1

                    for c, p in prerequisites:
                        if p == course:
                            indegree[c] -= 1

            if not found:
                break

        return processed == numCourses