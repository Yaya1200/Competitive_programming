
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        total = 0
        maximum = 0
        hash_map = {}
        i = 0
        j = 0
        result = 0

        while i < len(s):
            if s[i] in hash_map:
                hash_map[s[i]] += 1
            else:
                hash_map[s[i]] = 1

            total += 1
            maximum = max(maximum, hash_map[s[i]])

            if total - maximum > k:
                hash_map[s[j]] -= 1
                total -= 1
                j += 1

            result = max(result, total)
            i += 1

        return result


        