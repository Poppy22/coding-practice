class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        # get wrong closed paranthesis
        stack = []
        closed_without_open = 0
        
        for s in S:
            if s == '(':
                stack.append(s)
            
            # count and remove ) from the beginning
            if len(stack) == 0 and s == ')':
                closed_without_open += 1
                
            if len(stack) > 0 and stack[-1] == '(' and s == ')':
                stack.pop()
                
        # stack has only open paranthesis
        open_without_closed = len(stack)
        
        return open_without_closed + closed_without_open
        