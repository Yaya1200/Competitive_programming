class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        output = []
        result = []
        for i in range(len(nums)):
            output.append([-nums[i], i])
        j = 0
        heapq.heapify(output)
        while j < k:
          result.append([output[0][1], -output[0][0]])
          heapq.heappop(output)
          j+=1
        output = []
        for i in sorted(result):
            output.append(i[1])
        return output
