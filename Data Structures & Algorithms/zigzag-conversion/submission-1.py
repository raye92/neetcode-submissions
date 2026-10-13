class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [[] for _ in range(numRows)]
        si = 0
        ri = 0
        delta = 1
        while si < len(s):
            res[ri].append(s[si])
            si += 1
            ri += delta
            if ri == numRows - 1:
                delta = -1
            if ri == 0:
                delta = 1
        final = ""
        for l in res:
            final += "".join(l)
        return final