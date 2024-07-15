class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c=Counter(answers)
        return sum(ceil(c[i]/(i+1))*(i+1) for i in c)