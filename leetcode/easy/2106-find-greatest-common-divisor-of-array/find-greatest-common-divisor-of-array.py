class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        less = nums[0]
        large = nums[n-1]
        for i in range(large,-1,-1):
            if less % i == 0 and large % i == 0:
                return i
        return 1
        