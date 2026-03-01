class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != n*m:
            return []
        output = [] 
        k = 0
        for i in range(m):
            value = []
            for j in range(n):
                value.append(original[k])
                k+=1
            output.append(value)
        return output