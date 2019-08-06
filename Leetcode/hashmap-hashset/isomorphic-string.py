class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        replacements = {}
        for i in range(len(s)):
            if s[i] not in replacements.keys():
                if t[i] not in replacements.values():
                    # no two different characters may map to the same character
                    replacements[s[i]] = t[i]
                else:
                    return False
            elif replacements[s[i]] != t[i]:
                # s[i] is an existing key, but now it should have been 
                # mapped to another character
                return False
            
        return True
        