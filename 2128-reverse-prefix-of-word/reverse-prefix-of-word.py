class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        result = ""+ch
        if ch not in word:
            return word
            
        else:
            for i in range(len(word)):
                if word[i] != ch:
                    stack.append(word[i])
                else:
                    for j in range(len(stack)-1, -1, -1):
                        result += stack[j]
                    result += word[i+1:] 
                    return result
                 
                
