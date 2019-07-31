# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# ITERATIVE SOLUTION

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        
        r, q = head, head
        p = head.next
        while p.next != None:
            q = p
            p = p.next
            q.next = r
            r = q
            
        p.next = q
        head.next = None
        return p
            
        
# Time: O(n)
# Space: O(1)

# _________________________________________
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# RECURSIVE SOLUTION - todo

