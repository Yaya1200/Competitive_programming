class Solution:
    def partition(self, s: str) -> list[list[str]]:

            result = []
            path = []

            def backtrack(start):
                if start == len(s):
                    result.append(path.copy())
                    return

                for end in range(start, len(s)):
                    part = s[start:end + 1]

                    if is_palindrome(part):
                        path.append(part)
                        backtrack(end + 1)
                        path.pop()

            def is_palindrome(part):
                return part == part[::-1]

            backtrack(0)
            return result