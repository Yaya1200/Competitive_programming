class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        value = [0] * 1001
        for i in ranges:
            value[i[0]] += 1
            value[i[1]+1] -= 1
        for i in range(1,len(value)):
            value[i] += value[i-1]
        if 0 in value[left : right+1]:
            return False
        else:
            return True
            


        