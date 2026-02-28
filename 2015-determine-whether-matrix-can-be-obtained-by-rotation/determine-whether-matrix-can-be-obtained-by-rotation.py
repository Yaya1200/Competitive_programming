class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        for k in range(3):
            mat = [list(rows) for rows in zip(*mat[::-1])]
            
            if mat == target:
                return True
        
        return False

        