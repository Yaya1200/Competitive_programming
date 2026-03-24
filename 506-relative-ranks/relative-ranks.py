class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        value = []
        score1 = sorted(score)
        output = []
        for i in range(len(score1)):
            if len(score1)-i == 3:
                 value.append("Bronze Medal")
            elif len(score1)-i == 2:
                 value.append("Silver Medal")
            elif len(score1)-i == 1:
                 value.append("Gold Medal")
            else:
                value.append(str(len(score1) - i))
        for j in range(len(score)):
            for i in range(len(score1)):
                if score[j] == score1[i]:
                    output.append(value[i])
        return output


        