class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for l in word:
            nr = ord(l) - ord('a')
            if curr.children[nr] == None:
                curr.children[nr] = TrieNode()
            curr = curr.children[nr]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for l in word:
            nr = ord(l) - ord('a')
            print(l)
            if curr.children[nr] == None:
                return False

            curr = curr.children[nr]
        if curr.endOfWord is True:
            return True
        return False
            

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for l in prefix:
            nr = ord(l) - ord('a')
            if curr.children[nr] == None:
                return False
            curr = curr.children[nr]

        return True
        
        