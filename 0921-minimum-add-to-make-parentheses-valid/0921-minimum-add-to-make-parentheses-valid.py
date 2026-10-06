class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = ans = 0

        for c in s:
            if c == '(':
                balance += 1
            elif balance:
                balance -= 1
            else:
                ans += 1

        return ans + balance