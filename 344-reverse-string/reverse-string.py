class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []
        j = 0
        for i in range(len(s)):
            stack.append(s[i])
        for i in range(len(s)-1, -1, -1):
            s[j] = stack[i]
            j+= 1
        
