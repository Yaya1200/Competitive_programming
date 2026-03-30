class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix)-1
        while(i <= j):
            mid = i + (j-i)//2
            if matrix[mid][0] <= target and matrix[mid][len(matrix[mid])-1] >= target:
                y = 0
                z = len(matrix[mid])-1
                while( y <= z):
                    mid_1 = y + (z-y)//2
                    if matrix[mid][mid_1] == target:
                        return True
                    elif matrix[mid][mid_1] > target:
                        z = mid_1-1
                    else:
                        y = mid_1+1
                return False
            elif matrix[mid][0] > target:
                j = mid-1
            else:
                i = mid+1
        return False
        