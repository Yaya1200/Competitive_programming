class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        values = {0: -1}
        prefix = 0

        for i in range(len(nums)):
            prefix += nums[i]
            remainder = prefix % k

            if remainder in values:
                if i - values[remainder] >= 2:
                    return True
            else:
                values[remainder] = i

        return False
        