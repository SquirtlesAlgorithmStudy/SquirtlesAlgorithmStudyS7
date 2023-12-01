import sys
from math import ceil, log2
input = sys.stdin.readline

N, M, K = map(int, input().split())

numbers = [int(input()) for _ in range(N)]
commands = [tuple(map(int, input().split())) for _ in range(M + K)]


class SegTree():
    def __init__(self, numbers):
        self.numbers = numbers
        height = ceil(log2(len(numbers)))
        tree_size = 1 << (height + 1)
        self.tree = [0] * tree_size
        self._build(1, 0, len(self.numbers) - 1)

    def _build(self, node, start, end):
        if start == end:
            self.tree[node] = self.numbers[start]
            return

        mid = (start + end) // 2
        self._build(2 * node, start, mid)
        self._build(2 * node + 1, mid+1, end)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]
        return

    def query(self, left_idx, right_idx):
        return self._query(1, 0, len(self.numbers) - 1, left_idx, right_idx)

    def _query(self, node, start, end, left, right):
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        left_child = self._query(2 * node, start, mid, left, right)
        right_child = self._query(2 * node + 1, mid + 1, end, left, right)
        return left_child + right_child

    def update(self, idx, to_value):
        self._update(1, 0, len(self.numbers) - 1, idx, to_value)

    def _update(self, node, start, end, index, val):
        if start == end:
            self.tree[node] = val
            return

        mid = (start + end) // 2
        if start <= index and index <= mid:
            self._update(node * 2, start, mid, index, val)
        else:
            self._update(node * 2 + 1, mid + 1, end, index, val)

        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]


seg_tree = SegTree(numbers)
for command in commands:
    if command[0] == 1:
        seg_tree.update(command[1]-1, command[2])
    else:
        print(seg_tree.query(command[1]-1, command[2]-1))
