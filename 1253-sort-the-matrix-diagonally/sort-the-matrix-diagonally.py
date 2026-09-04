class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        value = []

        
        for i in range(len(mat[0])):
            j = 0
            c = i

            while j < len(mat) and c < len(mat[0]):
                value.append(mat[j][c])
                j += 1
                c += 1

            value = sorted(value)

            j = 0
            c = i
            k = 0

            while j < len(mat) and c < len(mat[0]):
                mat[j][c] = value[k]
                j += 1
                c += 1
                k += 1

            value = []

       
        for i in range(1, len(mat)):
            j = i
            c = 0

            while j < len(mat) and c < len(mat[0]):
                value.append(mat[j][c])
                j += 1
                c += 1

            value = sorted(value)

            j = i
            c = 0
            k = 0

            while j < len(mat) and c < len(mat[0]):
                mat[j][c] = value[k]
                j += 1
                c += 1
                k += 1

            value = []

        return mat

