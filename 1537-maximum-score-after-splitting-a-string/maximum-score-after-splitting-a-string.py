class Solution:
    def maxScore(self, s: str) -> int:
        output = []
        value = 0
        value1 = 0
        max_score = 0
        for i in range(len(s)-1):
            if s[i] == "0":
                value += 1
            output.append(value)
        for i in range(len(s)-1, 0, -1):
            if s[i] == "1":
                value1 += 1
            output[i-1] += value1
            max_score = max(output[i-1], max_score)
        return max_score
        

