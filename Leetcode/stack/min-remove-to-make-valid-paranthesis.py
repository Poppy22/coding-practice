class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        count, i = 0, 0
        while i < len(s):
            if s[i] == "(":
                count += 1
            elif s[i] == ")":
                count -= 1
                if count < 0: 
                    s.pop(i)
                    count = 0
                    i -= 1
            i += 1
        i = len(s)-1
        
        while count > 0 and i >=0 :
            if s[i] == "(":
                s.pop(i)
                count -= 1
            i-=1
        return "".join(s) 
            