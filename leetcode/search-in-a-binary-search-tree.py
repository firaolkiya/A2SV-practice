# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        outputNode=None
        finder=root
        while finder:
            if finder.val<val:
                finder=finder.right
            elif finder.val>val:
                finder=finder.left
            else:
                outputNode=finder
                break
        return outputNode