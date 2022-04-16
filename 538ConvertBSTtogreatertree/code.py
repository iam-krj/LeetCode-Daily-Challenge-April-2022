# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.greater = 0
        def solve(root):
            if not root: return
            solve(root.right)
            self.greater += root.val
            root.val = self.greater
            solve(root.left)
        solve(root)
        return root
