
class Solution:
    def numTrees(self, n: int) -> int:
        # g(n)表示由n个节点组成的二叉搜索树的数目
        # f(i,n)表示由n个节点组成的二叉搜索树中，以i为根节点的数目
        # 故有g(n) = f(1,n)+f(2,n)+...+f(n,n)
        # 又有f(i,n) = g(i-i)*g(n-i), 即左子树有g(i-1)种, 右子树有g(n-i)种
        # 得到g(n)的递推公式: g(n) = g(0)g(n-1)+g(1)g(n-2)+...+g(n-1)g(0)
        # base case: g(0)=1, g(1)=1
        dp = [0 for x in range(n+1)]
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):    # 从dp[2]开始递推到dp[n]
            for j in range(i):
                dp[i] += dp[j]*dp[i-j-1]    # 每次循环计算出一组g(i-1)*g(n-i)，加到g(n)上去

        return dp[n]