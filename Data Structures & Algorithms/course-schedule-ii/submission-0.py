class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = [0] * numCourses
        graph = defaultdict(list) #course, courses to take after
        independent = {x for x in range(numCourses)}
        for after, before in prerequisites:
            graph[before].append(after)
            independent.discard(after)
            indeg[after] += 1

        q = deque(independent)
        res = []
        while q:
            course = q.popleft()
            res.append(course)
            for dep in graph[course]:
                indeg[dep] -= 1
                if indeg[dep] == 0:
                    q.append(dep)
                
        return res if len(res) == numCourses else []