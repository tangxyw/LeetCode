from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # dfs+回溯+剪枝
        n = len(s)
        res = []
        track = []
        # 所有有效的ip位数字
        valid = [str(x) for x in range(256)]

        def traceback(start, track):
            # 找到有效的ip, 变换成需要的格式
            if start == n and len(track) == 4:
                res.append(".".join(track))
                return

            # 当前空缺的ip位都填三位数, 也填不满s时, 剪枝
            if n - start > (4 - len(track)) * 3:
                return

            # 当前空缺的ip位都填一位数, 剩余的s也不够时, 剪枝
            if n - start < 4 - len(track):
                return

            for digit in [1, 2, 3]:  # 判断当前s前1,2,3位是否是有效ip数字
                if s[start:start + digit] in valid:
                    track.append(s[start:start + digit])
                    traceback(start + digit, track)
                    track.pop()

        traceback(0, track)
        return res
