class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        nums = sorted(nums)
        value = float('inf')
        for i in range(len(nums)-k+1):
            value = min(value, abs(nums[i+k-1] - nums[i]))
        return value
        