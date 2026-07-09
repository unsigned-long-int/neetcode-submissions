# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1 -> 2 moves
# 2 -> 4 moves
# 3 -> 8 moves
# 4 -> 16 moves
# 5 -> 32 moves
# 6 -> 64 moves
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        deq = deque([root])
        res = []
        while deq:
            sublist = []
            for _ in range(len(deq)):
                node = deq.popleft()
                sublist.append(node.val)
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
            res.append(sublist)
        return res
        