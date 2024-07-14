class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # Step 1: Create the adjacency list for the tree
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        def dfs(node, parent):
            total_time = 0
            for child in tree[node]:
                if child != parent:
                    child_time = dfs(child, node)
                    # If the child or its subtree has an apple, add the traversal time
                    if child_time > 0 or hasApple[child]:
                        total_time += child_time + 2
            return total_time
        
        # Step 2: Start DFS from the root (node 0) and calculate the time
        return dfs(0, -1)