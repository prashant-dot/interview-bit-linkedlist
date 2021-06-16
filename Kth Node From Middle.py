# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        temp,n=A,0
        while(temp):
            n+=1
            temp=temp.next
        mid=n//2+1
        temp=A
        if B>=mid:
            return -1
        n=mid-B-1
        for i in range(n):
            temp=temp.next
        return temp.val
==>O(n) where n is lenth of linkedlist
