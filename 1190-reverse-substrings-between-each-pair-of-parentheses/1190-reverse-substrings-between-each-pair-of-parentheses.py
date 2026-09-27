class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair = [-1] * n
        stack = []

        # Match parentheses.
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i

        ans = []
        i = 0
        step = 1

        while 0 <= i < n:
            c = s[i]

            if c == '(' or c == ')':
                i = pair[i]
                step = -step
            else:
                ans.append(c)

            i += step

        return ''.join(ans)