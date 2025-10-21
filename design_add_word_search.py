class TrieNode():
    def __init__(self) -> None:
        self.maps = {}
        self.word = False

class WordDictionary():
    def __init__(self) -> None:
        self.root = TrieNode()
    def add(self, word):
        curr = self.root
        for char in word:
            if char not in curr.maps:
                curr.maps[char] = TrieNode()
            curr = curr.maps[char]
        curr.word = True
    def search(self,word):
        def dfs(j,root):
            curr = root
            for i in range(j, len(word)):
                c = word[i]
                if c ==".":
                    for letter in curr.maps.values():
                        if dfs(i+1, letter):
                            return True
                        return False
                else:
                    if c not in curr.maps:
                        return False
                    curr = curr.maps[c]
            return curr.word
        return dfs(0,self.root)