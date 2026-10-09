class Solution:
    def minInsertions(self, s: str) -> int:
        ans = need = 0

        for c in s:
            if c == '(':
                if need & 1:
                    ans += 1
                    need -= 1
                need += 2
            else:
                need -= 1
                if need < 0:
                    ans += 1
                    need = 1

        return ans + need