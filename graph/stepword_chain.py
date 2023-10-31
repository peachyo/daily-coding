from collections import deque
from string import ascii_lowercase


# Given a start word, an end word, and a dictionary of valid words, find the shortest
# transformation sequence from start to end such that only one letter is changed at
# each step of the sequence.
# model this as graph, nodes will be the words in dictionary.
# form an edge between two nodes if and only if one char can be modified in one word to get
# to the other. do breadth-first search from start and finishing once
# O(n^2) time O(n) space
def word_ladder(start, end, words):
    queue = deque([(start, [start])])

    while queue:
        word, path = queue.popleft()
        if word == end:
            return path

        for i in range(len(word)):
            for char in ascii_lowercase:
                next_word = word[:i] + char + word[i+1:]
                if next_word in words:
                    words.remove(next_word)
                    queue.append((next_word, path + [next_word]))

        return None