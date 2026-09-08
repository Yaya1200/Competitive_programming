class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        current_max_i = values[0]
        current_max_value = 0
        for i in range(1, len(values)):
            current_max_value = max(current_max_value, current_max_i+values[i]-i)
            current_max_i = max(current_max_i, values[i]+i)
        return current_max_value

        