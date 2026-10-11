class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        i = len(s)-1
        while s[i] == "":
            i -= 1
        return len(s[i])