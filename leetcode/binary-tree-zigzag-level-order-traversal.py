# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)

        def extract(node,row):
            if not node:
                return
            dic[row].append(node.val)
            extract(node.left,row+1)
            extract(node.right,row+1)
        extract(root,0)
        dic = dict(sorted(dic.items()))
        list1=[]
        k=0
        for i in dic.values():
            if k%2==0:
                list1.append(i)
            else:
                list1.append(i[::-1])
            k+=1
        print(list1)
        return list1
            