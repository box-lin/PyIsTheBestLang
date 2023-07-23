import unittest
from math import inf
from typing import List

from src.fast_io import FastIO

"""
算法：环形线性或者区间DP
功能：计算环形数组上的操作，比较简单的方式是将数组复制成两遍进行区间或者线性DP

题目：

===================================力扣===================================
918. 环形子数组的最大和（https://leetcode.cn/problems/maximum-sum-circular-subarray/）枚举可能的最大与最小区间
1388. 3n 块披萨（https://leetcode.cn/problems/pizza-with-3n-slices/）环形区间DP，类似打家劫舍
213. 打家劫舍 II（https://leetcode.cn/problems/house-robber-ii/）环形数组DP

===================================洛谷===================================
P1880 [NOI1995] 石子合并（https://www.luogu.com.cn/problem/P1880）环形数组区间DP合并求最大值最小值
P1121 环状最大两段子段和（https://www.luogu.com.cn/problem/P1121）环形子数组和的加强版本，只选择两段
P1043 [NOIP2003 普及组] 数字游戏（https://www.luogu.com.cn/problem/P1043）环形区间DP
P1133 教主的花园（https://www.luogu.com.cn/problem/P1133）环形动态规划

参考：OI WiKi（xx）
"""


class Solution:
    def __init__(self):
        return

    @staticmethod
    def lc_918(nums: List[int]) -> int:
        # 模板：环形子数组的最大非空连续子数组和
        s = ceil = floor = pre_ceil = pre_floor = nums[0]
        for num in nums[1:]:
            s += num
            pre_floor = pre_floor if pre_floor < 0 else 0
            pre_floor += num
            floor = floor if floor < pre_floor else pre_floor

            pre_ceil = pre_ceil if pre_ceil > 0 else 0
            pre_ceil += num
            ceil = ceil if ceil > pre_ceil else pre_ceil
        if floor < s:
            return max(ceil, s - floor)
        return ceil

    @staticmethod
    def lg_p1880(ac=FastIO()):

        # 模板：环形数组区间DP
        def check(fun):
            dp = [[0] * n for _ in range(n)]
            for i in range(n - 1, -1, -1):
                dp[i][i] = 0
                if i + 1 < n:
                    dp[i][i + 1] = nums[i] + nums[i + 1]
                for j in range(i + 2, n):
                    dp[i][j] = 0 if fun == max else inf
                    for k in range(i, j):
                        cur = dp[i][k] + dp[k + 1][j] + pre[j + 1] - pre[i]
                        dp[i][j] = fun(dp[i][j], cur)
            return fun([dp[i][i+n//2-1] for i in range(n//2)])

        n = ac.read_int()*2
        nums = ac.read_list_ints()
        nums.extend(nums)
        pre = [0]*(n+1)
        for x in range(n):
            pre[x+1] = pre[x]+nums[x]
        ac.st(check(min))
        ac.st(check(max))
        return

    @staticmethod
    def lg_p1121(ac=FastIO()):
        # 模板：环状最大两段子段和
        n = ac.read_int()
        nums = ac.read_list_ints()
        s = sum(nums)

        # 去除两段最大的
        pre = [-inf] * (n + 1)
        x = 0
        for i in range(n):
            x = x if x > 0 else 0
            x += nums[i]
            pre[i + 1] = ac.max(pre[i], x)

        post = [-inf] * (n + 1)
        x = 0
        for i in range(n - 1, -1, -1):
            x = x if x > 0 else 0
            x += nums[i]
            post[i] = ac.max(post[i + 1], x)
        ans = max(pre[i] + post[i + 1] for i in range(1, n))
        cnt = sum(num >= 0 for num in nums)
        if cnt <= 1:
            ac.st(ans)
            return

        # 扣掉两段最小的
        pre = [0] * (n + 1)
        x = 0
        for i in range(n):
            x = x if x < 0 else 0
            x += nums[i]
            pre[i + 1] = ac.min(pre[i], x)

        post = [0] * (n + 1)
        x = 0
        for i in range(n - 1, -1, -1):
            x = x if x < 0 else 0
            x += nums[i]
            post[i] = ac.min(post[i + 1], x)

        ans = ac.max(ans, s - min(pre[i] + post[i + 1] for i in range(1, n)))
        ac.st(ans)
        return

    @staticmethod
    def lg_p1043(ac=FastIO()):
        # 模板：环形区间DP
        n, m = ac.read_ints()
        nums = [ac.read_int() for _ in range(n)]
        floor = inf
        ceil = -inf
        for _ in range(n):
            nums.append(nums.pop(0))  # 依次枚举隔断点
            pre = [0]*(n+1)
            for i in range(n):
                pre[i+1] = pre[i] + nums[i]
            dp = [[[inf, -inf] for _ in range(m+1)] for _ in range(n+1)]
            # 经典记录乘积的最大值与最小值
            dp[0][0] = [1, 1]
            for i in range(n):
                for k in range(i+1):
                    for j in range(1, m+1):
                        cur = (pre[i+1]-pre[k]) % 10
                        if dp[k][j-1][0] != inf:
                            dp[i+1][j][0] = min(dp[i+1][j][0], dp[k][j-1][0]*cur)
                            dp[i + 1][j][1] = max(dp[i + 1][j][1], dp[k][j - 1][0] * cur)
                        if dp[k][j-1][1] != -inf:
                            dp[i + 1][j][0] = min(dp[i + 1][j][0], dp[k][j - 1][1] * cur)
                            dp[i + 1][j][1] = max(dp[i + 1][j][1], dp[k][j - 1][1] * cur)
            floor = min(floor, dp[-1][-1][0])
            ceil = max(ceil, dp[-1][-1][1])
        ac.st(floor)
        ac.st(ceil)
        return

    @staticmethod
    def lg_p1133(ac=FastIO()):
        # 模板：环形动态规划
        n = ac.read_int()
        nums = [ac.read_list_ints() for _ in range(n)]
        ans = 0

        # 计算下一状态
        state = []
        for a in range(3):
            for b in range(3):
                if a != b:
                    state.append([a, b])
        nex = defaultdict(list)
        for a, b in state:
            for c in range(3):
                if b<a and b < c:
                    nex[(a, b)].append(c)
                if b > a and b> c:
                    nex[(a, b)].append(c)

        # 枚举初始状态进行转移
        for a, b in state:
            pre = dict()
            pre[(a, b)] = nums[-1][a]+nums[0][b]
            for i in range(1, n-1):
                cur = dict()
                for x1, x2 in pre:
                    for y in nex[(x1, x2)]:
                        cur[(x2, y)] = ac.max(cur.get((x2, y), 0), pre[(x1, x2)]+nums[i][y])
                pre = cur.copy()
            for x1, x2 in pre:
                if (a<x2 and a<b) or (a>x2 and a > b):
                    ans = ac.max(ans, pre[(x1, x2)])
        ac.st(ans)
        return


class TestGeneral(unittest.TestCase):

    def test_circle_dp(self):
        pass
        return


if __name__ == '__main__':
    unittest.main()
