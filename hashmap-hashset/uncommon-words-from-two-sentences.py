class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        dict_A = {}
        dict_B = {}
        
        if A == "":
            return B.split(" ")
        
        if B == "":
            return A.split(" ")
        
        for a in A.split(" "):
            if a in dict_A.keys():
                dict_A[a] += 1
            else:
                dict_A[a] = 1
        
        for b in B.split(" "):
            if b in dict_B.keys():
                dict_B[b] += 1
            else:
                dict_B[b] = 1
              
        result = []
        for w in dict_A.keys():
            if dict_A[w] == 1 and not w in dict_B.keys():
                result.append(w)
                
        for w in dict_B.keys():
            if dict_B[w] == 1 and not w in dict_A.keys():
                result.append(w)
                
        return result