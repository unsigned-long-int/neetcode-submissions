class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = Trie()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for l in range(len(word)):
            i = ord(word[l]) - ord('a')
            if curr.children[i] is None:
                curr.children[i] = Trie()
            curr = curr.children[i]
        curr.end = True


    def search(self, word: str) -> bool:
        curr = self.root
        for l in range(len(word)):
            i = ord(word[l]) - ord('a')
            if curr is None:
                return False
            curr = curr.children[i]
        return curr.end if curr is not None else False
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root 
        for l in range(len(prefix)):
            i = ord(prefix[l]) - ord('a')
            if curr is None:
                return False
            curr = curr.children[i]
        return curr is not None

        
        