class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        output = []
        count = 0
        for i in range(len(s)-2):
            value = s[i:i+3]
            for x in value:
                if x not in output:
                    output.append(x)
            output = set(output)
            if len(output) == 3:
                count += 1
            output = []
        return count

        