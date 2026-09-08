class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))

        current_max = 1
        count = 1

        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i] + 1:
                count += 1
            else:
                count = 1

            current_max = max(current_max, count)

        return current_max
            
          
