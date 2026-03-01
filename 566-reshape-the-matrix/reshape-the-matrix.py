class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        output = []
        if r*c != len(mat)*len(mat[0]):
            return mat
        mat = [num for row in mat for num in row]
        i = 0
        j = 0
        k = 0
        while i < r:
            value = []
            while j < c:
                value.append(mat[k])
                k+= 1
                j += 1
            i += 1
            j = 0
            output.append(value)
        return output
