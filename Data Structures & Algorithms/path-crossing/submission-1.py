class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = set()
        seen.add((0, 0))
        curr = [0, 0]
        for d in path:
            if d == "N":
                curr[0] += 1
            elif d == "S":
                curr[0] -= 1
            elif d == "E":
                curr[1] += 1
            else:
                curr[1] -= 1
            if tuple(curr) in seen:
                return True
            seen.add(tuple(curr))
        return False