class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        visited=[0]*n
        res=[]
        for i in range(len(edges)):
            visited[edges[i][1]]+=1
        for i in range(n):
            if(visited[i]==0):
                res.append(i)
        return res
