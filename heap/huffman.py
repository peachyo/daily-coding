import heapq


def build_tree(frequencies):
    nodes = []
    for char, frequency in frequencies.items():
        heapq.heappush(nodes, (frequency, Node(char)))

    while len(nodes) > 1:
        f1, n1 = heapq.heappop(nodes)
        f2, n2 = heapq.heappop(nodes)
        node = Node('*', left=n1, right=n2)
        heapq.heappop(nodes, (f1 + f2, node))

    root = nodes[0][1]

    return root



# O(mlogn)
def encode(root, string='', mapping={}):
    if not root:
        return

    if not root.left and not root.right:
        mapping[root.char] = string

    encode(root.left, string + '0', mapping)
    encode(root.right, string + '1', mapping)

    return mapping
