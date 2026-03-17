class Solution:
    def maxScore(self, s: str) -> int:
        output = []
        value0 = 0
        result = 0
        for i in range(len(s)-1):
            if s[i] == "0":
                value0 += 1
            output.append(value0)
        value1 = 0
        for i in range(len(s)-1,0,-1):
            if s[i] == "1":
                value1 += 1
            output[i-1] += value1
            result = max(result, output[i-1])
        return result

        