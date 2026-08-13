from typing import List

class Node:
    __slots__ = ("l", "r", "lmx", "rmx", "mx")

    def __init__(self, l=0, r=0):
        self.l = l
        self.r = r
        self.lmx = 1
        self.rmx = 1
        self.mx = 1


class SegmentTree:

    def __init__(self, s):
        self.s = list(s)
        n = len(s)
        self.tr = [None] * (4 * n)
        self.build(1, 1, n)

    def build(self, u, l, r):
        self.tr[u] = Node(l, r)
        if l == r:
            return
        mid = (l + r) >> 1
        self.build(u << 1, l, mid)
        self.build(u << 1 | 1, mid + 1, r)
        self.pushup(u)

    def pushup(self, u):
        root = self.tr[u]
        left = self.tr[u << 1]
        right = self.tr[u << 1 | 1]

        root.lmx = left.lmx
        root.rmx = right.rmx
        root.mx = max(left.mx, right.mx)

        lenL = left.r - left.l + 1
        lenR = right.r - right.l + 1

        if self.s[left.r - 1] == self.s[right.l - 1]:

            if left.lmx == lenL:
                root.lmx += right.lmx

            if right.rmx == lenR:
                root.rmx += left.rmx

            root.mx = max(root.mx, left.rmx + right.lmx)

    def modify(self, u, pos, ch):
        node = self.tr[u]

        if node.l == node.r:
            self.s[pos - 1] = ch
            return

        mid = (node.l + node.r) >> 1

        if pos <= mid:
            self.modify(u << 1, pos, ch)
        else:
            self.modify(u << 1 | 1, pos, ch)

        self.pushup(u)


class Solution:
    def longestRepeating(self, s: str,
                         queryCharacters: str,
                         queryIndices: List[int]) -> List[int]:

        tree = SegmentTree(s)

        ans = []

        for idx, ch in zip(queryIndices, queryCharacters):
            tree.modify(1, idx + 1, ch)
            ans.append(tree.tr[1].mx)

        return ans