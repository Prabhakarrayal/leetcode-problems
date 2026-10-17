from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Helper function to calculate the sum of digits of a number
        def get_digit_sum(x: int) -> int:
            total = 0
            while x > 0:
                total += x % 10
                x //= 10
            return total
        
        # Step 1: Create an array of tuples (digit_sum, value, original_index)
        arr = [(get_digit_sum(nums[i]), nums[i], i) for i in range(n)]
        
        # Step 2: Sort the array based on the problem's criteria
        # Python automatically sorts tuples element by element:
        # 1st by digit_sum, 2nd by value, 3rd by original_index
        arr.sort()
        
        # Step 3: Count the minimum swaps by finding cycles
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            # If the element is already visited or it's already in the correct position
            if visited[i] or arr[i][2] == i:
                continue
            
            # Find the size of the current cycle
            cycle_size = 0
            j = i
            
            while not visited[j]:
                visited[j] = True
                j = arr[j][2] # Move to the index where this element originally came from
                cycle_size += 1
                
            # A cycle of size K requires (K - 1) swaps to resolve
            if cycle_size > 1:
                swaps += (cycle_size - 1)
                
        return swaps