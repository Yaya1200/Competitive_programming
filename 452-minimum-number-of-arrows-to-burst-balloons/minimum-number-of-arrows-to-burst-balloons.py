class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
       points.sort()
       count = 1
       index = points[0][1]
       for i in range(1,len(points)):
          if points[i][0] > index:
            count += 1
            index = points[i][1]
          else:
                index = min(index, points[i][1])
       return count



        