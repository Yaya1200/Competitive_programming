class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        zeros = 0
        result = 0
        j = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            if zeros == 2:
                while zeros > 1:
                    if nums[j] == 0:
                        zeros -= 1
                    j += 1
            if zeros:
              result = max(result, i - j + 1-zeros)
            else:
                result = max(result, i - j )
        return result

        