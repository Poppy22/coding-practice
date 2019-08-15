class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = [0] * n
        right = [0] * n
        left[0] = 1
        right[n - 1] = 1
        
        for i in range(n - 1):
            left[i + 1] = left[i] * nums[i]
            
        for i in range(n - 1, 0, -1):
            right[i - 1] = right[i] * nums[i]
            
        for i in range(n):
            nums[i] = left[i] * right[i]
            
        return nums
            