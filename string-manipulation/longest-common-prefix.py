class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        word1 = strs[0]
        word2 = strs[1]
        
        # find common prefix between the first two words
        prefix = []
        i = 0
        while i < len(word1) and i < len(word2) and word1[i] == word2[i]:
            prefix += word1[i]
            i += 1
            
        if prefix == []:
            return ""
        
        for j in range(2, len(strs)):
            word1 = prefix
            word2 = strs[j]
            prefix = []
            i = 0
            
            while i < len(word1) and i < len(word2) and word1[i] == word2[i]:
                prefix += word1[i]
                i += 1
            
            if prefix == []:
                return ""
            
        return "".join(prefix)
            

# Time: O(n)
# Space: O(n)