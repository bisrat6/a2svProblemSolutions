class Solution:
    def pathSum(self, root, targetSum):
        prefix = {0: 1}  # base case
        return self.dfs(root, 0, targetSum, prefix)

    def dfs(self, node, curr_sum, targetSum, prefix):
        if not node:
            return 0
        
        # update running sum
        curr_sum += node.val
        
        # count paths ending here
        count = prefix.get(curr_sum - targetSum, 0)
        
        # add current sum to hashmap
        prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
        
        # explore children
        count += self.dfs(node.left, curr_sum, targetSum, prefix)
        count += self.dfs(node.right, curr_sum, targetSum, prefix)
        
        # backtrack
        prefix[curr_sum] -= 1
        
        return count