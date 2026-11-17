class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:

        def atMost(k):
            if k < 0:
                return 0

            left = 0
            summation = 0
            count = 0

            for right in range(len(nums)):
                summation += nums[right]

                while summation > k:
                    summation -= nums[left]
                    left += 1

                count += right - left + 1

            return count

        return atMost(goal) - atMost(goal - 1)

        
        
       
        return count

        