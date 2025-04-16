class Solution:
  def maxSubarraySumCircular(self, A: List[int]) -> int:
    totalSum = 0 #7
    currMaxSum = 0 #7
    currMinSum = 0 #2
    maxSum = -math.inf #7
    minSum = math.inf #-3

    for a in A:
      totalSum += a
      currMaxSum = max(currMaxSum + a, a)
      currMinSum = min(currMinSum + a, a)
      maxSum = max(maxSum, currMaxSum)
      minSum = min(minSum, currMinSum)

    return maxSum if maxSum < 0 else max(maxSum, totalSum - minSum)