class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        nums = set(nums)  
        longest = 1
        cnt = 1
        for x in nums:
            if x - 1 not in nums:
                cnt = 1
                it = x
                while it + 1 in nums:
                    it += 1
                    cnt += 1
                longest = max(cnt, longest)

        return longest