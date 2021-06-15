# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        if A==None:
            return A
        aa=[]
        while(A):
            aa.append(A.val)
            A=A.next
        i=0
        bb=[]
        bc=[]
        while(i<len(aa)):
            if aa[i]<B:
                bb.append(aa[i])
            else:
                bc.append(aa[i])
            i+=1
        cc=[]
        for each in bb:
            cc.append(each)
        for each in bc:
            cc.append(each)
        head=ListNode(cc[0])
        cur=head
        for i in range(1,len(cc)):
            cur.next=ListNode(cc[i])
            cur=cur.next
        return head
            
==TC=O(n) and SC=O(n)
