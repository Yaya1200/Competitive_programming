class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0

        dp = [[] for _ in range(len(nums))]

        dp[0].append(nums[0])
        dp[0].append(-nums[0])

        for i in range(1, len(nums)):
            for value in dp[i - 1]:
                dp[i].append(value - nums[i])
                dp[i].append(value + nums[i])

        for value in dp[-1]:
            if value == target:
                count += 1

        return count