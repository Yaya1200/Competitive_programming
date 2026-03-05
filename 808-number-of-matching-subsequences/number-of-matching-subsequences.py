class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        l = 0
        j = 0
        count = 0
        hash_map = {}
        for i in range(len(words)):
            if words[i] in hash_map:
                hash_map[words[i]] += 1
            else:
                hash_map[words[i]] = 1
    
        words = set(words)
        words = list(words)
        for i in words:
            while l < len(s) and j < len(i):
                if i[j] == s[l]:
                    j+=1
                l+=1
            if j == len(i):
                count += hash_map[i]
            j = 0
            l = 0
        return count

        