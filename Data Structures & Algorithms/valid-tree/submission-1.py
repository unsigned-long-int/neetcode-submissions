class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        neighs = defaultdict(set)
        for edge1, edge2 in edges:
            neighs[edge1].add(edge2)
            neighs[edge2].add(edge1)
            

        visiting = set()
        print(neighs)
        def dfs(edge, parent):
            if edge in visiting:
                return False

            visiting.add(edge)
            for n in neighs[edge]:
                if n == parent:
                    continue                
                if not dfs(n, edge):
                    return False
            return True
        return dfs(0, -1) and len(visiting) == n


        