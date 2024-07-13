class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)

        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                cur = len(graph[i]) + len(graph[j]) - int(i in graph[j])

                if cur > ans:
                    ans = cur

        return ans