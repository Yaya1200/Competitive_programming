class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash_map = {}
        output = 0
        for i in s:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        for i in hash_map:
            if hash_map[i] % 2 == 0:
                output += hash_map[i]
            else:
                output+= hash_map[i]-1
        return output if len(s) == output else output+1
        
        