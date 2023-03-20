class Solution:
    def isHappy(self, n: int) -> bool:
        def getNextNum(n: int) -> int:
            """计算每一位的平方和"""
            sum = 0
            while n > 0:
                x = n % 10  # 每次都取个位数字
                sum += x * x
                n //= 10  # n"右移"一位
            return sum

        # 快慢指针
        slow = n
        fast = n
        while True:
            slow = getNextNum(slow)
            fast = getNextNum(getNextNum(fast))
            if slow == 1 or fast == 1:  # 有一个指针到了1, 则n为快乐数
                return True
            if slow == fast:  # 快慢指针相遇, 说明有环, n不为快乐数
                return False
