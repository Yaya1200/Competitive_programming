class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        output = set()
        path = []
        used = [False] * len(digits)

        def backtrack():
            if len(path) == 3:
                if path[2] % 2 == 0:
                    number = path[0] * 100 + path[1] * 10 + path[2]
                    output.add(number)
                return

            for i in range(len(digits)):
                if used[i]:
                    continue

                if len(path) == 0 and digits[i] == 0:
                    continue
                path.append(digits[i])
                used[i] = True

                backtrack()
                path.pop()
                used[i] = False

        backtrack()

        return len(output)