class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# convert sorted array to height balanced bst
def make_bst(array):
    if not array:
        return None

    mid = len(array) // 2  # floor

    root = Node(array[mid])
    root.left = make_bst(array[:mid])
    root.right = make_bst(array[mid + 1:])

    return root
