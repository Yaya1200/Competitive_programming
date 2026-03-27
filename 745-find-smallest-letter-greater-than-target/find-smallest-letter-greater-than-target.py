class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = 0
        j = len(letters)-1
        while(i < j):
            mid = (i +j)//2
            if letters[mid] > target:
                j = mid
            elif letters[mid] <= target:
                i = mid+1
        if letters[i] > target:
            return letters[i]
        else:
            return letters[0]
            
        