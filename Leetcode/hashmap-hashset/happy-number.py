class Solution:
    def isHappy(self, n: int) -> bool:
        computed = {n: True}
        
        while True:
            x = 0
            while n > 0:
                x += (n % 10) ** 2
                n = n // 10
             
            if x == 1:
                return True
            
            if x in computed.keys():
                return False
            computed[x] = True
            n = x
