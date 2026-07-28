"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        node_map = {}
        def dfs(original):
            if not original:
                return None
            if original in node_map:
                return node_map[original]
            
            copy = Node(original.val)
            node_map[original] = copy
            for n in original.neighbors:
                copy.neighbors.append(dfs(n))
            return copy

        return dfs(node)


        

