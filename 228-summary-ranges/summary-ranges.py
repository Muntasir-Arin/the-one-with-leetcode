class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []

        s = nums[0] if len(nums)>1 else None
        if s==None:
            return list(map(str, nums))
        for i in range(1,len(nums)):
            if nums[i-1]+1 != nums[i]:
                res.append(str(s) if nums[i-1]==s else f"{s}->{nums[i-1]}")
                s = nums[i]
            if i == len(nums)-1:
                    res.append(str(s) if nums[i]==s else f"{s}->{nums[i]}")

        
        return res
