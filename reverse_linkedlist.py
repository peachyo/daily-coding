class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


def reverse(node):
    head, _ = _reverse(node)
    return head


def _reverse(node):
    if node is None:
        return None, None

    if node.next is None:
        return node, node

    head, tail = _reverse(node.next)
    node.next = None
    tail.next = node
    return head, node

def reverse2(head):
    prev, current = None, head
    while current is not None:
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp

