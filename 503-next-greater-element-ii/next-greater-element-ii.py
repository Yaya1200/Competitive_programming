class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        output = []
        stack = []
        for i in range(len(nums)):
            k = (i+1)% (len(nums))
            flag = 0
            while k != i:
                if nums[i] < nums[k]:
                    output.append(nums[k])
                    flag = 1
                    break
                k = (k+1)%len(nums)
            if flag == 0:
                output.append(-1)
        return output
            

            
                


        