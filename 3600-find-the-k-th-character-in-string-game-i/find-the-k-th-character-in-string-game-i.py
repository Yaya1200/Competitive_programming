class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'
        while(len(word) < k):
            word += self.recurisve(word)
        return word[k-1]
    def recurisve(self, word):
            value = ""
            for i in range(len(word)):
                next_char = chr((ord(word[i]) - ord('a') + 1) % 26 + ord('a'))
                value += next_char
            return value
            
                        

                