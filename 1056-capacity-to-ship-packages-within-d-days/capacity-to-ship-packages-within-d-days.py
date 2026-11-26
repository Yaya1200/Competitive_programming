
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        submission = sum(weights)
        left = max(weights)
        right = submission

        while left <= right:
            mid = left + (right - left) // 2
            count = 1
            total = 0
            for i in range(len(weights)):
                if total + weights[i] > mid:
                    count += 1
                    total = weights[i]
                else:
                    total += weights[i]

            if count > days:
                left = mid + 1
            else:
                right = mid - 1

        return left
