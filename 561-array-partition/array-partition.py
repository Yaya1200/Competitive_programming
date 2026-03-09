class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        value = sorted(nums)
        output = 0
        for i in range(0,len(nums)-1,2):
            output += value[i]
        return output


        