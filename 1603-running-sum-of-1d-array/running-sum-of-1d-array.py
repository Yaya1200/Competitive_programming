class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        value = 0
        for i in range(len(nums)):
            value += nums[i]
            output.append(value)
        return output