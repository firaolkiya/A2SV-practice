# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            node=TreeNode(val)
            root=node
            return root

        def insert(root,val):
            if root.val>val:
                if root.left is None:
                    node=TreeNode(val)
                    root.left=node
                else:
                    insert(root.left,val)
            else:
                if root.right is None:
                    node=TreeNode(val)
                    root.right=node
                else:
                    insert(root.right,val)
        insert(root,val)
        return root