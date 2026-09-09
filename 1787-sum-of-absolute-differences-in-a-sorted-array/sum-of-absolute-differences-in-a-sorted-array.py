class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left_sum = 0
        output = []

        for i, x in enumerate(nums):
            left = x * i - left_sum

            right_sum = total - left_sum - x
            right_count = len(nums) - i - 1
            right = right_sum - x * right_count

            output.append(left + right)

            left_sum += x

        return output
        
        return output
        
