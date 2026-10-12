class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        def moveforward():
            nonlocal top, bottom, left, right
            for j in range(left, right + 1):
                output.append(matrix[top][j])
            top += 1

        def movedownward():
            nonlocal top, bottom, left, right
            for i in range(top, bottom + 1):
                output.append(matrix[i][right])
            right -= 1

        def movebackward():
            nonlocal top, bottom, left, right
            for j in range(right, left - 1, -1):
                output.append(matrix[bottom][j])
            bottom -= 1

        def moveupward():
            nonlocal top, bottom, left, right
            for i in range(bottom, top - 1, -1):
                output.append(matrix[i][left])
            left += 1

        while top <= bottom and left <= right:
            moveforward()

            if top <= bottom:
                movedownward()

            if left <= right and top <= bottom:
                movebackward()

            if top <= bottom and left <= right:
                moveupward()

        return output