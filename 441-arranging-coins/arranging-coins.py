class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        output = 0
        for i in range(n):
            output+= (i+1)
            if output <= n:
              count +=1
            else:
                break
        print(output)
        return count
