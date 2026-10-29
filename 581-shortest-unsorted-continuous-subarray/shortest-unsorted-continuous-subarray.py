
class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        left = -1
        right = -1

        maximum = float('-inf')
        minimum = float('inf')

        for i in range(len(nums)):
            if nums[i] < maximum:
                right = i
            else:
                maximum = nums[i]

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > minimum:
                left = i
            else:
                minimum = nums[i]

        return 0 if right == -1 else right - left + 1
