# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None
def solve(A,k):
    if(A==None):
        return A
    new=ListNode(A.val)
    i=1
    tmp=new
    cur=A.next
    while(i<k):
        a=ListNode(cur.val)
        a.next=new
        new=a
        cur=cur.next
        i+=1
    tmp.next=solve(cur,k)
    return new
class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        ans=ListNode(-1)
        if(A==None or B==1):
            return A
        ans=solve(A,B)
        return ans
==>O(n) where n is no. of nodes in linked list
