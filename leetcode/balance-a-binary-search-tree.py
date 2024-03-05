# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []
## fetch all number from linked list
        def extract(node):
            if not node:
                return
            nums.append(node.val)
            extract(node.left)
            extract(node.right)
        ##sort the list
        extract(root)
        nums.sort()
## re construct the binary tree
        def construct(start,end):
            if end<=start:
                return
            mid= (start+end)//2
            newNode = TreeNode(nums[mid])
            newNode.left =construct(start,mid)
            newNode.right =construct(mid+1,end)
            return newNode
        return construct(0,len(nums))
        
        
