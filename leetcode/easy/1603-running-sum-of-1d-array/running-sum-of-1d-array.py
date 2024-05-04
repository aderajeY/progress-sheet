class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = sum(nums[0:i+1])
        return ans