class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        temp = [ row[:] for row in board]
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                k = i - 1
                while k <= i+1:
                    l = j -1
                    while l <= j+1:
                        if (k >= 0) and (k < len(board))and (l >= 0) and (l < len(board[0])) and not((l == j) and (k == i)) and (temp[k][l] == 1):
                            count += 1
                        l += 1
                    k += 1
                if count < 2 and board[i][j] == 1:
                    board[i][j] = 0
                elif (count > 3) and board[i][j] == 1:
                    board[i][j] = 0
                elif count == 3 and board[i][j] == 0:
                     board[i][j] = 1
                count = 0

