class Solution:
    def isHappy(self, n: int) -> bool:
       i = n
       value = 0
       while(i != 1):
            while(i > 0):
                k  = i % 10
                value += k*k
                i = i//10
            i = value
            if value == 4:
                return False
            value = 0
       return True