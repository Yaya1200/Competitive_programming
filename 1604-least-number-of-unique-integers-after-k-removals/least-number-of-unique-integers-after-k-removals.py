class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        hash_map = {}

        for i in arr:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1

        sorted_hash_map = dict(
            sorted(hash_map.items(), key=lambda x: x[1])
        )

        for i in sorted_hash_map:
            if sorted_hash_map[i] <= k:
                k -= sorted_hash_map[i]
                sorted_hash_map[i] = 0
            else:
                sorted_hash_map[i] -= k
                k = 0
                break

        count = 0

        for i in sorted_hash_map:
            if sorted_hash_map[i] > 0:
                count += 1

        return count

                
