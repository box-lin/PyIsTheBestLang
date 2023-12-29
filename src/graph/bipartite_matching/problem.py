"""
Algorithm：bipartite_graph|maximum_weight_match|minimum_weight_match|km|ek|unweighted
Description：

====================================LeetCode====================================
4（https://leetcode.cn/problems/broken-board-dominoes/）outline_dp|classical|hungarian
1820（https://leetcode.cn/problems/maximum-number-of-accepted-invitations/）hungarian|bipartite_graph|maximum_weight_match|km

=====================================LuoGu======================================
P3386（https://www.luogu.com.cn/problem/P3386）bipartite_graph|maximum_weight_match|km
P6577（https://www.luogu.com.cn/problem/P6577）bipartite_graph|maximum_weight_match|km
P1894（https://www.luogu.com.cn/problem/P1894）bipartite_graph|maximum_weight_match|km
B3605（https://www.luogu.com.cn/problem/B3605）hungarian|bipartite_graph|maximum_weight_match|km

===================================CodeForces===================================
1437C（https://codeforces.com/problemset/problem/1437/C）bipartite_graph|minimum_weight_match|km

=====================================AcWing=====================================
4298（https://www.acwing.com/problem/content/4301/）hungarian|bipartite_graph

================================LibraryChecker================================
1（https://judge.yosupo.jp/problem/bipartitematching）maximum_weight_match|bipartite_matching

"""

from typing import List

from src.graph.bipartite_matching.template import BipartiteMatching
from src.utils.fast_io import FastIO


class Solution:
    def __init__(self):
        return

    @staticmethod
    def library_check_1(ac=FastIO()):
        """
        url: https://judge.yosupo.jp/problem/bipartitematching
        tag: maximum_weight_match|bipartite_matching
        """
        n, m, k = ac.read_list_ints()
        bm = BipartiteMatching(n, m)
        for _ in range(k):
            a, b = ac.read_list_ints()
            bm.add_edge(a, b)

        matching = bm.solve()
        ac.st(len(matching))
        for a, b in matching:
            ac.lst([a, b])
        return

    @staticmethod
    def lc_1820(grid):
        """
        url: https://leetcode.cn/problems/maximum-number-of-accepted-invitations/
        tag: hungarian|bipartite_graph|maximum_weight_match|bipartite_matching
        """
        m, n = len(grid), len(grid[0])
        bm = BipartiteMatching(m, n)
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    bm.add_edge(i, j)
        matching = bm.solve()
        return len(matching)

    @staticmethod
    def lg_p1894(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1894
        tag: bipartite_graph|maximum_weight_match|km
        """
        n, m = ac.read_list_ints()
        bm = BipartiteMatching(n, m)
        for i in range(n):
            for j in ac.read_list_ints_minus_one()[1:]:
                bm.add_edge(i, j)
        matching = bm.solve()
        ac.st(len(matching))
        return

    @staticmethod
    def lg_3386(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P3386
        tag: bipartite_graph|maximum_weight_match|km
        """
        n, m, e = ac.read_list_ints()
        bm = BipartiteMatching(n, m)
        for i in range(e):
            i, j = ac.read_list_ints_minus_one()
            bm.add_edge(i, j)
        matching = bm.solve()
        ac.st(len(matching))
        return

    @staticmethod
    def ac_4298(ac=FastIO()):
        """
        url: https://www.acwing.com/problem/content/4301/
        tag: hungarian|bipartite_graph
        """
        n = ac.read_int()
        a = ac.read_list_ints()
        m = ac.read_int()
        b = ac.read_list_ints()
        bm = BipartiteMatching(n, m)
        for i in range(n):
            for j in range(m):
                if abs(a[i] - b[j]) <= 1:
                    bm.add_edge(i, j)
        matching = bm.solve()
        ac.st(len(matching))
        return

    @staticmethod
    def lc_4(n: int, m: int, broken: List[List[int]]) -> int:
        """
        url: https://leetcode.cn/problems/broken-board-dominoes/
        tag: outline_dp|classical|hungarian
        """
        m, n = n, m
        grid = [[0] * n for _ in range(m)]
        for i, j in broken:
            grid[i][j] = 1
        bm = BipartiteMatching(m * n, m * n)
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    for x, y in [[i + 1, j], [i, j + 1]]:
                        if 0 <= x < m and 0 <= y < n and not grid[x][y]:
                            bm.add_edge(i * n + j, x * n + y)
                            bm.add_edge(x * n + y, i * n + j)
        matching = bm.solve()
        return len(matching) // 2
