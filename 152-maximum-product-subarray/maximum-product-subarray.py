class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [nums[0], nums[0]]
        result = nums[0]

        for i in range(1, len(nums)):
            old_min = dp[0]
            old_max = dp[1]

            dp[0] = min(nums[i], old_min * nums[i], old_max * nums[i])
            dp[1] = max(nums[i], old_min * nums[i], old_max * nums[i])

            result = max(result, dp[1])

        return result
            