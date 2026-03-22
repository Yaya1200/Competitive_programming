class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        output = []
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        for i in nums:
            if i not in output:
                output.append(i)
        if len(output) - 3 >= 0:
            return output[len(output)-3]
        else:
            return output[-1]