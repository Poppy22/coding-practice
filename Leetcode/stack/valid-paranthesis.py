class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        r = []
        for x in s:
            if len(r) == 0:
                r.append(x)
            elif (x == ')' and r[-1] == '(') or (x == ']' and r[-1] == '[') or (x == '}' and r[-1] == '{'):
                r.pop()
            else:
                r.append(x)
                
        if len(r) == 0:
            return True
        
        return False
                
            