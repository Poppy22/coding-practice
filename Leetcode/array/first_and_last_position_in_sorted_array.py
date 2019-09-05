class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) > 0 and (target < nums[0] or target > nums[len(nums) - 1]):
            return [-1, -1]
        
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]
        
        start = 0
        end = len(nums) - 1
        first = last = -1
        
        while start <= end:
            middle = (start + end) // 2
            if nums[middle] == target:
                prev_middle = middle
                
                # search for first
                positions_to_left = 0
                while nums[middle] == target and middle - 1 >= 0:
                    middle -= 1
                    if nums[middle] == target:
                        positions_to_left += 1
                    
                first = prev_middle - positions_to_left
                
                # search for last
                middle = prev_middle
                positions_to_right = 0
                while nums[middle] == target and middle + 1 < len(nums):
                    middle += 1
                    if nums[middle] == target:
                        positions_to_right += 1
                last = prev_middle + positions_to_right
                
                break
                
            elif nums[middle] < target:
                # search in the right half
                start = middle + 1
            else:
                # search in the left half
                end = middle - 1
                
        return [first, last]