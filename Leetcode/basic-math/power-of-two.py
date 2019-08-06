class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # only one bit active
        
        if n <= 0:
            return False
        
        active_bits = 0
        while n > 0:
            if n & 1 == 1:
                active_bits += 1
            n = n >> 1
            if active_bits == 2:
                return False
            
        return True
                

# Time: O(1)
# Space: O(1)