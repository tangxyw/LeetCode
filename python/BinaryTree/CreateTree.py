from typing import List


class TreeNode:
    """
    二叉树节点类
    """

    def __init__(self, val: int):
        """
        Args:
            val: int, 节点值
        """
        self.val = val
        self.left = None
        self.right = None


def list_creat_tree(root: TreeNode, llist: List[int], i: int) -> TreeNode:
    """
    按层序遍历顺序生成二叉树
    Args:
        root: 根节点, 在生成过程中恒为None
        llist: 存放TreeNode val的列表
        i: llist的index, 外部调用的时候一般都传0

    Returns:
        根节点对象
    """
    if i < len(llist):  # 下标越界表示不再生成子节点
        if llist[i] is None:
            return None
        else:
            root = TreeNode(llist[i])
            # 往左递推
            root.left = list_creat_tree(root.left, llist, 2 * i + 1)  # 从根开始一直到最左，直至为空，
            # 往右回溯
            root.right = list_creat_tree(root.right, llist, 2 * i + 2)  # 再返回上一个根，回溯右，
            # 再返回根'
            # print(root.val)
            return root
    return root


if __name__ == '__main__':
    llist = [0, 1, 2, None, 4, 5, 6, 7, 8, 9, 10]   # 7和8不会出现在结果中, 不严谨, 仅做构造测试数据用
    root = list_creat_tree(None, llist, 0)
"""
    0 
 /    \
1      2
 \    / \
  4  5   6
 / \
9  10
"""