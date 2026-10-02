class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        path = []

        def dfs(opened, closed):
            if opened == n and closed == n:
                ans.append(''.join(path))
                return

            if opened < n:
                path.append('(')
                dfs(opened + 1, closed)
                path.pop()

            if closed < opened:
                path.append(')')
                dfs(opened, closed + 1)
                path.pop()

        dfs(0, 0)
        return ans