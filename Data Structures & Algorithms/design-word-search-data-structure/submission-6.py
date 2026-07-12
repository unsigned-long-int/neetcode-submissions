class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for l in word:
            nr = ord(l) - ord('a')
            if not curr.children[nr]:
                curr.children[nr] = TrieNode()

            curr = curr.children[nr]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(start_index, node):
            curr = node
            for i in range(start_index, len(word)):
                if word[i] == ".":
                    return any(dfs(start_index=i+1, node=child) for child in curr.children if child)
            
                nr = ord(word[i]) - ord('a')
                if not curr.children[nr]:
                    return False
                curr = curr.children[nr]
            return curr.endOfWord
        return dfs(0, self.root)
