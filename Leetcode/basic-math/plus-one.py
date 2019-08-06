class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        n = len(digits)
        
        if n == 1:
            if digits[0] < 9:
                return [digits[0] + 1]
            else:
                return [1, 0]
        
        for i in range(n - 1, -1, -1):
            if carry:
                x = digits[i] + 1
            
                if x == 10:
                    x = 0
                    carry = True
                else:
                    carry = False
                
                digits[i] = x
                
        if carry:
            return [1] + digits
                
        return digits

# Time: O(n)
# Space: O(1)