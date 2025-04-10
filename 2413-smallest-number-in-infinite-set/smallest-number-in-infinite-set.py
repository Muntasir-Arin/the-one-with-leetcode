import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.curr = 1
        self.added = set()
        self.min_heap = []

    def popSmallest(self) -> int:
        if self.min_heap:
            smallest = heapq.heappop(self.min_heap)
            self.added.remove(smallest)
            return smallest
        else:
            val = self.curr
            self.curr += 1
            return val

    def addBack(self, num: int) -> None:
        if num < self.curr and num not in self.added:
            heapq.heappush(self.min_heap, num)
            self.added.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

