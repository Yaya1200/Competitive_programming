class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr)-1
        while left <= right:
            mid = left+(right-left)//2
            if mid-1 >=0 and  arr[mid] > arr[mid-1] and mid+1 < len(arr) and  arr[mid] > arr[mid+1]:
                return mid
            elif mid-1 >= 0 and arr[mid] < arr[mid-1]:
                right = mid -1
            else:
                left = mid +1
       
        