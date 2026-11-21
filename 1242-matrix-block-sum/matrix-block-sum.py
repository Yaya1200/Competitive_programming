
class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:

        m, n = len(mat), len(mat[0])

        matrix = [[0] * (n + 1) for _ in range(m + 1)]
        output = [[0] * n for _ in range(m)]

        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                matrix[i][j] = (
                    matrix[i-1][j]
                    + matrix[i][j-1]
                    - matrix[i-1][j-1]
                    + mat[i-1][j-1]
                )

        for i in range(m):
            for j in range(n):

                r1 = max(0, i-k)
                c1 = max(0, j-k)
                r2 = min(m-1, i+k)
                c2 = min(n-1, j+k)

                output[i][j] = (
                    matrix[r2+1][c2+1]
                    - matrix[r1][c2+1]
                    - matrix[r2+1][c1]
                    + matrix[r1][c1]
                )

        return output
