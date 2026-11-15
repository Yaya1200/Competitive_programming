class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        count = 0
        sumission = sum(arr[0:k])
        if sumission//k >= threshold:
            count += 1
        for i in range(k, len(arr)):
            sumission += arr[i]
            sumission -= arr[i-k]
            if sumission //k >= threshold:
                count+= 1
        return count


        