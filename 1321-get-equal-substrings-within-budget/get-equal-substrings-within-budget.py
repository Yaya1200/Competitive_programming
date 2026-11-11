class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        total = 0
        j = 0
        count = 0
        for i in range(len(s)):
            count += abs(ord(s[i]) - ord(t[i]))
            while count > maxCost:
                count -= abs(ord(s[j])- ord(t[j]))
                j += 1
            total = max(total, i-j+1)
        return total
