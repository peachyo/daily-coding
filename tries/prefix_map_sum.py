# insertion O(n)
# sum O(n*k)
from collections import defaultdict


class PrefixMapSum:
    def __init__(self):
        self.map = {}

    def insert(self, key: str, value: int):
        self.map[key] = value

    def sum(self, prefix):
        return sum(value for key, value in self.map.item()
                   if key.startsWith(prefix))


# solution 2
# insertion O(k^2)
# sum O(1)
class PrefixMapSum2:
    def __init__(self):
        self.map = defaultdict(int)
        self.words = set()

    def insert(self, key: str, value: str):
        if key in self.words:
            value -= self.map[key]
        self.words.add(key)

        for i in range(1, len(key) + 1):
            self.map[key[:i]] += value

    def sum(self, prefix):
        return self.map[prefix]


# solution 3 using trie
# insertion O(k)
# sum O(k)
class TrieNode:
    def __init__(self):
        self.letters = {}
        self.total = 0


class PrefixMapSum3:
    def __init__(self):
        self._trie = TrieNode()
        self.map = {}

    def insert(self, key: str, value: int):
        value -= self.map.get(key, 0)
        self.map[key] = value

        trie = self._trie
        for char in key:
            if char not in trie.letters:
                trie.letters[char] = TrieNode()
            trie = trie.letters[char]
            trie.total += value

    def sum(self, prefix):
        d = self._trie
        for char in prefix:
            if char in d.letters:
                d = d.letters[char]
            else:
                return 0
        return d.total
