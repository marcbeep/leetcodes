# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        rootIndex = len(nums)//2
        root = TreeNode(nums[rootIndex])
        
        root.left  = self.sortedArrayToBST(nums[:rootIndex])
        root.right = self.sortedArrayToBST(nums[rootIndex + 1:])

        return root
