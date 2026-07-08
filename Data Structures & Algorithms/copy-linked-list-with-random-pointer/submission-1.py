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
        curr = head
        if not curr:
            return None 

        hashMap = {}
        while curr:
            copy = Node(curr.val)
            hashMap[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = hashMap[curr]
            copy.next = hashMap[curr.next] if curr.next else None
            copy.random = hashMap[curr.random] if curr.random else None
            curr = curr.next

        return hashMap[head]

