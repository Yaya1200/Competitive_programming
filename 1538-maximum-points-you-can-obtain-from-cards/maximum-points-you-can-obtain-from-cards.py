class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        value1 = cardPoints[:k]
        value2 = cardPoints[len(cardPoints)-k:]
        sum1 = sum(value1)
        sum2 = sum(value2)
        maximum = max(sum1, sum2)
        for i in range(len(value1)):
            sum2 = value1[i] + sum2 - value2[i]
            maximum = max(maximum, sum2)

        for i in range(len(value1)-1, -1, -1):
            sum1 = value2[i] + sum1 - value1[i]
            maximum = max(maximum , sum1)
        return maximum
                

                