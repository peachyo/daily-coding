def get_spaces(row, desc, k):
    max_spaces = (k - 1) * 2 - 1
    if desc:
        spaces = max_spaces - row * 2
    else:
        spaces = max_spaces - (k - 1 - row) * 2
    return spaces


def is_descending(index, k):
    return index % (2 * (k - 1)) < k - 1


def zigzag(sentence, k):
    n = len(sentence)

    for row in range(k):
        i = row
        line = [" " for _ in range(n)]

        while i < n:
            line[i] = sentence[i]
            desc = is_descending(i, k)
            spaces = get_spaces(row, desc, k)
            i += spaces + 1

        print("".join(line))


if __name__ == '__main__':
    print(zigzag("Thatallowshumantoreachouterspace", 5))
