class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""
        while n > 0:
            d = n % 26
            if d == 0:
                result = 'Z'+ result
                d = 26
            else:
                result = chr(d + 64) + result
            n = (n - d) // 26
        return result