class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        zeros = 1 if s[0] == '0' else 0
        ones = sum(1 for ch in s[1:] if ch == '1')

        ans = zeros + ones
        for i in range(1, n - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1
            ans = max(ans, zeros + ones)

        return ans