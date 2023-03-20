from typing import List
from CreateTree import TreeNode

class Solution:
    @staticmethod
    def inorderTraversal(root: TreeNode) -> List[int]:
        def inorder(root: TreeNode) -> List[int]:
            if root is None:
                return None
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        res = []
        inorder(root)
        return res


if __name__ == '__main__':
    from CreateTree import list_creat_tree
    llist = [0, 1, 2, None, 4, 5, 6, 7, 8, 9, 10]   # 7和8不会出现在结果中, 不严谨, 仅做构造测试数据用
    root = list_creat_tree(None, llist, 0)
    print(Solution.inorderTraversal(root))
