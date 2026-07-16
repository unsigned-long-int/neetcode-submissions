class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.word_end = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for l in word:
            i = ord(l) - ord('a')
            if curr.children[i] == None:
                curr.children[i] = Trie()
            curr = curr.children[i]

        curr.word_end = True
        

    def search(self, word: str) -> bool:
        def dfs(start_i, curr):
            if not curr:
                return False

            for li in range(start_i, len(word)):
                if word[li] == ".":
                    print('encountered .')
                    print(f'exploring children: {curr.children}')
                    #print(f'child has word_end: {curr.children[6].word_end}')
                    return any(dfs(li + 1, child) for child in curr.children if child)
                else:
                    index = ord(word[li]) - ord('a')
                    print(f'looking for {word[li]}')
                    if not curr or not curr.children[index]:
                        return False
                    print(f'proceeded for {word[li]}')
                    curr = curr.children[index]

            return curr.word_end

        return dfs(0, self.root)