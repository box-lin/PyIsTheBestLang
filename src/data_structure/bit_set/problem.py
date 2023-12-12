"""
Algorithm：bit_set|implemention|range_state|range_reverse
Description：

====================================LeetCode====================================
2569（https://leetcode.com/problems/handling-sum-queries-after-update/）segment_tree|range_reverse|bit_set

=====================================LuoGu======================================
xx（xxx）xxxxxxxxxxxxxxxxxxxx

===================================CodeForces===================================
xx（xxx）xxxxxxxxxxxxxxxxxxxx

====================================AtCoder=====================================
D - FT Robot（https://atcoder.jp/contests/abc082/tasks/arc087_b）brain_teaser|bfs|bit_set
E - Balanced Path（https://atcoder.jp/contests/abc147/tasks/abc147_e）matrix_dp|bit_set

=====================================AcWing=====================================
5037（https://www.acwing.com/problem/content/5040/）CF242E|range_or_sum|range_xor_sum

"""
from typing import List

from src.data_structure.bit_set.template import SegmentTreeBitSet
from src.utils.fast_io import FastIO


class Solution:
    def __int__(self):
        return

    @staticmethod
    def abc_82d(ac=FastIO()):
        # brain_teaser|，分开bfs平面坐标的x与y轴移动，bitset优化
        s = ac.read_str()
        x, y = ac.read_list_ints()
        ls = [len(t) for t in s.split("T")]
        pre_x = 1 << ls[0] + 8000
        for d in ls[2::2]:
            pre_x = (pre_x >> d) | (pre_x << d)

        pre_y = 1 << 8000
        for d in ls[1::2]:
            pre_y = (pre_y >> d) | (pre_y << d)
        ac.st("Yes" if pre_x & (1 << x + 8000) and pre_y & (1 << y + 8000) else "No")
        return

    @staticmethod
    def lc_2569_2(nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        """
        url: https://leetcode.com/problems/handling-sum-queries-after-update/
        tag: segment_tree|range_reverse|bit_set
        """
        # 01segment_tree|区间翻转与求和，也可以BitSet
        res = []
        seg = SegmentTreeBitSet()
        n = len(nums1)
        for i in range(n):
            if nums1[i]:
                seg.update(i, i)
        s = sum(nums2)
        for a, b, c in queries:
            if a == 1:
                seg.update(b, c)
            elif a == 2:
                s += seg.val.bit_count() * b
            else:
                res.append(s)
        return res

    @staticmethod
    def abc_147f(ac=FastIO()):
        # matrix_dpbitset表示01状态优化
        m, n = ac.read_list_ints()
        grid_a = [ac.read_list_ints() for _ in range(m)]
        grid_b = [ac.read_list_ints() for _ in range(m)]
        pre = [0 for _ in range(n)]
        tmp = abs(grid_a[0][0] - grid_b[0][0])
        offset = 6401
        pre[0] = (1 << (offset - tmp)) | (1 << (offset + tmp))
        for i in range(m):
            cur = [0 for _ in range(n)]
            if not i:
                cur[0] = pre[0]
            for j in range(n):
                tmp = abs(grid_a[i][j] - grid_b[i][j])
                if i:
                    cur[j] |= (pre[j] << tmp) | (pre[j] >> tmp)
                if j:
                    cur[j] |= (cur[j - 1] << tmp) | (cur[j - 1] >> tmp)
            pre = cur[:]

        ans = offset
        val = 1
        x = 0
        while val <= pre[-1]:
            if val & pre[-1]:
                if abs(x - offset) < ans:
                    ans = abs(x - offset)
            val *= 2
            x += 1
        ac.st(ans)
        return

    @staticmethod
    def ac_5037_2(ac=FastIO()):
        # 同CF242E，二十多个01segment_tree|维护区间异或与区间|和
        n = ac.read_int()
        nums = ac.read_list_ints()
        tree = [SegmentTreeBitSet() for _ in range(22)]
        for i in range(n):
            x = nums[i]
            for j in range(22):
                if x & (1 << j):
                    tree[j].update(i, i)

        for _ in range(ac.read_int()):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr = lst[1:]
                ll -= 1
                rr -= 1
                ans = sum((1 << j) * tree[j].query(ll, rr) for j in range(22))
                ac.st(ans)
            else:
                ll, rr, xx = lst[1:]
                ll -= 1
                rr -= 1
                for j in range(22):
                    if (1 << j) & xx:
                        tree[j].update(ll, rr)
        return