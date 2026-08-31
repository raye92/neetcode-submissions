class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set) # before: set(after)
        indeg = {l: 0 for w in words for l in w} # letters: number of indeg
        for i in range(len(words)-1):
            fw = words[i]
            sw = words[i+1]
            end = min(len(fw), len(sw))
            if len(fw) != len(sw) and fw[:end] == sw:
                return ""
            for d in range(end):
                before = fw[d]
                after = sw[d]
                if before == after:
                    continue
                if after not in graph[before]:
                    graph[before].add(after)
                    indeg[after] += 1
                break
        
        res = []
        q = deque()
        for l, i in indeg.items():
            if i == 0:
                q.append(l)
        
        while q:
            let = q.popleft()
            res.append(let)
            for sub in graph[let]:
                indeg[sub] -= 1
                if indeg[sub] == 0:
                    q.append(sub)
        return "".join(res) if len(res) == len(indeg) else ""

        