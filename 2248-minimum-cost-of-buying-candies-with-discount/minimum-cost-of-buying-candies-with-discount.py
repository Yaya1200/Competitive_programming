class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        output = 0 
        if len(cost) < 3:
            return sum(cost)
        cost1 = sorted(cost)
        for i in range(len(cost1)-1,0,-3):
            output += cost1[i] + cost1[i-1]
            cost1.pop(i)
            if len(cost1) > 0:
                cost1.pop(i-1)
            if len(cost1) > 0:
                cost1.pop(i-2)
        return output + sum(cost1[:])

        