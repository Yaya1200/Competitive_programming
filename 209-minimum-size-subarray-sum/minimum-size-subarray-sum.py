class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        value = 0
        result = float('inf')
        for j in range(len(nums)):
            value += nums[j]
            while value > target:
                if value - nums[i] >= target:
                    value -= nums[i]
                    i+=1
                else:
                    break
            if value >= target:
                result = min(j+1 - i, result)
        if result == float("inf"):
            return 0
        else:
            return result
        

        