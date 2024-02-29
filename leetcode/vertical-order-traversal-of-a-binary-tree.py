# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
    ##declare dictionary to store node.val with their correct row and column
        store = defaultdict(list)
    ##declare the function to collect the value from tree
        def extract(node,row,column):
            if not node:   ## if the node has'nt any value stop recursion
                return None
            extract(node.left,row+1,column-1)   ##move left part
            store[column].append([row,node.val])  ## collect from current node
            extract(node.right,row+1,column+1)  ## move to right part
            
        extract(root,0,0)  ## coll function by starting ro=0, col = 0
        store = dict(sorted(store.items()))   ## sort dictionary based on key
        ## declare list that will contain answer
        answer=[]
        ## iterate over the store.values
        for num in store.values():
            temp = [x for y,x in sorted(num)]  ## sort the inner list and get
            answer.append(temp)

        return answer