class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        min_value = -1
        max_value = -1
        while(left <= right):
            mid = (left+right)//2
            if nums[mid] == target:
                min_value = mid
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        left = 0
        right = len(nums)-1
        while(left <= right):
            mid = (left+right)//2
            if nums[mid] == target:
                max_value = mid
                left = mid+1
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return [min_value, max_value]

        