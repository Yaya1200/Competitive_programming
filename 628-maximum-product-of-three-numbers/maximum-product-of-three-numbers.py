class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums1 = sorted(nums)
        output = []
        output.append(nums1[0])
        output.append(nums1[1])
        output.append(nums1[2])
        if len(nums1) == 4:
            output.append(nums1[-1])
        elif len(nums1) == 5:
            output.append(nums1[-1])
            output.append(nums1[-2])
        elif len(nums1) > 5:
            output.append(nums1[-1])
            output.append(nums1[-2])
            output.append(nums1[-3])
        
        maxValue = -float('inf')
        for i in range(len(output)-2):
            for j in range(i+1, len(output)-1):
                for k in range(j+1, len(output)):
                    value = output[i]*output[j]*output[k]
                    maxValue = max(value, maxValue)
                  
                    
        return maxValue


       
      