class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        value = [x for row in matrix for x in row]
        value = sorted(value)
        i = 0
        j = len(value)-1
        while(i<= j):
            mid = i +(j-i)//2
            if value[mid] == target:
                return True
            elif value[mid] > target:
                j = mid -1
            else:
                i = mid+1
        return False