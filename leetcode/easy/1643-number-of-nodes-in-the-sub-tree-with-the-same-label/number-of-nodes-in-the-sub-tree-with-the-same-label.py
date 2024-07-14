ORD_A = ord('a')

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj_list = [[] for _ in range(n)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        count = [0] * 26
       
        first_seen = [-1] * n

        stack = [0]
        while stack:
            node = stack[-1]

            label = ord(labels[node]) - ORD_A
            
            if first_seen[node] == -1:
                first_seen[node] = count[label]
                count[label] += 1
                
                for neigh in adj_list[node]:
                    if first_seen[neigh] == -1:
                        stack.append(neigh)
            else:
                stack.pop()
                
                first_seen[node] = count[label] - first_seen[node]
        
        return first_seen