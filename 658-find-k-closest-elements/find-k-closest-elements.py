class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
       output1 = []
       output2 = []
       result = []
       for i in range(len(arr)):
           if arr[i] > x:
             output2.append(arr[i])
           else:
             output1.append(arr[i])
       output1.sort(reverse=True)
       output2.sort()
       while (output1 or output2) and len(result) < k:
          if output1 and output2:
            if abs(output1[0] - x) <= abs(output2[0] - x):
                result.append(output1.pop(0))
            else:
                result.append(output2.pop(0))
          else:
             if output1:
                result.append(output1.pop(0))
             else:
                result.append(output2.pop(0))

       return sorted(result)
         

