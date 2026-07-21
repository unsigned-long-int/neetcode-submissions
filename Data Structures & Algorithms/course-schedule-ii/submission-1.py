class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ROWS = len(prerequisites)

        neighs = defaultdict(set)

        for i in range(ROWS):
            neighs[prerequisites[i][0]].add(prerequisites[i][1])

        output = []

        visited = set()
        visiting = set()
        def dfs(node):
            if node in visiting:
                return False

            if node in visited:
                return True

            visiting.add(node)
            for n in neighs[node]:
                if not dfs(n):
                    return False
            visiting.remove(node)
            visited.add(node)
            output.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return output