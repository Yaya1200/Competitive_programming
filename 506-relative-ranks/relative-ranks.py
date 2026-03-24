class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        hash_map = {}
        score1 = sorted(score)
        output = []
        for i in range(len(score1)):
            if len(score1)-i == 3:
                 hash_map[score1[i]] = "Bronze Medal"
            elif len(score1)-i == 2:
                 hash_map[score1[i]] = "Silver Medal"
            elif len(score1)-i == 1:
                 hash_map[score1[i]] = "Gold Medal"
            else:
                hash_map[score1[i]] = (str(len(score1) - i))
        for j in score:
            output.append(hash_map[j])
        return output


        