# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        first_pointer=headA
        second_pointer=headB
        store={}
        while first_pointer:
            temp_node=ListNode(first_pointer.val)
            store[first_pointer]=temp_node
            first_pointer=first_pointer.next
        while second_pointer:
            if second_pointer in store:
                return second_pointer
            second_pointer=second_pointer.next
        return None


        