class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
       less_than_pivot = []
       greather_than_pivot = []
       for i in nums:
        if i < pivot:
            less_than_pivot.append(i)
        elif i > pivot:
            greather_than_pivot.append(i)
       value = nums.count(pivot)
       for i in range(value):
        less_than_pivot.append(pivot)
       less_than_pivot.extend(greather_than_pivot)
       return less_than_pivot