class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = 0
        for i in range(len(nums)):
            if i > last:
                return False
            last = max(last, i+nums[i])
            
        return True