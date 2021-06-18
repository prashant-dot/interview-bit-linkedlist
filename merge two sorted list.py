# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def mergeTwoLists(self, A, B):
        temp1=A
        temp2=B
        l1=[]
        l2=[]
        while(temp1):
            l1.append(temp1.val)
            temp1=temp1.next
        while(temp2):
            l2.append(temp2.val)
            temp2=temp2.next
        n=len(l1)
        m=len(l2)
        l1.append(float('inf'))
        l2.append(float('inf'))
        l3=[]
        i,j=0,0
        count=1
        while(count<=n+m):
            if l1[i]<l2[j]:
                l3.append(l1[i])
                i+=1
            else:
                l3.append(l2[j])
                j+=1
            count+=1
        new=ListNode(l3[0])
        temp3=new
        i=1
        while(i<len(l3)):
            temp3.next=ListNode(l3[i])
            temp3=temp3.next
            i+=1
        return new
 ==>TC=O(n) and SC=O(n) 
