class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        output = []
        output1 = []
        if rowIndex == 0:
            return [1]
        else:
            while rowIndex > 0:
                output1 = [1]
                for j in range(len(output)-1):
                    output1.append(output[j] + output[j+1])
                output1.append(1)
                output = output1[:]
                output1 = []
                rowIndex -=1
            return output


        