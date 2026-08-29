class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        j = len(s)-1
        value = ""
        while s[i] == " ":
            i += 1
        while s[j] == " ":
            j -= 1
        value1 = ""
       
        while j >= i:
            if s[j] != " ":
              value1 =  s[j] + value1
            elif value1:
                value += value1 + " "
                value1 = ""
            j -= 1
        return value+value1
        
        