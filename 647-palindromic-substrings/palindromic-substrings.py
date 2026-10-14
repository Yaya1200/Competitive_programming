class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [0] * len(s)
        for i in range(len(s)):
            if dp[i-1]:
                dp[i] = dp[i-1]
            for j in range(i, -1, -1):
                if s[j:i+1] == s[j:i+1][::-1]:
                    dp[i] += 1
        return dp[-1]
        