class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ROWS = len(prerequisites)

        neighs = defaultdict(set)
        for i in range(ROWS):
            neighs[prerequisites[i][0]].add(prerequisites[i][1])


        visiting_nodes = set()
        def dfs(node):
            if node in visiting_nodes:
                return False

            if not neighs.get(node, []):
                return True

            visiting_nodes.add(node)
            for n in neighs[node]:
                if not dfs(n):
                    return False
            visiting_nodes.remove(node)
            #neighs[node] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True