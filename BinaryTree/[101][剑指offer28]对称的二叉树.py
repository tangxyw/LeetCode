from typing import List
from CreateTree import TreeNode

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 层次遍历, 广度优先
        if not root:
            return True

        def issys(l: List) -> bool:
            """判断l是否为对称的"""
            if not l:
                return True
            left = 0    # 左指针
            right = len(l)-1    # 右指针
            while left < right:
                # 由于列表中可能有None, 且对称位置都是None的话结果为相等, 这里要注意判断顺序
                if (not l[left] and l[right]) or (not l[right] and l[left]):
                    break
                elif (not l[left] and not l[right]) or l[left].val == l[right].val:
                    left += 1   # 左指针右移
                    right -= 1  # 右指针左移
                else:
                    break
            return True if left > right else False  # 左指针在右指针右边说明没找到不对称的

        q = [root]
        while q:
            tmp = []
            for node in q:
                left_node = node.left if node.left else None
                right_node = node.right if node.right else None
                # q中node的左右子节点都放进tmp, 无论是不是None
                tmp.append(left_node)
                tmp.append(right_node)
            # 判断tmp是不是对称的
            if issys(tmp) == False:
                return False
            q = [x for x in tmp if x]   # 把q中的None都排除
        return True