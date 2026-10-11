class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        changed = True
        # after, none, s,
        new = []
        while changed:
            changed = False
            new = []
            i = 0
            while i <= len(s) - k:
                if all(x == s[i] for x in s[i:i+k]):
                    i = i+k
                    changed = True
                else:
                    new.append(s[i])
                    i += 1
            new.append(s[i:])
            s = "".join(new)
        return s