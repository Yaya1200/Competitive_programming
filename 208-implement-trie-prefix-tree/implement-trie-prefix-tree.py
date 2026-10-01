class Trie:

    def __init__(self):
        self.value = []
        

    def insert(self, word: str) -> None:
        self.value.append(word)
        

    def search(self, word: str) -> bool:
        if word in self.value:
             return True 
        else:
             return False
        

    def startsWith(self, prefix: str) -> bool:
        for i in self.value:
            if prefix == i[:len(prefix)]:
                 return True 
            else:
                 False
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)