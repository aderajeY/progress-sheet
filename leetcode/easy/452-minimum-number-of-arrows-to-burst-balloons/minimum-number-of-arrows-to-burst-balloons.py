class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        ans = len(points)
        
        _, prev_end = points[0]
        for index in range(1, len(points)):
            curr_start, curr_end = points[index]
            
            if prev_end >= curr_start:
                ans -= 1
            else:
                prev_end = curr_end
            
        return ans       