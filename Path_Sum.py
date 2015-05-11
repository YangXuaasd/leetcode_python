# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum): 
        ret = False
        if root == None:
            return ret
        sum -= root.val
        if sum == 0 and root.left == None and root.right == None:
            ret = True
        return ret or self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)
