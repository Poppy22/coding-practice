class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x ^= y
        
        # count the number of 1 bits in x
        result = 0
        
        while x > 0:
            if x & 1 == 1:
                result += 1
            x = x >> 1
            
        return result

# Time: O(1)
# Space: O(1)