# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter=defaultdict(int)
        def extract(node):
            if not node:
                return None
            counter[node.val]+=1
            extract(node.left)
            extract(node.right)
        extract(root)
        counter = dict(sorted(counter.items(), key=lambda item:item[1],reverse= True))
        answer = []
        for key in counter:
            if not answer or counter[answer[0]]==counter[key]:
                answer.append(key)
            else:
                break
        return answer