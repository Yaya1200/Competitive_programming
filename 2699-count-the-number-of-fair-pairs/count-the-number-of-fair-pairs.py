class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0

        for i in range(len(nums)):
            low = lower - nums[i]
            high = upper - nums[i]

            j = i + 1
            k = len(nums) - 1

            while j <= k:
                mid = j + (k - j) // 2

                if nums[mid] >= low:
                    k = mid - 1
                else:
                    j = mid + 1

            left = j

            j = i + 1
            k = len(nums) - 1

            while j <= k:
                mid = j + (k - j) // 2

                if nums[mid] > high:
                    k = mid - 1
                else:
                    j = mid + 1

            right = j

            count += right - left

        return count

