class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = [num for num in range(len(nums) + 1)]
        for j in arr:
            if j not in nums:
                return j 
                