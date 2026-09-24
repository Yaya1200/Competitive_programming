class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):

            for k in wordDict:

                if i >= len(k) and dp[i - len(k)]:
                    if s[i - len(k):i] == k:
                        dp[i] = True
                        break

        return dp[len(s)]




        
        
                



        
            

                