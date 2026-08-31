# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        index = 1

        first = -1
        last = -1
        min_dist = float('inf')

        while curr.next:
            nxt = curr.next

            
            if ((prev.val < curr.val > nxt.val) or
                (prev.val > curr.val < nxt.val)):

                if first == -1:
                    first = index
                else:
                    min_dist = min(min_dist, index - last)

                last = index

            prev = curr
            curr = nxt
            index += 1

        
        if first == -1 or first == last:
            return [-1, -1]

        return [min_dist, last - first]