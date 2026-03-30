class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2 = sorted(arr2)
        value = 0
        for i in arr1:
            j = 0
            k = len(arr2)-1
            count = 0
            while(j <= k):
                if abs(i - arr2[j]) <= d and j != k: 
                    count += 1
                    break
                if abs(i - arr2[k]) <= d:
                    count += 1
                    break
                j+=1
                k-=1
            if count > 0:
                value += 1
        return len(arr1) - value

        