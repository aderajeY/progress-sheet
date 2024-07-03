class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        
        index = 0
        while index <= len(nums) -3:
            if nums[index] < nums[index+1] + nums[index+2]:
                return nums[index] + nums[index+1] + nums[index+2]
            index += 1
            
        return 0
            
            