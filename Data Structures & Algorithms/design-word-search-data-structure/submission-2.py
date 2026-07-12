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

        def dfs(j, node):
            curr = node
            for i in range(j, len(word)):
                nr = ord(word[i]) - ord('a')
                if word[i] == ".":
                    for child in curr.children:
                        return any(dfs(i + 1, child) for child in curr.children if child)

                nr = ord(word[i]) - ord('a')
                if not curr.children[nr]:
                    return False
                curr = curr.children[nr]
            return curr.endOfWord

        return dfs(0, self.root)
        
