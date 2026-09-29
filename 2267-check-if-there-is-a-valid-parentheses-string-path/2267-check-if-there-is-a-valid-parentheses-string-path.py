class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        # Path contains exactly m + n - 1 characters.
        # A valid parentheses string must have even length.
        if (m + n - 1) & 1:
            return False

        # A valid parentheses string must start with '('
        # and end with ')'.
        if grid[0][0] != '(' or grid[m - 1][n - 1] != ')':
            return False

        # dp[j] = bitset of reachable balances at column j
        # for the current row.
        dp = [0] * n

        # Starting '(' gives balance = 1.
        dp[0] = 1 << 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                states = 0

                # From top.
                if i:
                    states |= dp[j]

                # From left.
                if j:
                    states |= dp[j - 1]

                if grid[i][j] == '(':
                    dp[j] = states << 1
                else:
                    dp[j] = states >> 1

        # Bit 0 means balance 0 is reachable.
        return bool(dp[n - 1] & 1)