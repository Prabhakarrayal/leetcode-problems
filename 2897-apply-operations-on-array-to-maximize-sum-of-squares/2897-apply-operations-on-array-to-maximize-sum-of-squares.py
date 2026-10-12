class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        cnt = [0] * 31

        for x in nums:
            while x:
                bit = x & -x
                cnt[bit.bit_length() - 1] += 1
                x ^= bit

        ans = 0

        for _ in range(k):
            x = 0
            for b in range(31):
                if cnt[b]:
                    x |= 1 << b
                    cnt[b] -= 1

            ans = (ans + x * x) % MOD

        return ans