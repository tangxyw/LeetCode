from typing import List, Optional
from .CreateTree import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        track = []

        def traceback(root, track, cur_targetSum):
            if not root:
                return

            # 到达叶节点, 且当前值等于叶节点值时, 这是一条合法路径
            if not root.left and not root.right and root.val == cur_targetSum:
                self.res.append(track + [root.val])
                return

            if root.left:  # 若左子树存在, 在左子树上递归+回溯
                track.append(root.val)
                traceback(root.left, track, cur_targetSum - root.val)
                track.pop()
            if root.right:  # 若右子树存在, 在右子树上递归+回溯
                track.append(root.val)
                traceback(root.right, track, cur_targetSum - root.val)
                track.pop()

        traceback(root, track, targetSum)
        return self.res
