class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] not in dict:
                # create a new entrance
                dict[nums[i]] = i
            else:
                return [dict[target - nums[i]], i]