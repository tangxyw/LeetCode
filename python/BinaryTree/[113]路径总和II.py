from typing import List, Optional
from .CreateTree import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        track = []

        def traceback(root, track, cur_targetSum):
            if not root:
                return

            track.append(root.val)  # 加入到track的元素是固定, 故可以放到循环外面
            # 到达叶节点, 且当前值等于叶节点值时, 这是一条合法路径
            if not root.left and not root.right and root.val == cur_targetSum:
                self.res.append(track[:])

            for node in [root.left, root.right]:
                traceback(node, track, cur_targetSum - root.val)

            track.pop()  # 在循环体外pop一次即可

        traceback(root, track, targetSum)
        return self.res
