class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
       output = float('inf')
       j = 0
       sum_1 = 0
       for i in range(len(nums)):
            sum_1 += nums[i]
            if sum_1 >= target:
                output = min(i+1 - j, output)
                while target < sum_1:
                    sum_1 -= nums[j]
                    j+=1
                    if sum_1 >= target:
                        output = min(i+1 - j, output)
                    
       if output == float("inf"):
        return 0
       else: 
         return output

