class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
      distances = []
      output = []
      for x in points:
            distance = x[0]*x[0] + x[1]*x[1]
            distances.append([distance, x])
      i = 0
      heapq.heapify(distances)
      while i < k:
          output.append(heapq.heappop(distances)[1])
          i+=1
      return output
      