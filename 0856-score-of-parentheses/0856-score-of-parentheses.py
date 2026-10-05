class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = depth = 0

        for i, c in enumerate(s):
            if c == '(':
                depth += 1
            else:
                depth -= 1
                if s[i - 1] == '(':
                    ans += 1 << depth

        return ans