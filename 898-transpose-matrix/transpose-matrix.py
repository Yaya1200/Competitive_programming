class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        output = []
        value = []
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                value.append(matrix[j][i])
            output.append(value)
            value = []
        return output
        