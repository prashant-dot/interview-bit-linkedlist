# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        i=A
        j=i.next
        if A.next==None:
            return A
        while(j.next):
            if i.val==j.val and j.val==1:
                j=j.next
            elif i.val==j.val and j.val==0:
                i=i.next
                j=j.next
            elif i.val>j.val:
                i.val,j.val=j.val,i.val
                i=i.next
                j=j.next
            else:
                i=i.next
                j=j.next
        if j.val<i.val:
            i.val,j.val=j.val,i.val
            return A
        return A 
            
==>O(n)
where n is no. of nodes
_________________________________________

def solve(self, A):   #Traverse the list and count the number of 0s, 1s. Let the counts be n1, n2 respectively.
                      #Traverse the list again, fill the first n1 nodes with 0, then n2 nodes with 1.
        h=A
        a=0
        b=0
        while h:
            if h.val==0:
                a+=1
            else:
                b+=1
            h=h.next     
        h=A
        c=0
        while h:
            if c<a:
                c+=1
                h.val=0
            else:
                h.val=1
            h=h.next
        return A

==>O(n)
