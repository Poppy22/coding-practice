class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {}
        for n in nums1:
            if n not in d.keys():
                d[n] = True
           
        result = []
        for n in nums2:
            if n in d.keys():
                result.append(n)
                del d[n]
                
        return result