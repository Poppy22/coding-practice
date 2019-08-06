
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = {"a":".-",
                 "b":"-...",
                 "c":"-.-.",
                 "d":"-..",
                 "e":".",
                 "f":"..-.",
                 "g":"--.",
                 "h":"....",
                 "i":"..",
                 "j":".---",
                 "k":"-.-",
                 "l":".-..",
                 "m":"--",
                 "n":"-.",
                 "o":"---",
                 "p":".--.",
                 "q":"--.-",
                 "r":".-.",
                 "s":"...",
                 "t":"-",
                 "u":"..-",
                 "v":"...-",
                 "w":".--",
                 "x":"-..-",
                 "y":"-.--",
                 "z":"--.."}
        
        unique = {}
        
        for word in words:
            morse_word = ""
            for letter in word:
                morse_word += morse[letter]
                
            if morse_word not in unique.keys():
                unique[morse_word] = 1
                
        return len(unique)