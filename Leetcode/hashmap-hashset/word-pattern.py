class Solution(object):
    def wordPattern(self, pattern, string):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = string.split(' ')
        if len(words) != len(pattern):
            return False
        
        replacements = {}
        for i in range(len(words)):
            if pattern[i] not in replacements.keys():
                if words[i] not in replacements.values():
                    replacements[pattern[i]] = words[i]
                else:
                    # one word could not be matched with two different letters
                    return False
            elif replacements[pattern[i]] != words[i]:
                # incorrect match from previous data
                return False
        
        return True