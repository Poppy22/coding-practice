class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) >= 2:
            if word[0] >= 'A' and word[0] <= 'Z' and word[1] >= 'A' and word[1] <= 'Z':
                # check for all the other letters to be capital
                for i in range(2, len(word)):
                    if not(word[i] >= 'A' and word[i] <= 'Z'):
                        return False
                return True
            
            if not(word[0] >= 'A' and word[0] <= 'Z') and word[1] >= 'A' and word[1] <= 'Z':
                return False
                
            if word[0] >= 'A' and word[0] <= 'Z' and not(word[1] >= 'A' and word[1] <= 'Z') or not(word[0] >= 'A' and word[0] <= 'Z'):
                # check for all the other letters to be small
                for i in range(2, len(word)):
                    if word[i] >= 'A' and word[i] <= 'Z':
                        return False
                return True
            
        # it has only one letter or the string is empty
        return True

# Time: O(n)
# Space: O(1)