class TrieNode:

    def __init__(self):
        self.children = {}
        self.end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root

        for i in word:

            if i not in current.children:
                current.children[i] = TrieNode()

            current = current.children[i]

        current.end = True

    def search(self, word: str) -> bool:
        current = self.root

        for i in word:

            if i not in current.children:
                return False

            current = current.children[i]

        return current.end

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for i in prefix:

            if i not in current.children:
                return False

            current = current.children[i]

        return True