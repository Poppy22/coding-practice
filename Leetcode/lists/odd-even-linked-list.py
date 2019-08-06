# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None or head.next.next == None:
            return head
        
        # there are are at least 3 elements in the list
        odd = head
        p = head.next
        even = head.next
        
        # there can be n odd and n even or (n + 1) odd and n even
        while even != None:
            if odd.next != None:
                odd.next = odd.next.next
                o = odd
                odd = odd.next
                    
            if even.next != None:
                even.next = even.next.next
                e = even
                even = even.next
            else:
                even = None
            
        if odd != None:
            o.next = odd
            o = odd
            
        o.next = p
        return head

# Time: O(n)
# Space: O(1)