class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {} 

        for i, num in enumerate(nums): 
            hash_map[num] = i 

        for i, num in enumerate(nums): 
            
            if target - num in hash_map and hash_map[target - num] != i: 
                return [i, hash_map[target - num]] 
                
        return []