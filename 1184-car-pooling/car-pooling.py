class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        output = [[0,0]]
        for i in trips:
            output.append([i[1], i[0]])
            output.append([i[2], -(i[0])])
        output.sort()
        for i in range(1,len(output)): 
            output[i][1] += output[i-1][1]
            if output[i][1] > capacity:
                return False
            
        return True
        