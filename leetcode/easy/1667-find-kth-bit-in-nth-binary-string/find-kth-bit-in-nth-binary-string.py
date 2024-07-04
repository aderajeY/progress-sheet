class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def inverse(s):
            res=""
            for i in s:
                if i=='1': res+='0'
                else: res+='1'
            return res[::-1]

        s="0"
        for i in range(n-1):
            s=s+'1'+inverse(s)
        return s[k-1]