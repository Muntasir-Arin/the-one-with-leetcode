class SegmentTree:
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, index: int, value: int):
        index += self.n
        self.tree[index] = value
        index //= 2
        while index >= 1:
            self.tree[index] = max(self.tree[2 * index], self.tree[2 * index + 1])
            index //= 2

    def get_max(self, left: int, right: int) -> int:
        left += self.n
        right += self.n
        max_val = 0
        while left <= right:
            if left % 2 == 1:
                max_val = max(max_val, self.tree[left])
                left += 1
            if right % 2 == 0:
                max_val = max(max_val, self.tree[right])
                right -= 1
            left //= 2
            right //= 2
        return max_val


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        seg = SegmentTree(baskets)
        unplaced = 0
        n = len(baskets)

        for fruit in fruits:
            if seg.get_max(0, n - 1) < fruit:
                unplaced += 1
            else:
                low, high = 0, n - 1
                while low < high:
                    mid = low + (high - low) // 2
                    if seg.get_max(low, mid) < fruit:
                        low = mid + 1
                    else:
                        high = mid
                seg.update(low, 0)

        return unplaced
