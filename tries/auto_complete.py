WORDS = ['dog', 'deer', 'deal']


# O(n) n # of words in dict
def auto_complete(s):
    results = set()
    for word in WORDS:
        if word.startswith(s):
            results.add(word)
    return results


ENDS_HERE = '#'


class Trie:
    def __init__(self):
        self._trie = {}

    def insert(self, text):
        trie = self._trie
        for char in text:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie[ENDS_HERE] = True

    def find(self, prefix):
        trie = self._trie
        for c in prefix:
            if c in trie:
                trie = trie[c]
            else:
                return []
        return self._elements(trie)

    def _elements(self, d):
        result = []
        for c, v in d.items():
            if c == ENDS_HERE:
                subresult = ['']
            else:
                subresult = [c + s for s in self._elements(v)]
            result.extend(subresult)
        return result


words = []
trie = Trie()
for word in words:
    trie.insert(word)


def autocomplete(prefix):
    suffixes = trie.find(prefix)
    return [prefix + w for w in suffixes]
