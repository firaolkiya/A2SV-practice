# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def search(node):
            nonlocal ans
            if not node:
                return [-1,-1]
            left=search(node.left)
            right=search(node.right)
            if right==[-1,-1]:
                right= [node.val,node.val]
            if left==[-1,-1]:
                left= [node.val,node.val]
            ans = max(ans,abs(node.val-right[0]),abs(node.val-right[1]))
            ans = max(ans,abs(node.val-left[0]),abs(node.val-left[1]))
            res = [min(node.val,right[0],left[0]),max(node.val,right[1],left[1])]
            return res
        search(root)
        return ans
