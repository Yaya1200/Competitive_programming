class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x

        if target < 0:
            return -1

        i = 0
        current = 0
        value = -1
        j = 0

        for i in range(len(nums)):
            current += nums[i]

            while current > target:
                current -= nums[j]
                j += 1

            if current == target:
                value = max(value, i - j + 1)

        return len(nums) - value if value != -1 else -1