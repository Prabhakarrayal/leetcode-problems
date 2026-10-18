import math

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        def dfs(arr: list[int]) -> int:
            # Base case: A tree with 2 or fewer nodes only has 1 valid ordering
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            
            # Maintain the relative order of elements going to left and right subtrees
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            
            # Calculate how many ways we can interleave the left and right elements
            # math.comb(n, k) calculates n! / (k! * (n - k)!)
            interleave_ways = math.comb(len(left) + len(right), len(left))
            
            # Recursively calculate ways for left and right subtrees
            left_ways = dfs(left)
            right_ways = dfs(right)
            
            # Multiply them all together modulo 10^9 + 7
            return (interleave_ways * left_ways * right_ways) % MOD
            
        # Subtract 1 because we want to exclude the original array itself
        return (dfs(nums) - 1) % MOD