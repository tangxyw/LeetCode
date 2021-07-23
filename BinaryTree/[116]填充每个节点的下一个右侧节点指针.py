"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
    # 层序遍历, 完美二叉树每一层的节点数为2^depth
        if not root:
            return None
        q = [root]
        while q:
            tmp = []
            for i in range(len(q)):
                if q[i].left:
                    tmp.append(q[i].left)
                if q[i].right:
                    tmp.append(q[i].right)
                if i == len(q)-1:   # 每层最后一个节点
                    q[i].next = None
                else:               # 其他节点
                    q[i].next = q[i+1]
            q = tmp

        return root