# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        head = None
        def worker(start,end):
            if end<=start:
                return None
            midIndex = (start+end)//2
            tree=TreeNode(nums[midIndex])
            tree.left =worker(start,midIndex)
            tree.right =worker(midIndex+1,end)
            return tree
        return worker(0,len(nums))
