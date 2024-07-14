class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for i in range(n + 1)]

        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        colored = [-1] * (n + 1)

        for i in range(1, n + 1):
            if colored[i] == -1:
                if self.bipartite(i, graph, colored, 0) == 0:
                    return 0

        return 1

    def bipartite(self, node, graph, colored, color):
        colored[node] = color

        for nei in graph[node]:
            if colored[nei] == -1:
                if self.bipartite(nei, graph, colored, not color) == 0:
                    return 0
            elif colored[nei] == colored[node]:
                return 0
        return 1