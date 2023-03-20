from typing import List
from CreateTree import TreeNode

class Solution:
    @staticmethod
    def preorderTraversal(root: TreeNode) -> List[int]:
        """前序遍历 根左右"""
        def preorder(root: TreeNode) -> List[int]:
            if root is None:
                return None
            else:
                res.append(root.val)
                preorder(root.left)
                preorder(root.right)

        res = []
        preorder(root)
        return res


if __name__ == '__main__':
    from CreateTree import list_creat_tree
    llist = [0, 1, 2, None, 4, 5, 6, 7, 8, 9, 10]   # 7和8不会出现在结果中, 不严谨, 仅做构造测试数据用
    root = list_creat_tree(None, llist, 0)
    print(Solution.preorderTraversal(root))
