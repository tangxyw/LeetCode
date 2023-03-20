from typing import List
from CreateTree import TreeNode

class Solution:
    @staticmethod
    def postorderTraversal(root: TreeNode) -> List[int]:
        """后序遍历 左右根"""
        def postorder(root: TreeNode) -> List[int]:
            if root is None:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        res = []
        postorder(root)
        return res


if __name__ == '__main__':
    from CreateTree import list_creat_tree
    llist = [0, 1, 2, None, 4, 5, 6, 7, 8, 9, 10]   # 7和8不会出现在结果中, 不严谨, 仅做构造测试数据用
    root = list_creat_tree(None, llist, 0)
    print(Solution.postorderTraversal(root))
    # [9, 10, 4, 1, 5, 6, 2, 0]
    """
        0 
     /    \
    1      2
     \    / \
      4  5   6
     / \
    9  10
    """