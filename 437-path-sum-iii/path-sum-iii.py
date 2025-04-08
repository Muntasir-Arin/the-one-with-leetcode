# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sum_count = {0: 1} 
        def dfs(node, current_sum) -> int:
            if node is None:
                return 0
            
            current_sum += node.val
            num_paths = prefix_sum_count.get(current_sum - targetSum, 0)
            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1

            num_paths += dfs(node.left, current_sum)
            num_paths += dfs(node.right, current_sum)
            
            prefix_sum_count[current_sum] -= 1
            return num_paths
        
        return dfs(root, 0)