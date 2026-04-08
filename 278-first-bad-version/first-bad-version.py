# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int: 
        i = 1
        j = n
        while(i <= j):
            mid = i + (j-i)//2
            value = isBadVersion(mid)
            if value == True:
                j = mid-1
            else:
                i = mid+1
        if isBadVersion(mid):
            return mid
        else:
            return mid+1


        