# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        answ=0
        tag=False
        def searchYou(node,indx):
            nonlocal answ,tag
            if not node:
                return indx
            left=searchYou(node.left,indx)+1
            if left==k and not tag:
                answ=node.val
                tag=True
                return left+2 
            right=searchYou(node.right,left)
            return right
        searchYou(root,0)
        return answ