class Solution:
    def isValid(self, s: str) -> bool:
        match = {')': '(',
                 ']': '[',
                 '}': '{'}
        stack = []
        for token in s:
            if token in match:  # token为右括号
                if stack:  # stack非空
                    if match[token] == stack.pop():  # 判断右括号是否能匹配栈顶的左括号, 匹配则弹出栈顶
                        pass
                    else:
                        return False
                else:  # stack为空
                    return False
            else:  # token为右括号
                stack.append(token)

        if stack:
            return False
        else:
            return True
