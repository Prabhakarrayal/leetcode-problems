from typing import List

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:

        cnt = [0, 0, 0]

        for x in stones:
            cnt[x % 3] += 1

        def check(cnt):
            if cnt[1] == 0:
                return False

           
            cnt[1] -= 1

            moves = 1 + min(cnt[1], cnt[2]) * 2

           
            if cnt[1] > cnt[2]:
                cnt[1] -= 1
                moves += 1

         
            moves += cnt[0]

            return moves % 2 == 1 and cnt[1] != cnt[2]

        
        if check(cnt.copy()):
            return True

        
        swapped = [cnt[0], cnt[2], cnt[1]]

        return check(swapped)