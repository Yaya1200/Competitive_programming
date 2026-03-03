class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        while(n != 1): 
            if (n / 2) - (n//2) != 0 and (n / 3) - (n//3) != 0 and (n / 5) - (n//5) != 0:
                return False
            
            if (n / 2) - (n//2) == 0:
                n = n/2
            if (n / 3) - (n//3) == 0:
                n = n/3
            if (n / 5) - (n//5) == 0:
                n = n/5
        return True
            
        