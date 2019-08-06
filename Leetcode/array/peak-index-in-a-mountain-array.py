class Solution(object):
    def peakIndexInMountainArray(self, A):
        start, end = 0, len(A) - 1
        while start < end:
            m = (start + end) // 2
            if A[m] < A[m + 1]:
                start = m + 1
            else:
                end = m
        return end