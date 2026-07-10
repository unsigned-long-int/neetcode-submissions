# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        deq = deque([root])

        while deq:
            right_node = None
            for _ in range(len(deq)):
                node = deq.popleft()
                if node:
                    right_node = node
                    deq.append(node.left)
                    deq.append(node.right)

            if right_node:
                res.append(right_node.val)

        return res



