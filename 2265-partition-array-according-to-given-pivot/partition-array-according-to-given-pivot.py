class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than = []
        equal_to = []
        greather_than = []
        result = []
        for i in nums:
            if i < pivot:
                less_than.append(i)
            elif i > pivot:
                greather_than.append(i)
            else:
                equal_to.append(i)
        for i in less_than:
            result.append(i)
        for i in equal_to:
            result.append(i)
        for i in greather_than:
            result.append(i)
        return result
        