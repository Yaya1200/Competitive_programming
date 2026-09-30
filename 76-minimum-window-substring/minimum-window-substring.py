class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_map1 = {}
        hash_map2 = {}

        for char in t:
            if char in hash_map1:
                hash_map1[char] += 1
            else:
                hash_map1[char] = 1

        i = 0
        j = 0

        best_left = 0
        best_length = float("inf")

        while j < len(s):

            hash_map2[s[j]] = hash_map2.get(s[j], 0) + 1

            while all(
                hash_map2.get(c, 0) >= count
                for c, count in hash_map1.items()
            ):

                if j - i + 1 < best_length:
                    best_length = j - i + 1
                    best_left = i

                hash_map2[s[i]] -= 1
                i += 1

            j += 1

        if best_length == float("inf"):
            return ""

        return s[best_left:best_left + best_length]
