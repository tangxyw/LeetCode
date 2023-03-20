from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        track = ''

        # 转换为在深度为2n的满二叉树上进行深度优先遍历+剪枝
        # 左子节点代表在当前路径track后加'(', 右子节点代表在当前路径track后加')'
        def dfs(left, right, track):
            """
            Args:
                left (int): '('在track中出现的次数
                right (int):  ')'在track中出现的次数
                track (str): 当前括号组合字符串
            """
            if left == n and right == n:    # 到达2n层叶节点, 所有括号都已添加完
                self.res.append(track)
                return

            if left > n or right > left:    # 左括号数量超过n 或者 当前右括号数量比左括号多, 剪枝
                return

            # 向左右子树递归
            dfs(left+1, right, track+'(')
            dfs(left, right+1, track+')')

        dfs(0, 0, track)
        return self.res

