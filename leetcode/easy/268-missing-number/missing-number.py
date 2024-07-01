class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for index in range(n):
            if nums[index] != index:
                return index
        return n
            
            
        