class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for x in nums:
            result ^= x
            
        return result

# Time: O(n)
# Space: O(1)