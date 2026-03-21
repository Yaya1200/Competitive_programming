class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
       output = float('inf')
       j = 0
       sum_1 = 0
       for i in range(len(nums)):
                sum_1 += nums[i]
                while target <= sum_1:
                    output = min(i+1 - j, output)
                    sum_1 -= nums[j]
                    j+=1         
       if output == float("inf"):
        return 0
       else: 
         return output

