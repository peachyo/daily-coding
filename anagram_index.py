from collections import defaultdict


def del_if_zero(dict, char):
    if dict[char] == 0:
        del dict[char]
    print(dict)


def anagram_idicies(word, s):
    result = []
    freq = defaultdict(int)
    for char in word:
        freq[char] += 1

    for char in s[:len(word)]:
        freq[char] -= 1
        del_if_zero(freq, char)

    if not freq:
        result.append(0)

    for i in range(len(word), len(s)):
        start_char, end_char = s[i - len(word)], s[i]
        freq[start_char] += 1
        del_if_zero(freq, start_char)

        freq[end_char] -= 1
        del_if_zero(freq, end_char)

        if not freq:
            beginning_index = i - len(word) + 1
            result.append(beginning_index)

    return result


if __name__ == '__main__':
    print(anagram_idicies('ab', 'abxaba'))
