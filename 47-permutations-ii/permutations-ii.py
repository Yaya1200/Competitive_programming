class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(path, indexes):
            if len(path) == len(nums) and path not in result:
                result.append(path[:])
                indexes = []
                return
            for i in range(len(nums)):
                if i in indexes:
                    continue
                path.append(nums[i])
                indexes.append(i)
                backtrack(path, indexes)
                path.pop()
                indexes.pop()
        backtrack([],[])
        return result

        