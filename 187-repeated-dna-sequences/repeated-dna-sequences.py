class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        output = []
        for i in range(len(s)-9):
            if s[i:i+10] in s[i+1:]:
                output.append(s[i:i+10])
        return list(set(output))

            