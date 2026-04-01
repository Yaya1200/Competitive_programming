class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        output = []
        for i in range(len(nums)-1, -1, -1):
            if sum(nums[i:]) > sum(nums[:i]):
                for j in nums[i:]:
                    output.append(j)
                return sorted(output, reverse=True)
       
                
