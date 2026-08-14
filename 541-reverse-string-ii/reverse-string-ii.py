class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        output = ""
        i = 0

        while i < len(s):
            output += s[i:i+k][::-1]
            output += s[i+k:i+2*k]
            i += 2*k

        return output