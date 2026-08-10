class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        def rob_linear(arr):
            dp = [0] * len(arr)

            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

            return dp[-1]

        return max(rob_linear(nums[:-1]),rob_linear(nums[1:]))
        