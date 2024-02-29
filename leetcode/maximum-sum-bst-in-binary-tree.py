# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check_lr(self, node, left_max, right_min):
        if node.val >= right_min or left_max >= node.val:
            return False
        return True
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            if node is None:
                return [0, float("inf"), float("-inf")]
            ls, lmin, lmax = dfs(node.left)
            rs, rmin,rmax = dfs(node.right)

            if self.check_lr(node, lmax, rmin) and ls != "f" and rs != "f":
                ans = max(ans, ls+rs+node.val)
                _min = min(lmin, rmin, node.val)
                _max = max(lmax, rmax, node.val)
                return [ls+rs+node.val, _min, _max]
            return ["f", node.val, node.val]
        dfs(root)
        return ans