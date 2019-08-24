class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 1 or len(nums) == 2:
            return -1
        
        S = sum(nums)
        if S - nums[0] == 0:
            return 0
        nums.append(0)
        
        s = 0
        for i in range(len(nums) - 1):
            if S == 2 * s + nums[i]:
                return i
            s += nums[i]
            
        return -1