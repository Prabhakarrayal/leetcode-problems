from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        litter = {}
        start = -1
        litter_count = 0

        
        for r in range(m):
            for c in range(n):
                ch = classroom[r][c]

                if ch == 'S':
                    start = r * n + c

                elif ch == 'L':
                    litter[r * n + c] = litter_count
                    litter_count += 1

        
        if litter_count == 0:
            return 0

        full_mask = (1 << litter_count) - 1

        
        cells = m * n
        best = bytearray((1 << litter_count) * cells)

        start_state = (0, start, energy)
        q = deque([start_state])

        best[start] = energy

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        moves = 0

        while q:
            for _ in range(len(q)):
                mask, pos, en = q.popleft()

                r = pos // n
                c = pos % n

               
                idx = mask * cells + pos
                if best[idx] > en:
                    continue

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                   
                    if en == 0:
                        continue

                    np = nr * n + nc
                    new_en = en - 1
                    new_mask = mask

                    ch = classroom[nr][nc]

                    
                    if ch == 'L':
                        bit = 1 << litter[np]
                        new_mask |= bit

                   
                    if ch == 'R':
                        new_en = energy

                   
                    if new_mask == full_mask:
                        return moves + 1

                    idx = new_mask * cells + np

                    
                    if new_en > best[idx]:
                        best[idx] = new_en
                        q.append((new_mask, np, new_en))

            moves += 1

        return -1