class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        s = sum([customers[i] for i in range(len(customers)) if not grumpy[i]])
        
        final_result = result = sum([customers[i] for i in range(X) if grumpy[i]])
        for i in range(X, len(customers)):
            start, end = i - X, i
            if grumpy[start]:
                result -= customers[start]
            if grumpy[end]:
                result += customers[end]
            final_result = max(result, final_result)
            
        return s + final_result