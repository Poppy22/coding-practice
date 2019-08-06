# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        p1 = l1
        p2 = l2
        l3 = None
        head = None
        
        while p1 != None and p2 != None:
            if p1.val < p2.val:
                n = ListNode(p1.val)
                p1 = p1.next
            else:
                n = ListNode(p2.val)
                p2 = p2.next
                
            if head == None:
                l3 = n
                head = n
            else:
                l3.next = n
                l3 = n
                
        while p1 != None:
            n = ListNode(p1.val)
            p1 = p1.next
                
            if head == None:
                l3 = n
                head = n
            else:
                l3.next = n
                l3 = n
                
        while p2 != None:
            n = ListNode(p2.val)
            p2 = p2.next
                
            if head == None:
                l3 = n
                head = n
            else:
                l3.next = n
                l3 = n
                
        return head
                
        