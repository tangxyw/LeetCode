from typing import List, Optional
from CreateTree import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        track = []
        res = []

        def traceback(root: Optional[TreeNode], track: List[int], target: int) -> None:
            if not root:
                return

            # 根节点
            if not root.left and not root.right:
                if root.val == target:
                    res.append(track + [root.val])
                return

            # 递归&回溯
            track.append(root.val)
            traceback(root.left, track, target - root.val)
            traceback(root.right, track, target - root.val)
            track.pop()

        traceback(root, track, targetSum)

        return res
