# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        elif root1 and not root2:
            return root1
        elif root2 and not root1:
            return root2
        
        newNode=  TreeNode(root1.val+root2.val)
        newNode.left=self.mergeTrees(root1.left,root2.left)
        newNode.right=self.mergeTrees(root1.right,root2.right)
        return newNode

         
        