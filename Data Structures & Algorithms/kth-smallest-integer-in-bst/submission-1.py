# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#               12
#          9.5          14
#       7       10    11.5  15
#    3     9   8   11


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        res = root.val
        def dfs(node):
            nonlocal cnt, res
            if not node:
                return 
            dfs(node.left)
            cnt -= 1
            if cnt == 0:
                res = node.val
                return
            dfs(node.right)
        dfs(root)
        return res


        