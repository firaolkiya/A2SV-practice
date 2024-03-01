# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total_sum = 0
        
        def worker(node,other):
            nonlocal total_sum
            if not node.left and not node.right:
                other.append(str(node.val))
                s="".join(other)
                total_sum+=int(s)
                return
            other.append(str(node.val))
            temp=[i for i in other]
            if node.left:
                worker(node.left,other)
            if node.right:
                worker(node.right,temp)
            return
        worker(root,[])
        return total_sum
        