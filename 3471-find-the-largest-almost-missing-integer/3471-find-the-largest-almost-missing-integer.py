from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count = [0] * 51
        n = len(nums)

        for i in range(n - k + 1):
            seen = set()

            for j in range(i, i + k):
                seen.add(nums[j])

            for x in seen:
                count[x] += 1

        for x in range(50, -1, -1):
            if count[x] == 1:
                return x

        return -1