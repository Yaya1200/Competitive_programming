class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        output = []
        path = []
        used = [False]*len(digits)
        def backtrack():
            if len(path) == 3:
                if path[2] % 2 == 0:
                    values = str(path[0])+str(path[1])+str(path[2])
                    output.append(int(values))

                return 
            for i in range(len(digits)):
                if used[i] :
                    continue
                if len(path) == 0 and digits[i] == 0:
                    continue
                path.append(digits[i])
                used[i] = True
                backtrack()
                path.pop()
                used[i] = False
        backtrack()
        return sorted(set(output))
    