class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        count1 = 0
        count2 = 0
        value1 = True
        value2 = True
        while i < j:
            if s[i] != s[j]:
                count1 += 1
                if j-1 > i and s[i] == s[j-1]:
                    j -= 1
                else:
                    i+= 1
            else:
                i+= 1
                j -= 1
            if count1 == 2:
                value1 = False
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                count2 += 1
                if i+1 < j and s[i+1] == s[j]:
                    i += 1
                else:
                    j -= 1
            else:
                i+= 1
                j -= 1
            if count2 == 2:
                value2 = False
        print(value1)
        print(value2)
        return value1 or value2
        

        