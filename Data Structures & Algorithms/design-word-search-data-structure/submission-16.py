class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        curr = self.root 
        for l in word:
            index = ord(l) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = Trie()
            curr = curr.children[index]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(curr, start_index):
            if start_index == len(word):
                return curr.end_of_word

            if curr is None:
                return False 
            
            for i in range(start_index, len(word)):
                if word[i] == ".":
                    return any(dfs(child, i + 1) for child in curr.children if child)
                else:
                    index = ord(word[i]) - ord('a')
                    if curr is None or curr.children[index] is None:
                        return False
                    
                    curr = curr.children[index]

            return curr.end_of_word

        return dfs(self.root, 0)
                

