class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        output = []
        i = 0
        j = 0

        while i < len(firstList) and j < len(secondList):
            a, b = firstList[i]
            c, d = secondList[j]

            start = max(a, c)
            end = min(b, d)

            if start <= end:
                output.append([start, end])

            if b < d:
                i += 1
            else:
                j += 1

        return output




        
        
        
        