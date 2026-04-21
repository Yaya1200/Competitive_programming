class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        n=len(s)
        result=""
        i=0
        top=0

        while i<n:

            if s[i]=='(':
                top+=1
                if top>1:
                    result+=s[i]
            else:
                top-=1
                if top>0:
                    result+=s[i]
            i+=1
                
   
        return result
        