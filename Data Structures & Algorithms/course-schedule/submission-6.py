class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = [0] * numCourses
        graph = defaultdict(list) #course, courses to take after
        independent = {x for x in range(numCourses)}
        for after, before in prerequisites:
            graph[before].append(after)
            independent.discard(after)
            indeg[after] += 1

        q = deque(independent)
        while q:
            course = q.popleft()
            for dep in graph[course]:
                indeg[dep] -= 1
                if indeg[dep] == 0:
                    q.append(dep)
                
        return True if sum(indeg) == 0 else False