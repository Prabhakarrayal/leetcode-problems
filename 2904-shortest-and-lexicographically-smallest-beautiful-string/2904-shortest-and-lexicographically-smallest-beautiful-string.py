class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)

        left = 0
        ones = 0
        ans = ""

        for right in range(n):
            if s[right] == '1':
                ones += 1

            if ones < k:
                continue

           
            while left <= right and s[left] == '0':
                left += 1

            candidate = s[left:right + 1]

            if not ans or len(candidate) < len(ans):
                ans = candidate
            elif len(candidate) == len(ans) and candidate < ans:
                ans = candidate

            
            if s[left] == '1':
                ones -= 1
                left += 1

        return ans