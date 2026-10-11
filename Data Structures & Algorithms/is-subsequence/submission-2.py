class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        si = 0
        for ch in t:
            if ch == s[si]:
                si += 1
                if si == len(s):
                    return True
                
        return si == len(s)