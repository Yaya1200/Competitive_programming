class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        a,b = intervals[0]
        count = 0
        for i in range(1,len(intervals)):
            c,d = intervals[i]
            value1 = max(a,c)
            value2 = min(b, d)
            if value1 < value2:
                count += 1
                a = min(a,c)
                b = min(b, d)
            else:
                a = c
                b = d
          
        return count


            