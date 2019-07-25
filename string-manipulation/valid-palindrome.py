class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        s = [x for x in s if x >= 'a' and x <= 'z']
        n = len(s)
        if n == 0:
            return True
        
        start = 0
        end = n - 1
        
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
            
        return True

# Time: O(n)
# Space: O(1)