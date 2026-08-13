class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        intervals.sort()
        for i in intervals:
            if not output:
                output.append(i)
            if output[-1][1] >= i[0]:
                output[-1][1] = max(output[-1][1], i[1])
            else:
                output.append(i)
        return output

        
        