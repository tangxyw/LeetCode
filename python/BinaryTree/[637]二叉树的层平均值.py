from CreateTree import TreeNode


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # 层次遍历, 宽度优先
        res = []  # 存放最终结果
        q = []  # 存放每层节点
        if not root:
            return None
        q.append(root)
        sum = 0  # 累积每层节点val的和
        while q:
            tmp = []
            for node in q:
                sum += node.val
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            avg = sum / len(q)  # 求每层节点val的平均值
            res.append(avg)
            sum = 0  # 进入下一层前sum要归0
            q = tmp  # 将下一层节点列表赋值到q
        return res
