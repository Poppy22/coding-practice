class Solution:
    def reverseVowels(self, s: str) -> str:
        start = 0
        end = len(s) - 1
        vowels = "aeiouAEIOU"
        # turn the string into a list, because string are immutable
        s = list(s)
        
        while start <= end:
            if s[start] in vowels and s[end] in vowels:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            elif s[start] in vowels:
                end -= 1
            elif s[end] in vowels:
                start += 1
            else:
                # both are consonants
                start += 1
                end -= 1
            
        # concatenate the letters back to the string
        return "".join(s)


# Time: O(n)
# Space: O(1)