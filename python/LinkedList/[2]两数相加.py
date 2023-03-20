from .LinkedList import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def helper(l1: ListNode, l2: ListNode, add_one) -> ListNode:
            """模仿竖式计算, 递归"""
            # 先序遍历
            # base case
            if not l1 and not l2 and not add_one:
                return None
            # 两个加数
            p1 = l1.val if l1 else 0
            p2 = l2.val if l2 else 0
            # 本位上的数字
            sum = (p1 + p2 + add_one) % 10
            # 是否进位
            add_one = (p1 + p2 + add_one) // 10
            # 向后递归
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            # 生成本数字位节点
            cur = ListNode(sum)
            # 本位节点next为向下递归结果
            cur.next = helper(l1, l2, add_one)
            # 返回当前位节点
            return cur

        return helper(l1, l2, 0)
