class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ROWS = len(prerequisites)

        neighs = defaultdict(set)
        for r in range(ROWS):
            neighs[prerequisites[r][0]].add(prerequisites[r][1])

        visiting = set()
        def dfs(course):
            if course in visiting:
                return False
            if neighs[course] == []:
                return True
            
            visiting.add(course)
            for n in neighs[course]:
                if not dfs(n):
                    return False
            visiting.remove(course)
            neighs[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
                