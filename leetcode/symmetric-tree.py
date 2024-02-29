# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isTheSame(right,left):
            if not right and not left:
                return True
            elif not right or not left:
                return False
            if right.val!=left.val:
                return False
            tree1=isTheSame(right.right,left.left)
            tree2=isTheSame(right.left,left.right)
            return tree1 and tree2
        return isTheSame(root.right,root.left)