class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0

        dp = [0] * (len(t) + 1)
        dp[0] = 1

        for c in s:
            for j in range(len(t), 0, -1):
                if c == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[-1]