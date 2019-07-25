class Solution:
        
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        n = left
        result = []
        
        while n <= right:
            isSelfDividing = True
            x = n
            while x > 0:
            
                # check if it has digit 0
                if x % 10 == 0:
                    isSelfDividing = False
                    break
            
                # check if it is divisible by its last digit
                if n % (x % 10) != 0:
                    isSelfDividing = False
                    break
            
                x = x // 10
    
            if isSelfDividing:
                result.append(n)
            n += 1
                
        return result

# Time: O(right - left + 1)
# Space: O(right - left + 1)