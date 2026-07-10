# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidSubtree(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return (isValidSubtree(node.left, left, node.val) and isValidSubtree(node.right, node.val, right))
        return isValidSubtree(root, float('-inf'), float('inf'))

