class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        output = []
        for i in range(len(mat)):
            output.append(mat[i][i])
        j = len(mat)-1
        for i in range(len(mat)):
            if i != j-i:
             output.append(mat[i][j-i]) 
        return sum(output)
        