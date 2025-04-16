class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        max_total = nums[0]
        for i in nums:
            total+=i
            max_total = max(total, max_total)
            if total<0:
                total=0
        return max_total