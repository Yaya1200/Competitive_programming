class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        maximum = float('-inf')
        
        suffix_max = [0] * len(nums)
        suffix_max[-1] = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            suffix_max[i] = max(nums[i], suffix_max[i + 1])

        for i in range(len(nums) - k):
            maximum = max(maximum, nums[i] + suffix_max[i + k])

        return maximum