class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

        node.is_end = True


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        trie = Trie()

        for word in strs:
            trie.insert(word)

        node = trie.root
        answer = ""

        while len(node.children) == 1 and not node.is_end:

            ch = next(iter(node.children))

            answer += ch

            node = node.children[ch]

        return answer
        