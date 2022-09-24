class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # 双指针
        # 指向两个数字的尾部
        p = len(num1) - 1
        q = len(num2) - 1
        is_plus_one = 0  # 进位标识符
        res = ""

        while p >= 0 or q >= 0:
            i = int(num1[p]) if p >= 0 else 0
            j = int(num2[q]) if q >= 0 else 0
            s = i + j + is_plus_one
            if s >= 10:
                res = str(s - 10) + res
                is_plus_one = 1
            else:
                res = str(s) + res
                is_plus_one = 0
            p -= 1
            q -= 1

        if is_plus_one == 1:
            res = "1" + res

        return res
