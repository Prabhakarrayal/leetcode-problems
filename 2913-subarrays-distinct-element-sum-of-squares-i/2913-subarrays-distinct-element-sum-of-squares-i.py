class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(n):
            seen = set()
            add = seen.add
            distinct = 0

            for j in range(i, n):
                x = nums[j]
                if x not in seen:
                    add(x)
                    distinct += 1
                ans += distinct * distinct

        return ans