from .LinkedList import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 模仿竖式计算, 递归
        def helper(l1: ListNode, l2: ListNode, flag: int) -> ListNode:
            """l1,l2为当前位, flag为进位标识, 1为有进位0为没有进位"""
            if not l1 and not l2 and flag == 0:  # 到最高位了
                return None

            # 计算当前位数字, l1,l2是空就看做0
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            val = l1_val + l2_val + flag

            # 处理下层递归的参数
            l1_next = l1.next if l1 else None
            l2_next = l2.next if l2 else None

            if val < 10:  # 当前位小于10, 不用进位
                cur = ListNode(val)
                cur.next = helper(l1_next, l2_next, 0)  # 当前节点的next节点指向下层递归结果
                return cur  # 返回当前节点给上层递归

            if val >= 10:  # 当前位大约等于10, 要进位
                cur = ListNode(val - 10)
                cur.next = helper(l1_next, l2_next, 1)
                return cur

        head = helper(l1, l2, 0)
        return head
