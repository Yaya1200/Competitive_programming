class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        i = 0
        totals = 0
        hash_map = {}
        for j in range(len(nums)):
            hash_map[nums[j]] = hash_map.get(nums[j], 0) + 1
            if 0 in hash_map:
                while hash_map[0] > k:
                   if nums[i] == 0:
                     hash_map[0] -= 1
                   i += 1
            totals = max(totals, j-i+1)
        return totals


        