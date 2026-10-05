class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for c in s:
            if c == '(':
                stack.append(0)
            else:
                cur = stack.pop()
                stack[-1] += 1 if cur == 0 else cur << 1

        return stack[0]