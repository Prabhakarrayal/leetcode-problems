class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        diff = 0
        q = 0

        for i in range(half):
            if num[i] == '?':
                q += 1
            else:
                diff += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                q -= 1
            else:
                diff -= int(num[i])

        
        return 2 * diff + 9 * q != 0