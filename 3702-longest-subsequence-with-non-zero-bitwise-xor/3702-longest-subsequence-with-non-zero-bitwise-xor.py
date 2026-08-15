from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = 0
        has_nonzero = False

        for x in nums:
            total_xor ^= x
            if x != 0:
                has_nonzero = True

        if total_xor != 0:
            return len(nums)

        return len(nums) - 1 if has_nonzero else 0