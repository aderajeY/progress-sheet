class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        result = []
        for negOne in range(numNegOnes):
            result.append(-1)
        for zero in range(numZeros):
            result.append(0)
        for one in range(numOnes):
            result.append(1)
        return sum(result[len(result) - k:])
        