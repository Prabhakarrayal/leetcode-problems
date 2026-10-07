class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        ans = []

        def dfs(s, start_i, start_j, left, right):
            balance = 0

            for i in range(start_i, len(s)):
                if s[i] == left:
                    balance += 1
                elif s[i] == right:
                    balance -= 1

                # Found an invalid closing parenthesis.
                if balance < 0:
                    for j in range(start_j, i + 1):
                        if s[j] == right and (
                            j == start_j or s[j - 1] != right
                        ):
                            dfs(
                                s[:j] + s[j + 1:],
                                i,
                                j,
                                left,
                                right
                            )
                    return

            # No invalid closing parenthesis remains.
            reversed_s = s[::-1]

            # First pass: remove extra ')'.
            # Second pass: remove extra '(' by reversing
            # and swapping the two parenthesis roles.
            if left == '(':
                dfs(
                    reversed_s,
                    0,
                    0,
                    ')',
                    '('
                )
            else:
                # We are on the reversed pass.
                # Reverse back before storing.
                ans.append(reversed_s)

        dfs(s, 0, 0, '(', ')')

        return ans