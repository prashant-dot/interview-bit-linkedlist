head = ListNode(-float('inf'))
        head.next = A
        
        prev = A
        node = A
        
        while node is not None:
            if prev.val <= node.val:  # sort not needed
                prev = node
                node = node.next
            else:  # sort needed
                before = head
                after = head.next
                prev.next = node.next
                
                while after is not None and node.val > after.val:
                    before = after
                    after = before.next
                    
                before.next = node
                node.next = after
                node = prev.next
   
        return head.next


==>O(n^2)
