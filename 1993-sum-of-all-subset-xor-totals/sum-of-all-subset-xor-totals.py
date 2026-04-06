class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = []
        output = []
        def backtrack(path, start):
            result.append(path[:])
            if len(path) == len(nums):
                 return
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(path, i+1)
                value = path[0]
                for j in range(1, len(path)):
                    value = value^path[j]
                output.append(value)
                path.pop()
        backtrack([], 0)
        return sum(output)

        