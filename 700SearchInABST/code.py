# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def traverse(root):
            if not root:
                return
            if root.val==val:
                result.append(root)
            elif root.val<val:
                traverse(root.right)
            else:
                traverse(root.left)
        
        result=[]
        traverse(root)
        if len(result)==0:
            return
        else:
            return result[0]
        
