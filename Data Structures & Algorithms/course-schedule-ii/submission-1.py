class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = [0] * numCourses
        courseMap = defaultdict(set)
        for after, before in prerequisites:
            if after not in courseMap[before]:
                indeg[after] += 1
                courseMap[before].add(after)
        
        q = deque()
        for i in range(len(indeg)):
            if indeg[i] == 0:
                q.append(i)
        
        res = []
        while q:
            course = q.popleft()
            res.append(course)
            for sub in courseMap[course]:
                indeg[sub] -= 1
                if indeg[sub] == 0:
                    q.append(sub)
        
        return res if len(res) == numCourses else []