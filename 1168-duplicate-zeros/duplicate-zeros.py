class Solution:
    def duplicateZeros(self, arr):
        value = arr.copy()

        i = 0
        j = 0

        while j < len(arr) and i < len(value):
            if value[i] == 0:
                arr[j] = 0
                if j + 1 < len(arr):
                    arr[j+1] = 0
                j += 2
            else:
                arr[j] = value[i]
                j += 1

            i += 1