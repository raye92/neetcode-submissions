class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        indeg = {ch: 0 for word in words for ch in word}
        graph = defaultdict(set) # letter, set(following letters)
        for i in range(len(words)-1):
            before = words[i]
            after = words[i+1]
            if len(before) > len(after) and before[:len(after)] == after:
                return ""
            i = 0
            while i < min(len(before), len(after)):
                if before[i] == after[i]:
                    i += 1
                    continue
                b = before[i]
                a = after[i]
                if a not in graph[b]:
                    graph[b].add(a)
                    indeg[a] += 1
                break
        print("INDEG", indeg)
        q = deque()
        for let in indeg:
            if indeg[let] == 0:
                q.append(let)
        
        res = []
        while(q):
            c = q.popleft()
            res.append(c)
            for sub in graph[c]:
                indeg[sub] -= 1
                if indeg[sub] == 0:
                    q.append(sub)
        print(res)
        print(graph)
        return "".join(res) if len(res) == len(indeg) else ""


