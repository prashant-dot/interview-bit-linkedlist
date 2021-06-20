# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def removeNthFromEnd(self, A, B):
        temp=A
        c=0
        while(temp):
            c+=1
            temp=temp.next
        if B>c or B==c:
            A=A.next
            return A
        d=c-B
        temp=A
        i=1
        while(i<=d-1):
            i+=1
            temp=temp.next
        temp.next=temp.next.next
        return A
==>O(n)
