class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor_all = 0

        # XOR all the elements in nums
        for num in nums:
            xor_all ^= num

        # XOR the result with all the numbers from 0 to n
        for i in range(n + 1):
            xor_all ^= i

        return xor_all

            
        