class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        compare = {}
        compare2 = {}

        if len(s) != len(t):
            return False
        for letter in s:
            compare[letter]=compare.get(letter,0)+1
        for letter in t:
            compare2[letter]=compare2.get(letter,0)+1

        
        return compare == compare2

        
