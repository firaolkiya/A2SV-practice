# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        list_size=0
        cur=head
        while cur:
            cur=cur.next
            list_size+=1
        each_small_size=list_size//k
        remain=list_size%k
        print(each_small_size,list_size)
        current=head
        broked=[]
        counter=0
        temp_head=current
        while current:
            if counter<each_small_size:
                counter+=1
            if counter>=each_small_size:
                if remain>0 and counter!=0:
                    current=current.next
                    remain-=1
                temp_pointer=current
                if current:
                    current=current.next
                    temp_pointer.next=None
                broked.append(temp_head)
                temp_head=current
                counter=0
                continue
            current=current.next
        while len(broked)<k:
            broked.append(temp_head)
        return broked


        