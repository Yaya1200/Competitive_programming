class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        hash_map = {0: -1}
        prefix = 0
        maximum = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                prefix -= 1
            else:
                prefix += 1

            if prefix in hash_map:
                maximum = max(maximum, i - hash_map[prefix])
            else:
                hash_map[prefix] = i

        return maximum