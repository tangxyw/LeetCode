from CreateTree import TreeNode

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def getDepth(root: TreeNode) -> int:
            """返回经以节点root为子树的深度, 计算以root为转折点的直径"""
            if not root:
                return 0
            left_depth = getDepth(root.left)
            right_depth = getDepth(root.right)
            self.max_diameter = max(self.max_diameter, left_depth+right_depth)  # 更新最长路径
            return max(left_depth, right_depth) + 1
        self.max_diameter = 0
        getDepth(root)
        return self.max_diameter