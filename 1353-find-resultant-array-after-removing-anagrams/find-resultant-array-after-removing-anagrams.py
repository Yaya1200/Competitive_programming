class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        "submittion" 
        output = []
        output.append(words[0])
        j = 0
        for i in range(1, len(words)):
            if sorted(words[i]) != sorted(output[j]):
                j += 1
                output.append(words[i])
        return output
