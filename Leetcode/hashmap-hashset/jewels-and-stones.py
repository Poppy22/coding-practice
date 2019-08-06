class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        d = {}
        
        for j in J:
            d[j] = True
            
        nr = 0
        for s in S:
            if s in d:
                nr += 1
                
        return nr