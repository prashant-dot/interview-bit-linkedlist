# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def rotateRight(self, A, B):
        c=0
        temp=A
        while temp:
            c+=1
            temp=temp.next
        if B>c:
            t=B//c
            B=B-t*c
        if c==1 or B==0:
            return A
        d=c-B
        c=0
        temp=A
        while(c<d-1):
            c+=1
            temp=temp.next
        p=temp.next
        q=p
        temp.next=None
        while(p):
            if p.next:
                p=p.next
            else:
                break
        p.next=A
        return q
==>O(n) where n is no. of nodes


        

