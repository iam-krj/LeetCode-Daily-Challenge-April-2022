# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack=[]
        def inorder(root):
            if root:
                inorder(root.left)
                stack.append(root.val)
                inorder(root.right)
        
        inorder(root)
        result=None
        for i in stack[::-1]:
            result=TreeNode(i,left=None,right=result)
        return result
