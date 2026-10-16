from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Parallel arrays for Segment Tree to avoid overhead (faster than objects in Python)
        # Tree size is 4 * N
        sum1 = [0] * (4 * n)  # sum of counts
        sum2 = [0] * (4 * n)  # sum of squares of counts
        lazy = [0] * (4 * n)  # lazy propagation array
        
        def update(node: int, L: int, R: int, ql: int, qr: int):
            # If the current segment is fully within the query range
            if ql <= L and R <= qr:
                length = R - L + 1
                # Math: (C + 1)^2 = C^2 + 2C + 1
                # Sum of (C+1)^2 = Sum of C^2 + 2*(Sum of C) + 1*(Length)
                sum2[node] = (sum2[node] + 2 * sum1[node] + length) % MOD
                sum1[node] = (sum1[node] + length) % MOD
                lazy[node] += 1
                return
            
            mid = (L + R) // 2
            left = 2 * node
            right = 2 * node + 1
            
            # Push down the pending lazy updates to children
            lz = lazy[node]
            if lz:
                len_left = mid - L + 1
                sum2[left] = (sum2[left] + 2 * lz * sum1[left] + lz * lz * len_left) % MOD
                sum1[left] = (sum1[left] + lz * len_left) % MOD
                lazy[left] += lz
                
                len_right = R - mid
                sum2[right] = (sum2[right] + 2 * lz * sum1[right] + lz * lz * len_right) % MOD
                sum1[right] = (sum1[right] + lz * len_right) % MOD
                lazy[right] += lz
                
                lazy[node] = 0  # Clear lazy for current node
                
            # Recursively update overlapping halves
            if ql <= mid:
                update(left, L, mid, ql, qr)
            if qr > mid:
                update(right, mid + 1, R, ql, qr)
                
            # Backtrack and combine results for current node
            sum1[node] = (sum1[left] + sum1[right]) % MOD
            sum2[node] = (sum2[left] + sum2[right]) % MOD
            
        last_seen = {}
        total_sum_of_squares = 0
        
        # Iterate through the array, expanding the right boundary `i`
        for i, x in enumerate(nums):
            prev = last_seen.get(x, -1)
            
            # x is a newly seen distinct element for all subarrays starting between prev+1 and i
            update(1, 0, n - 1, prev + 1, i)
            
            # Update the last seen position of x
            last_seen[x] = i
            
            # sum2[1] always holds the total sum of squares of counts for all subarrays ending at i
            total_sum_of_squares = (total_sum_of_squares + sum2[1]) % MOD
            
        return total_sum_of_squares