class Solution:
    def rob_helper(self, nums, start, end):
        if start == end:
            return nums[start]
        
        result = [0] * len(nums)
        result[start] = nums[start]
        result[start + 1] = max(result[start], nums[start + 1])
        
        for i in range(start + 2, end + 1):
            result[i] = max(result[i - 1], result[i - 2] + nums[i])
            
        return result[end]
    
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        max1 = self.rob_helper(nums, 0, len(nums) - 2)
        max2 = self.rob_helper(nums, 1, len(nums) - 1)
            
        return max(max1, max2)