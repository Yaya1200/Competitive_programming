class Solution:
    def finalString(self, s: str) -> str:
        value = []
        for i in range(len(s)):
            if s[i] == 'i':
                i,j = 0, len(value)-1
                while(i<j):
                    value[i], value[j] = value[j], value[i]
                    i+=1
                    j-=1
            else:
                value.append(s[i])
        return "".join(value)
        