def is_palindrome(word):
    return word == word[::-1]


def palindrom_pairs(words):
    d = {}

    # map of word and index
    for i, word in enumerate(words):
        d[word] = i

    result = []

    # break up word into prefix suffix
    # cbaa = cbaa + "", "" is palindrome, look for aabc in d
    # cbaa = cba + "a", "a" is palindrome, look for abc in d
    # cbaa = cb + aa, aa is palindrome, look for bc in d
    # cbaa = c + aab, c is palindrome, look for aab in d
    for i, word in enumerate(words):
        for char_i in range(len(word)):
            prefix, suffix = word[:char_i], word[char_i:]
            reversed_prefix = prefix[::-1]
            reversed_suffix = suffix[::-1]

            if is_palindrome(suffix) and (reversed_prefix in d):
                if i != d[reversed_prefix]:
                    result.append((i, d[reversed_prefix]))

            if is_palindrome(prefix) and (reversed_suffix in d):
                if i != d[reversed_suffix]:
                    result.append((i, d[reversed_suffix]))

    return result

if __name__ == '__main__':
    print(palindrom_pairs(["code", "edoc", "da", "d"]))