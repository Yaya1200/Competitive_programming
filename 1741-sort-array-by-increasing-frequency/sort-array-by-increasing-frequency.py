class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        numsCount = collections.Counter(nums)

        nums.sort(key= lambda n: (numsCount[n], -n))

        return nums





        