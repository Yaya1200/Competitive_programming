class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)
        min_index = -1
        max_index = -1
        left = 0
        right = len(nums)-1
        while(left <= right):
            mid = left+(right-left)//2
            if nums[mid] == target:
                right = mid-1
                min_index = mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        left = 0
        right = len(nums)-1
        while(left <= right):
            mid = left+(right-left)//2
            if nums[mid] == target:
                left = mid+1
                max_index = mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        if min_index == -1:
            return []
        output_array = list(range(min_index, max_index+1))
        return output_array

        