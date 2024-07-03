class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        
        one,zero,negOne = [1]*numOnes,[0]*numZeros,[-1]*numNegOnes
        result = one+zero+negOne
        ans = 0
        for i in range(k):
            ans += result[i]
        return ans
        