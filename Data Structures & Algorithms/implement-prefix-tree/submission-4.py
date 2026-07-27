class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False 

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
 
    def insert(self, word: str) -> None:
        curr = self.root
        for l in word:
            index = ord(l) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.end = True 

    def search(self, word: str) -> bool:
        curr = self.root
        for l in word:
            index = ord(l) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root 
        for l in prefix:
            index = ord(l) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return True

        
        