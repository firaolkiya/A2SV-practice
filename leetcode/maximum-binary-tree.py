# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def built(start,end):
            if start>=end:
                return None
            mid = nums.index(max(nums[start:end]))
            root = TreeNode(nums[mid])
            root.left=built(start,mid)
            root.right=built(mid+1,end)
            return root
        return built(0,len(nums))