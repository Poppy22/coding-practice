# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        
        fast, slow = head, head
        while fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
            
            if slow == None or fast == None:
                break
            
        return False
        