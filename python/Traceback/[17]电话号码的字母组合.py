class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        self.map = {'2': ['a', 'b', 'c'],
                    '3': ['d', 'e', 'f'],
                    '4': ['g', 'h', 'i'],
                    '5': ['j', 'k', 'l'],
                    '6': ['m', 'n', 'o'],
                    '7': ['p', 'q', 'r', 's'],
                    '8': ['t', 'u', 'v'],
                    '9': ['w', 'x', 'y', 'z']}

        self.res = []

        def backtrack(nextdigits, track):
            if len(nextdigits) == 0:    # 到了最后一层
                self.res.append(track)
            else:
                # 这里其实就是N叉树的先序遍历, 实际上实现的是一个不定层数的多层循环
                for letter in self.map[nextdigits[0]]:
                    backtrack(nextdigits[1:], track+letter)
                    # 不需要维护全局变量, 无需回溯

        backtrack(digits, '')
        return self.res