"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        map_ = {}
        def dfs(curr):
            if curr in map_:
                return map_[curr]

            map_[curr] = Node(curr.val)

            for n in curr.neighbors:
                map_[curr].neighbors.append(dfs(n))
            return map_[curr]
        return dfs(node) if node else None
        
        

