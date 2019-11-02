class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        result = [0] * len(nums)
        result[0] = nums[0]
        result[1] = nums[0]
        
        if nums[1] > nums[0]:
            result[1] = nums[1]
        
        for i in range(2, len(nums)):
            result[i] = max(result[i - 1], result[i - 2] + nums[i])
            
        return result[-1]