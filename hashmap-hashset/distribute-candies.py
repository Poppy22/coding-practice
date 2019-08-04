### Set - faster, shorter

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        freq = set()
        for candy in candies:
            freq.add(candy)
                
        return min(len(freq), len(candies) // 2)



### Dictionary - time limit exceeded, but explains the idea

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        freq = {}
        for candy in candies:
            if candy in freq.keys():
                freq[candy] += 1
            else:
                freq[candy] = 1
         
        sister = 0
        types = 0
        brother = 0
        for c in freq.keys():
            if freq[c] > 1:
                sister += 1
                brother += freq[c] - 1
            else:
                sister += 1
                
        # sister only has one candy from each type and has all unique candies
        if sister <= brother:
            # the have the same number or candies or
            # the brother has more and when he gives candies to his sister
            # it will be duplicates, so this is the maximum number of types
            return sister
        
        # some candies have to go to the brother in order to balance the number
        # sister has only one candy from each type, so the balance is half of the total candies
        return len(candies) // 2
        