from CreateTree import TreeNode

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # 层次遍历
        q = [root]
        while q:
            tmp = []
            for node in q:
                if node.left and node.right:
                    if node.left.val in (x, y) and node.right.val in (x,y): # x,y为亲兄弟节点
                        return False
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            val_list = [node.val for node in tmp]
            if x in val_list and y in val_list: # x,y为同一层节点的节点值
                return True
            q = tmp
        return False