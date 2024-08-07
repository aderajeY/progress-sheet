from math import gcd

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0
        for i in range(n):
            g = nums[i]
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == k:
                    result += 1
                elif g < k:
                    break
        return result