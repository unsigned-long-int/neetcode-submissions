"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = head 
        if not dummy:
            return None

        hash_map = {}
        dummy = head 
        while dummy:
            newNode = Node(dummy.val)
            hash_map.update({dummy: newNode})
            dummy = dummy.next

        dummy = head
        while dummy:
            copy = hash_map[dummy]
            copy.next = hash_map[dummy.next] if dummy.next else None
            copy.random = hash_map[dummy.random] if dummy.random else None
            dummy = dummy.next
        return hash_map[head]

