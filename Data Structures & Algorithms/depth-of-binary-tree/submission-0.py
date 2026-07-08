# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def depth(root: TreeNode) -> int:
    if not root:
        return 0
    lDepth = depth(root.left)
    rDepth = depth(root.right)

    return max(lDepth, rDepth) + 1

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return depth(root)

    

