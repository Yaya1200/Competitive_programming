class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_value = 0
        index = 0
        for i in range(len(nums)):
            if max_value < nums[i]:
                max_value = nums[i]
                index = i
        for i in nums:
            if max_value < i*2 and max_value != i:
                return -1
        return index
        