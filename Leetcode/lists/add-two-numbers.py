# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        p1 = l1
        p2 = l2
        result = ListNode(-1) # dummy cell
        prev_node = result
        
        while p1 != None and p2 != None:
            
            x = p1.val + p2.val + carry
            if x > 9:
                carry = 1
                x = x % 10
            else:
                carry = 0
                    
            new_node = ListNode(x)
            prev_node.next = new_node
            prev_node = new_node
                
            p1 = p1.next
            p2 = p2.next
         
        while p1 != None:
            # there are digits left in the first number
            x = p1.val + carry
            if x > 9:
                carry = 1
                x = x % 10
            else:
                carry = 0
                
            new_node = ListNode(x)
            prev_node.next = new_node
            prev_node = new_node
            p1 = p1.next
            
        while p2 != None:
            # there are digits left in the second number
            x = p2.val + carry
            if x > 9:
                carry = 1
                x = x % 10
            else:
                carry = 0
                
            new_node = ListNode(x)
            prev_node.next = new_node
            prev_node = new_node
            p2 = p2.next
         
        if carry:
            new_node = ListNode(1)
            prev_node.next = new_node
            
        p = result
        result = result.next
        del p # eliminate dummy
            
        return result
        