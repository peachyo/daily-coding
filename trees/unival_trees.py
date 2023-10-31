class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def is_unival(root):
    return unival_helper(root, root.value)


def unival_helper(root, value):
    if root is None:
        return True

    if root.value == value:
        return unival_helper(root.left, value) and \
            unival_helper(root.right, value)

    return False


# O(n*n)
def count_unival_subtrees(root):
    if root is None:
        return 0

    left = count_unival_subtrees(root.left)
    right = count_unival_subtrees(root.right)
    return 1 + left + right if is_unival(root) else left + right


# O(n)
def count2(root):
    count, _ = helper2(root)


def helper2(root):
    if root is None:
        return 0, True

    left_count, is_left_unival = helper2(root.left)
    right_count, is_right_unival = helper2(root.right)
    total_count = left_count + right_count

    if is_left_unival and is_right_unival:
        if root.left is not None and root.value != root.left.value:
            return total_count, False
        if root.right is not None and root.value != root.right.value:
            return total_count, False
        return total_count + 1, True

    return total_count, False
