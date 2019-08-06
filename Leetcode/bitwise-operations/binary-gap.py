class Solution:
    def binaryGap(self, N: int) -> int:
        global_max = 0
        current_max = 0
        ones = 0
        
        while N > 0:
            if N & 1 == 1:
                ones += 1
                print(current_max)
                current_max += 1
                if current_max > global_max:
                    global_max = current_max
                current_max = 0
            elif ones > 0:
                current_max += 1
            N = N >> 1
           
        if ones == 1:
            return 0
        return global_max
        
# Time: O(log N) - number of bits
# Space: O(1)