class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        output = []
        i = 0
        j = 0
        flag = 0
        while i < len(pushed) and flag == 0:
            output.append(pushed[i])
            while j < len(popped) and output:
                if output[-1] == popped[j]:
                    j+= 1
                    output.pop()
                elif i == len(pushed):
                    flag = 1
                else:
                    break
            i+=1
        
        if len(output) == 0:
            return True
        else:
            return False     


        