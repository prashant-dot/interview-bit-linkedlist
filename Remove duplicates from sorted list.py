# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def deleteDuplicates(self, A):
        temp=A
        while(temp):
            if temp.next!=None:
                if temp.val==temp.next.val:
                    c=temp.next
                    temp.next=c.next
                else:
                    temp=temp.next
            else:
                temp=temp.next
        return A
  ==>O(n)
