class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        hash_map = {}
        j = 0
        result = 0

        for i in range(len(fruits)):
            if fruits[i] in hash_map:
                hash_map[fruits[i]] += 1
            else:
                hash_map[fruits[i]] = 1

            while len(hash_map) > 2:
                hash_map[fruits[j]] -= 1

                if hash_map[fruits[j]] == 0:
                    hash_map.pop(fruits[j])

                j += 1

            result = max(result, i - j + 1)

        return result



        