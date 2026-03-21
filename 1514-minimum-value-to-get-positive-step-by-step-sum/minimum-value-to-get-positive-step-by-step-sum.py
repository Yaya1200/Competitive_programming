class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        value = 0
        min_num = 0
        for i in nums:
            value += i
            min_num = min(value, min_num)
        return 1-min_num

