class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWords = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWords = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endOfWords

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


if __name__ == '__main__':
    obj = Trie()
    obj.insert('yash')
    param_2 = obj.search('yash')
    param_3 = obj.startsWith('yah')
    print(param_2)
    print(param_3)
