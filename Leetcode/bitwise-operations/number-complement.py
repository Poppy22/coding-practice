class Solution:
    def findComplement(self, num: int) -> int:
        i = 0
        result = 0
        while num > 0:
            if num & 1 == 0:
                result += 2 ** i
            num = num >> 1
            i += 1
            
        return result

# Time: O(log N) - number of bits
# Space: O(1)