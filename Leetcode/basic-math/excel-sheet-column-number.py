class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        i = 0
        
        for c in s[::-1]:
            result += 26 ** i * (ord(c) - 64)
            i += 1
            
        return result

# Time: O(n)
# Space: O(1)