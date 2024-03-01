# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        answer = True
        def checkNumber(node):
            nonlocal answer
            if not node:
                return [float('inf'),float('-inf')]
            left=checkNumber(node.left)
            right=checkNumber(node.right)
            if left[1]>=node.val or right[0]<=node.val:
                answer=False
            res = [min(left[0],right[0],node.val),max(left[1],right[1],node.val)]
            return res
        checkNumber(root)
        return answer