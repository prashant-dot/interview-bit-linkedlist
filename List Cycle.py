# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        
        slow=A
        fast=A
        while(fast):
            slow=slow.next
            fast=fast.next
            if (not fast):
                return None
            fast=fast.next
            if slow==fast:
                break
        if not fast: return None
        fast=A
        while(slow!=fast):
            slow=slow.next
            fast=fast.next
        return fast    

==>o(N)
