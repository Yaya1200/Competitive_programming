class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = 0
        start_value = 1
        i = 0
        prefix_sum = start_value
        while(i < len(nums)):
            prefix_sum += nums[i]
            i+= 1
            if prefix_sum < 1:
                start_value += 1
                prefix_sum = start_value
                i = 0
        return start_value
            

