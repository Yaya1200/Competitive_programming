class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        result = float('inf')
        while left <= right:
            mid = left + (right - left)//2
            count = 0
            for i in range(len(nums)):
                count += (nums[i] + mid -1)// mid
            if count > threshold:
                left = mid+1
            else:
                right = mid-1
        return left
            
        