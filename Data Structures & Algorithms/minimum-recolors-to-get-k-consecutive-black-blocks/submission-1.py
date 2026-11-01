class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        counts = blocks[:k].count("W")
        res = counts
        for i in range(k, len(blocks)):
            print(counts, i, i-k)
            if blocks[i] == "W":
                counts += 1

            if blocks[i-k] == "W":
                counts -= 1
        
            res = min(counts, res)
        return res