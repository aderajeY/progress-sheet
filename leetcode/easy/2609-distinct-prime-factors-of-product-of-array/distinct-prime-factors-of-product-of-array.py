class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int: 
        def prime(a):
            ans = set()            
            for i in range (len(a)) :
                if a[i] == 2:
                    ans.add(2)
                    continue
                sqr = int(math.sqrt(a[i]))
                for j in range(2, sqr+1) :
                    if (a[i] % j == 0) :
                        ans.add(j)
                        while (a[i] % j == 0) :
                            a[i] //= j
                if (a[i] > 2) :
                    ans.add(a[i])
            return len(ans)

        return prime(nums)