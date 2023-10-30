def get_spaces(row, desc, k):
    max_spaces = (k - 1) * 2 - 1
    if desc:
        spaces = max_spaces - row * 2
    else:
        spaces = max_spaces - (k - 1 - row) * 2
    return spaces


def is_descending(index, k):
    return index % 2 * (k - 1) < k - 1
