class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        output = []
        for i in image:
            value = []
            for j in range(len(i)-1, -1, -1):
                if i[j] == 1:
                    value.append(0)
                else:
                    value.append(1)
            output.append(value)
        return output


        