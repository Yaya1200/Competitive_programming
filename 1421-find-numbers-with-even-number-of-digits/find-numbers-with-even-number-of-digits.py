class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            value = 0
            while(i > 0):
               i =  i // 10 
               value += 1
            if value % 2 == 0:
                count += 1
        return count
        