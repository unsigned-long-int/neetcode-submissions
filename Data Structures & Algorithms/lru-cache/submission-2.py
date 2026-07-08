class Node:
    def __init__(self, val=0, key=0,  prev=None, next=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.hash_map = {}
        self.right, self.left = Node(), Node()
        self.left.next = self.right
        self.right.prev = self.left


    def _remove(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert(self, node):
        prev_r_node, next_r_node = self.right.prev, self.right

        prev_r_node.next = node
        next_r_node.prev = node

        node.next = next_r_node
        node.prev = prev_r_node



    def get(self, key):
        if key not in self.hash_map:
            return -1

        self._remove(self.hash_map[key])
        self._insert(self.hash_map[key])
        return self.hash_map[key].val

    def put(self, key: int, value: int):
        if key in self.hash_map:
            self._remove(self.hash_map[key])
        node = Node(value, key)
        self.hash_map.update({key: node})
        self._insert(node)

        if len(self.hash_map) > self.cap:
            lru = self.left.next
            self._remove(lru)
            del self.hash_map[lru.key]
        




        