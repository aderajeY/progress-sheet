class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = [False for i in range(len(rooms))]
        self.IsPossible(rooms, 0, visited)

        for visit in visited:
            if(visit == False):
                return False
        return True

    def IsPossible(self, rooms, index, visited):

        if(visited[index] == True):
            return
        
        visited[index] = True
        for key in rooms[index]:
            if(visited[key] == False):
                self.IsPossible(rooms, key, visited)
        return