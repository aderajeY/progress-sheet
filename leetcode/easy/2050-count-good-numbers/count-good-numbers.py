class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def power(x,n):
            if n==0:
                return 1
            res=power(x,n//2)
            res=res*res
            res=res%1000000007
            return res*x if n%2 else res

        four=n//2
        fo=power(4,four)%1000000007 if n>1 else 1
        five=(n//2)+1 if n%2==1 else n//2
        fi=power(5,five)%1000000007
        return (fo*fi)%1000000007