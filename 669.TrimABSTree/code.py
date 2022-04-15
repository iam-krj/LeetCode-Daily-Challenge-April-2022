# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:

		def TrimBST(node):

			if node == None:
				return None

			elif node.val > high : 
				return TrimBST(node.left)

			elif node.val < low : 
				return TrimBST(node.right)

			else:
				node.left = TrimBST(node.left)
				node.right = TrimBST(node.right)

				return node

		return TrimBST(root)
