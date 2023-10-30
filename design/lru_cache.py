class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.count = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.dummy_head = Node(None, None)
        self.tail = self.dummy_head
        self.size = 0

    def __len__(self):
        return self.size

    def insert(self, node):
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.size += 1

    def remove(self, node=None):
        if self.size == 0:
            return None

        if not node:
            node = self.dummy_head.next

        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        if node == self.tail:
            self.tail = self.tail.prev

        self.size -= 1
        return node


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.node_map = {}
        self.node_list = DoublyLinkedList()

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.head
        self.tail.prev = self.head

    def get(self, key):
        if key in self.node_map:
            node = self.node_map[key]
            self.node_list.remove(node)
            self.node_list.insert(node)
            return node
        return None

    def put(self, key, value):
        if key in self.node_map:
            node = self.node_map[key]
            self.node_list.remove(node)
            self.node_list.insert(node)
        else:
            node = Node(key, value)
            self.node_list.insert(node)
            self.node_map[key] = node

        if len(self.node_map) > self.capacity:
            node = self.node_list.dummy_head.next
            self.node_list.remove(node)
            del self.node_map[node.key]


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put("a", 5)
    print(cache.get("a"))

    cache.put("b", 3)
    cache.put("c", 4)
    print(cache.get("a"))
