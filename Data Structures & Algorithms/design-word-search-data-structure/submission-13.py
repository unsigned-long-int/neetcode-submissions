class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        curr = self.root
        for l in range(len(word)):
            i = ord(word[l]) - ord('a')
            if curr.children[i] is None:
                curr.children[i] = Trie()

            curr = curr.children[i]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(curr, start_index):
            if not curr:
                return False

            for i in range(start_index, len(word)):
                if word[i] == '.':
                    return any(dfs(child, i + 1) for child in curr.children if child)
                else:
                    ind = ord(word[i]) - ord('a')
                    if not curr or not curr.children[ind]:
                        return False
                    curr = curr.children[ind]
            return curr.end_of_word

        return dfs(self.root, 0)

