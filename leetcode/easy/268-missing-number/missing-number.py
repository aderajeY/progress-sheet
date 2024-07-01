class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0

        for num in nums:
            xor ^= num

        for i in range(n + 1):
            xor ^= i

        return xor

            
        