class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        values = ["+", "/", "*", "-"]
        output = []
        for i in tokens:
            if i not in values:
                output.append(i)
            else:
                a = int(output[-2])
                b = int(output[-1])
                if i == "+":
                    output[-2] = str(a + b)
                elif i == "-":
                    output[-2] = str(a - b)
                elif i == "*":
                    output[-2] = str(a * b)
                elif i == "/":
                    output[-2] = str(int(a / b))
                output.pop()
           
        return int(output[0])


        