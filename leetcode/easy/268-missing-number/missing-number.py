class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
    
        for counter,value in enumerate(nums):

            result ^= counter+1 # XOR result with numbers from the complete series
            result ^= value # XOR with the numbers given in num series

        return result
        