class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        value = [x for row in matrix for x in row]
        value = sorted(value)
        return value[k-1]

        