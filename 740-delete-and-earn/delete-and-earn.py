class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        hash_map = {}

        for i in nums:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1

        max_num = max(nums)
        points = [0] * (max_num + 1)

        for i in hash_map:
            points[i] = i * hash_map[i]

        dp = [0] * (max_num + 1)

        dp[1] = points[1]

        for i in range(2, max_num + 1):

            option1 = dp[i - 1]

            option2 = dp[i - 2] + points[i]

            dp[i] = max(option1, option2)

        return dp[max_num]