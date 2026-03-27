class Solution:
    def countElements(self, nums: List[int]) -> int:
        hash_map = {}
        count = 0
        for i in nums:
            if i not in hash_map:
                hash_map[i]  = 1
            else:
                hash_map[i] += 1
        nums = sorted(list(set(nums)))
        for i in range(1, len(nums)-1):
            count += hash_map[nums[i]] 
        return count

