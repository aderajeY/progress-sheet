class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        left,right = len(nums)-3,len(nums)-1
        index = 0
        while index <= len(nums) -3:
            if nums[left] + nums[left+1] > nums[right]:
                return nums[left] + nums[left+1] + nums[right]
            index += 1
            left -= 1
            right -= 1
        return 0
            
            