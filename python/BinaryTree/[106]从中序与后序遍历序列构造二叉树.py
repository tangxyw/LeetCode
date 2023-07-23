from .CreateTree import TreeNode
from typing import List, Optional


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(inorder_start: int, inorder_end: int, postorder_start: int, postorder_end: int) -> Optional[TreeNode]:
            if inorder_start > inorder_end or postorder_start > postorder_end:
                return None

            root_val = postorder[postorder_end]
            root_index = inorder.index(root_val)
            root = TreeNode(root_val)

            # 左子树
            left_inorder_start = inorder_start
            left_inorder_end = root_index - 1
            left_postorder_start = postorder_start
            left_postorder_end = left_postorder_start + left_inorder_end - left_inorder_start

            # 右子树
            right_inorder_start = root_index + 1
            right_inorder_end = inorder_end
            right_postorder_start = left_postorder_end + 1
            right_postorder_end = postorder_end - 1

            root.left = helper(left_inorder_start, left_inorder_end, left_postorder_start, left_postorder_end)
            root.right = helper(right_inorder_start, right_inorder_end, right_postorder_start, right_postorder_end)

            return root

        return helper(0, len(inorder) - 1, 0, len(postorder) - 1)
