class Solution:
  def minEatingSpeed(self, piles: list[int], h: int) -> int:
    def eatHours(m: int) -> bool:
      return sum((pile - 1) // m + 1 for pile in piles)
    l = 1
    r = max(piles)
    return bisect.bisect_left(range(l, r), True,
                              key=lambda m: eatHours(m) <= h) + l