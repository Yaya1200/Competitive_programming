class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        output = []
        stack = []
        top = 0
        for i in s:
            if i == "(":
                stack.append(i)
                top += 1
            else:
                top -= 1
                stack.append(i)
            if top == 0:
                output.append(stack[1:len(stack)-1])
                top = 0
                stack = []
        result = ""
        for i in output:
            k = "".join(i)
            result+= k
        return result


