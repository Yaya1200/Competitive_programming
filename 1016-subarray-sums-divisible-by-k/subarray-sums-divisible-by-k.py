class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        hash_map = {0:1}
        prefix = 0
        count = 0
        for i in nums:
            prefix += i
            remender = prefix % k
            if remender in hash_map:
                count += hash_map[remender]
                hash_map[remender] += 1
            else:
                hash_map[remender] = 1
        return count