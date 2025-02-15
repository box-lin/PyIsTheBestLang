"""
Algorithm：segment_tree|bisect_left
Description：range_sum|range_min|range_add|range_change|range_max|dynamic_segment_tree|defaultdict

====================================LeetCode====================================
218（https://leetcode.cn/problems/the-skyline-problem/solution/by-liupengsay-isfo/）segment_tree|RangeChangeRangeMax
2286（https://leetcode.cn/problems/booking-concert-tickets-in-groups/）segment_tree|RangeAddRangeSumMaxMin
2407（https://leetcode.cn/problems/longest-increasing-subsequence-ii/）segment_tree|RangeAddRangeMax|linear_dp
2158（https://leetcode.cn/problems/amount-of-new-area-painted-each-day/）segment_tree|RangeAddRangeSum
2589（https://leetcode.cn/problems/minimum-time-to-complete-all-tasks/）segment_tree|greedy|bisect_left
732（https://leetcode.cn/problems/my-calendar-iii/）dynamic_segment_tree
1851（https://leetcode.cn/problems/minimum-interval-to-include-each-query/）segment_tree|RangeChangeRangeMin|offline_query|monotonic_queue
2213（https://leetcode.cn/problems/longest-substring-of-one-repeating-character/）segment_tree|sub_consequence|range_query|range_merge
2276（https://leetcode.cn/problems/count-integers-in-intervals/）dynamic_segment_tree|union_find_range|SortedList
1340（https://leetcode.cn/problems/jump-game-v/）segment_tree|linear_dp
2940（https://leetcode.cn/problems/find-building-where-alice-and-bob-can-meet/）segment_tree|bisect_left
2569（https://leetcode.cn/problems/handling-sum-queries-after-update/）segment_tree|range_reverse|bit_set
3003（https://leetcode.cn/problems/maximize-the-number-of-partitions-after-operations）segment_tree|bisect_left|range_or|point_set
1622（https://leetcode.cn/problems/fancy-sequence/）segment_tree|range_affine|range_sum

=====================================LuoGu======================================
P2846（https://www.luogu.com.cn/problem/P2846）segment_tree|range_reverse|range_sum
P2572（https://www.luogu.com.cn/problem/P2572）segment_tree|range_reverse|range_sum
P2574（https://www.luogu.com.cn/problem/P2574）segment_tree|range_change|range_sum|range_cover
P3130（https://www.luogu.com.cn/problem/P3130）RangeAddRangeSumMaxMin
P3870（https://www.luogu.com.cn/problem/P3870）segment_tree|range_reverse|range_sum
P5057（https://www.luogu.com.cn/problem/P5057）segment_tree|range_reverse|range_sum
P3372（https://www.luogu.com.cn/problem/P3372）RangeAddRangeSumMaxMin
P2880（https://www.luogu.com.cn/problem/P2880）RangeAddRangeSumMaxMin
P1904（https://www.luogu.com.cn/problem/P1904）segment_tree|RangeAscendRangeMax
P1438（https://www.luogu.com.cn/problem/P1438）diff_array|RangeAddRangeSumMaxMin|segment_tree
P1253（https://www.luogu.com.cn/problem/P1253）range_add|range_change|segment_tree|range_sum
P3373（https://www.luogu.com.cn/problem/P3373）range_add|range_mul|segment_tree|range_sum|RangeAffineRangeSum
P4513（https://www.luogu.com.cn/problem/P4513）segment_tree|range_change|range_merge|sub_consequence
P1471（https://www.luogu.com.cn/problem/P1471）math|segment_tree|RangeAddRangeSum
P6492（https://www.luogu.com.cn/problem/P6492）segment_tree|range_change|range_merge|sub_consequence
P4145（https://www.luogu.com.cn/problem/P4145）math|segment_tree|RangeAddRangeSum
P1558（https://www.luogu.com.cn/problem/P1558）segment_tree|RangeSetRangeOr
P3740（https://www.luogu.com.cn/problem/P3740）discretization|segment_tree|RangeChangeRangeSum
P4588（https://www.luogu.com.cn/problem/P4588）segment_tree|RangeChangeRangeMul
P6627（https://www.luogu.com.cn/problem/P6627）segment_tree|range_xor
P8081（https://www.luogu.com.cn/problem/P8081）diff_array|counter|action_scop|segment_tree|RangeSetRangeOr
P8812（https://www.luogu.com.cn/problem/P8812）segment_tree|RangeDescendRangeMin
P8856（https://www.luogu.com.cn/problem/solution/P8856）segment_tree|RangeAddRangeSumMaxMin
P1972（https://www.luogu.com.cn/problem/P1972）point_add|range_sum|tree_array|offline_query
P5848（https://www.luogu.com.cn/problem/P5848）segment_tree|range_set|range_pre_max_sum|dynamic

===================================CodeForces===================================
482B（https://codeforces.com/problemset/problem/482/B）segment_tree|RangeOrRangeAnd
380C（https://codeforces.com/problemset/problem/380/C）segment_tree|range_merge|sub_consequence|bracket
52C（https://codeforces.com/problemset/problem/52/C）segment_tree|circular_array|range_add|range_min
438D（https://codeforces.com/problemset/problem/438/D）segment_tree|range_sum|mod|RangeChangeRangeSumMaxMin
558E（https://codeforces.com/contest/558/problem/E）alphabet|segment_tree|sorting
343D（https://codeforces.com/problemset/problem/343/D）dfs_order|segment_tree
242E（https://codeforces.com/problemset/problem/242/E）segment_tree|RangeReverseRangeBitCount
987C（https://codeforces.com/problemset/problem/987/C）brute_force|segment_tree|prefix_suffix
1216F（https://codeforces.com/contest/1216/problem/F）segment_tree|linear_dp|monotonic_queue
1665E（https://codeforces.com/contest/1665/problem/E）segment_tree
1478E（https://codeforces.com/contest/1478/problem/E）RangeSetRangeSumMinMax|backward_thinking|implemention
1679E（https://codeforces.com/contest/1679/problem/B）RangeSetRangeSumMinMax|range_change|range_sum
85D（https://codeforces.com/contest/85/problem/D）segment_tree|point_add|range_sum
474E（https://codeforces.com/contest/474/problem/E）segment_tree|point_set|range_max_index|linear_dp|classical
920F（https://codeforces.com/problemset/problem/920/F）union_find|all_factor_cnt|range_sum|point_add
438D（https://codeforces.com/contest/438/problem/D）segment_tree|point_set|range_mod|range_sum|classical
1187D（https://codeforces.com/problemset/problem/1187/D）segment_tree|point_set|range_min|classical
914D（https://codeforces.com/contest/914/problem/D）segment_tree|point_set|range_gcd
1567E（https://codeforces.com/problemset/problem/1567/E）segment_tree|point_set|range_ascend_sub_cnt
522D（https://codeforces.com/problemset/problem/522/D）segment_tree|point_set|range_min|offline_query
703D（https://codeforces.com/problemset/problem/703/D）segment_tree|point_add|range_xor|offline_query
1208D（https://codeforces.com/problemset/problem/1208/D）segment_tree|reverse_thinking|construction|point_set|range_sum_bisect_left
558E（https://codeforces.com/problemset/problem/558/E）segment_tree|range_set|range_sum|alphabet
1157D（https://codeforces.com/contest/1557/problem/D）segment_tree|range_ascend|range_max_index|dp
1114F（https://codeforces.com/problemset/problem/1114/F）segment_tree|range_set|range_sum|range_mul
292E（https://codeforces.com/problemset/problem/292/E）segment_tree|range_set|point_get
1881G（https://codeforces.com/contest/1881/problem/G）segment_tree|range_add|range_palindrome
915E（https://codeforces.com/problemset/problem/915/E）segment_tree|range_set|range_sum|dynamic
877E（https://codeforces.com/problemset/problem/877/E）segment_tree|range_reverse|dfs_order|range_bit_count
1108E2（https://codeforces.com/contest/1108/problem/E2）segment_tree|range_add|range_min|prefix_suffix|bryte_force|brain_teaser
1234D（https://codeforces.com/contest/1234/problem/D）segment_tree|point_set|range_or

====================================AtCoder=====================================
ABC332F（https://atcoder.jp/contests/abc332/tasks/abc332_f）RangeAffineRangeSum
ABC287G（https://atcoder.jp/contests/abc287/tasks/abc287_g）segment_tree|range_sum|dynamic|offline
ABC327F（https://atcoder.jp/contests/abc327/tasks/abc327_f）segment_tree|range_add|range_max
ABC285F（https://atcoder.jp/contests/abc285/tasks/abc285_f）segment_tree|point_add|range_sum|range_ascend_sub_cnt|point_set
ABC339E（https://atcoder.jp/contests/abc339/tasks/abc339_e）segment_tree|linear_dp

=====================================AcWing=====================================
3805（https://www.acwing.com/problem/content/3808/）RangeAddRangeMin

=====================================LibraryChecker=====================================
1（https://judge.yosupo.jp/problem/range_affine_point_get）RangeAffineRangeSum
2（https://judge.yosupo.jp/problem/range_affine_range_sum）RangeAffineRangeSum
3（https://judge.yosupo.jp/problem/point_set_range_composite）PointSetRangeComposite
4（https://codeforces.com/edu/course/2/lesson/4/1/practice/contest/273169/problem/A）PointSetRangeSum
5（https://codeforces.com/edu/course/2/lesson/4/1/practice/contest/273169/problem/B）segment_tree|point_set|range_min
6（https://codeforces.com/edu/course/2/lesson/4/1/practice/contest/273169/problem/C）segment_tree|point_set|range_min_count
7（https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/A）segment_tree|point_set|range_max_sub_sum
8（https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/B）segment_tree|point_set|range_sum_bisect_left
9（https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/C）segment_tree|point_set|range_max_bisect_left
10（https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/D）segment_tree|point_set|range_max_bisect_left_with_ind
11（https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/A）segment_tree|point_set|range_sum|inversion
12（https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/B）segment_tree|point_set|range_sum|inversion|bisect_left
13（https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/C）segment_tree|point_set|range_sum|range_include
14（https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/D）segment_tree|point_set|range_sum|range_include|reverse_thinking|include_exclude
15（https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/E）segment_tree|range_add|point_get
16（https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/problem/A）segment_tree|point_set|range_sum
17（https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/problem/B）segment_tree|matrix_build|range_mul
18（https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/problem/C）segment_tree|point_set|range_inverse
19（https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/problem/D）segment_tree|point_set|range_or
20（https://codeforces.com/edu/course/2/lesson/5/1/practice/contest/279634/problem/A）segment_tree|range_add|point_get
21（https://codeforces.com/edu/course/2/lesson/5/1/practice/contest/279634/problem/A）segment_tree|range_ascend|point_get
22（https://codeforces.com/edu/course/2/lesson/5/1/practice/contest/279634/problem/A）segment_tree|range_set|point_get
23（https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/problem/E）segment_tree|bisect_left|brute_force|classical|range_min|point_set
24（https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/A）segment_tree|range_add|range_min
25（https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/B）segment_tree|range_affine|range_sum
26（https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/C）segment_tree|range_or|range_and
27（https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/D）segment_tree|range_add|range_sum
28（https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/E）segment_tree|range_set|range_min
29（https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/F）segment_tree|range_set|range_sum
30（https://codeforces.com/edu/course/2/lesson/5/3/practice/contest/280799/problem/A）segment_tree|range_set|range_max_non_emp_con_sub_sum
31（https://codeforces.com/edu/course/2/lesson/5/3/practice/contest/280799/problem/B）segment_tree|range_reverse|range_bit_count_bisect_left
32（https://codeforces.com/edu/course/2/lesson/5/3/practice/contest/280799/problem/C）segment_tree|range_add|range_max|bisect_left
33（https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/A）segment_tree|range_change_add|range_sum
34（https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/B）segment_tree|diff_array|range_add|point_get|range_sum
35（https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/C）segment_tree|range_set|range_seg_count_length
36（https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/D）segment_tree|range_add|range_weighted_sum
37（https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/E）segment_tree|range_chmin_chmax|point_get
38（https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/F）segment_tree_dynamic|range_set|range_sum_bisect_left


"""
import bisect
from collections import defaultdict, Counter, deque
from functools import lru_cache
from typing import List

from src.data_structure.segment_tree.template import RangeAscendRangeMax, RangeDescendRangeMin, \
    RangeAddRangeSumMinMax, RangeRevereRangeBitCount, RangeSetRangeOr, \
    RangeAddRangeAvgDev, \
    RangeSetRangeSumMinMaxDynamic, PointSetRangeLongestSubSame, \
    RangeOrRangeAnd, RangeSetRangeSumMinMax, RangeKthSmallest, RangeSetRangeMaxNonEmpConSubSum, \
    RangeAffineRangeSum, PointSetRangeComposite, RangeLongestRegularBrackets, \
    RangeXorUpdateRangeXorQuery, PointSetRangeLongestAlter, \
    RangeSqrtRangeSum, RangeSetReverseRangeSumLongestConSub, PointSetRangeOr, PointSetRangeSum, PointSetRangeMin, \
    PointSetRangeMinCount, PointSetRangeMaxSubSum, PointSetRangeMax, RangeAddPointGet, MatrixBuildRangeMul, \
    PointSetRangeInversion, RangeSetPointGet, RangeAscendPointGet, RangeSetAddRangeSumMinMax, \
    RangeSetRangeSegCountLength, RangeAddRangeWeightedSum, RangeChminChmaxPointGet, RangeSetPreSumMaxDynamicDct, \
    PointAddRangeSum1Sum2, PointAddRangeSumMod5, PointSetRangeMaxIndex, RangeModPointSetRangeSum, PointSetRangeGcd, \
    PointSetRangeAscendSubCnt, PointSetRangeNotExistABC, RangeAscendRangeMaxIndex, RangeMulRangeMul, \
    RangeAddRangePalindrome, RangeSetRangeSumMinMaxDynamicDct, RangeSetPreSumMaxDynamic
from src.data_structure.sorted_list.template import SortedList
from src.data_structure.tree_array.template import PointAddRangeSum
from src.graph.union_find.template import UnionFind
from src.mathmatics.number_theory.template import PrimeSieve
from src.mathmatics.prime_factor.template import AllFactorCnt, PrimeFactor
from src.search.dfs.template import DFS
from src.utils.fast_io import FastIO
from src.utils.fast_io import inf


class Solution:
    def __int__(self):
        return

    @staticmethod
    def lc_2213(s: str, word: str, indices: List[int]) -> List[int]:
        """
        url: https://leetcode.cn/problems/longest-substring-of-one-repeating-character/
        tag: segment_tree|sub_consequence|range_query|range_merge
        """
        n = len(s)
        tree = PointSetRangeLongestSubSame(n, [ord(w) - ord("a") for w in s])
        ans = []
        for i, w in zip(indices, word):
            ans.append(tree.point_set_rang_longest_sub_same(i, ord(w) - ord("a")))
        return ans

    @staticmethod
    def library_1(ac=FastIO()):
        """
        url: https://judge.yosupo.jp/problem/range_affine_point_get
        tag: RangeAffineRangeSum
        """
        n, q = ac.read_list_ints()
        nums = ac.read_list_ints()
        mod = 998244353
        tree = RangeAffineRangeSum(n, mod)
        tree.build(nums)
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 0:
                ll, rr, b, c = lst[1:]
                tree.range_affine(ll, rr - 1, (b << 32) | c)
            else:
                i = lst[1]
                ac.st(tree.range_sum(i, i))
        return

    @staticmethod
    def library_check_2(ac=FastIO()):
        """
        url: https://judge.yosupo.jp/problem/range_affine_range_sum
        tag: RangeAffineRangeSum
        """
        n, q = ac.read_list_ints()
        nums = ac.read_list_ints()
        mod = 998244353
        tree = RangeAffineRangeSum(n, mod)
        tree.build(nums)
        ans = []
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 0:
                ll, rr, b, c = lst[1:]
                tree.range_affine(ll, rr - 1, (b << 32) | c)
            else:
                ll, rr = lst[1:]
                ans.append(str(tree.range_sum(ll, rr - 1)))
        print("\n".join(ans))
        return

    @staticmethod
    def library_3(ac=FastIO()):
        n, q = ac.read_list_ints()
        nums = [ac.read_list_ints() for _ in range(n)]
        m = 32
        mod = 998244353
        tree = PointSetRangeComposite(n, mod, m)
        tree.build([(c << m) | d for c, d in nums])
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 0:
                p, c, d = lst[1:]
                tree.point_set(p, p, (c << m) | d)
            else:
                ll, rr, x = lst[1:]
                val = tree.range_composite(ll, rr - 1)
                mul, add = val >> m, val & tree.mask
                ac.st((mul * x + add) % mod)
        return

    @staticmethod
    def lc_2569(nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        """
        url: https://leetcode.cn/problems/handling-sum-queries-after-update/
        tag: segment_tree|range_reverse|bit_set
        """
        n = len(nums1)
        tree = RangeRevereRangeBitCount(n)
        tree.build(nums1)
        ans = []
        s = sum(nums2)
        for op, x, y in queries:
            if op == 1:
                tree.range_reverse(x, y)
            elif op == 2:
                s += tree.range_bit_count(0, n - 1) * x
            else:
                ans.append(s)
        return ans

    @staticmethod
    def lg_p1904(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1904
        tag: segment_tree|RangeAscendRangeMax
        """
        high = 10 ** 4
        segment = RangeAscendRangeMax(high)
        segment.build([0] * high)
        nums = set()
        while True:
            s = ac.read_str()
            if not s:
                break
            x, h, y = [int(w) for w in s.split() if w]
            nums.add(x)
            nums.add(y)
            segment.range_ascend(x, y - 1, h)
        nums = sorted(list(nums))
        n = len(nums)
        height = [segment.range_max(num, num) for num in nums]
        ans = []
        pre = -1
        for i in range(n):
            if height[i] != pre:
                ans.extend([nums[i], height[i]])
                pre = height[i]
        ac.lst(ans)
        return

    @staticmethod
    def cf_242e(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/242/E
        tag: segment_tree|RangeReverseRangeBitCount
        """
        n = ac.read_int()
        nums = ac.read_list_ints()
        tree = [RangeRevereRangeBitCount(n) for _ in range(22)]
        for j in range(22):
            lst = [1 if nums[i] & (1 << j) else 0 for i in range(n)]
            tree[j].build(lst)
        for _ in range(ac.read_int()):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr = lst[1:]
                ll -= 1
                rr -= 1
                ans = sum((1 << j) * tree[j].range_bit_count(ll, rr) for j in range(22))
                ac.st(ans)
            else:
                ll, rr, xx = lst[1:]
                ll -= 1
                rr -= 1
                for j in range(22):
                    if (1 << j) & xx:
                        tree[j].range_reverse(ll, rr)
        return

    @staticmethod
    def cf_1216f(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1216/problem/F
        tag: segment_tree|dp|monotonic_queue
        """
        n, k = ac.read_list_ints()
        s = ac.read_str()
        tree = RangeDescendRangeMin(n)
        for i in range(n):
            if s[i] == "1":
                left = ac.max(0, i - k)
                right = ac.min(n - 1, i + k)
                pre = tree.range_min(left - 1, i - 1) if left else 0
                cur = pre + i + 1
                tree.range_descend(i, right, cur)
            else:
                pre = tree.range_min(i - 1, i - 1) if i else 0
                cur = pre + i + 1
                tree.range_descend(i, i, cur)
        ac.st(tree.range_min(n - 1, n - 1))
        return

    @staticmethod
    def cf_1478e(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1478/problem/E
        tag: RangeSetRangeSumMinMax|backward_thinking|implemention
        """
        for _ in range(ac.read_int()):
            def check():
                n, q = ac.read_list_ints()
                s = [int(w) for w in ac.read_str()]
                t = [int(w) for w in ac.read_str()]
                queries = [ac.read_list_ints_minus_one() for _ in range(q)]
                queries.reverse()
                tree = RangeSetRangeSumMinMax(n)
                tree.build(t)
                for ll, rr in queries:
                    cur_sum = tree.range_sum(ll, rr)
                    if cur_sum < rr - ll + 1 - cur_sum:
                        tree.range_set(ll, rr, 0)
                    elif cur_sum > rr - ll + 1 - cur_sum:
                        tree.range_set(ll, rr, 1)
                    else:
                        ac.st("NO")
                        return
                if tree.get() == s:
                    ac.st("YES")
                else:
                    ac.st("NO")
                return

            check()
        return

    @staticmethod
    def cf_1665e(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1665/problem/E
        tag: segment_tree|classical
        """
        for _ in range(ac.read_int()):
            n = ac.read_int()
            nums = ac.read_list_ints()
            tree = RangeKthSmallest(n, 31)
            tree.build(nums)
            for _ in range(ac.read_int()):
                ll, rr = ac.read_list_ints_minus_one()
                lst = tree.range_kth_smallest(ll, rr)
                ans = inf
                m = len(lst)
                for i in range(m):
                    x = lst[i]
                    if x > ans:
                        break
                    for j in range(i + 1, m):
                        y = lst[j]
                        if x > ans:
                            break
                        ans = ac.min(ans, x | y)
                ac.st(ans)
        return

    @staticmethod
    def lc_218(buildings: List[List[int]]) -> List[List[int]]:
        """
        url: https://leetcode.cn/problems/the-skyline-problem/
        tag: segment_tree|RangeChangeRangeMax
        """
        pos = set()
        for left, right, _ in buildings:
            pos.add(left)
            pos.add(right)
        lst = sorted(list(pos))
        n = len(lst)
        dct = {x: i for i, x in enumerate(lst)}

        segment = RangeAscendRangeMax(n)
        segment.build([0] * n)
        for left, right, height in buildings:
            segment.range_ascend(dct[left], dct[right] - 1, height)

        pre = -1
        ans = []
        for pos in lst:
            h = segment.range_max(dct[pos], dct[pos])
            if h != pre:
                ans.append([pos, h])
                pre = h
        return ans

    @staticmethod
    def cf_380c(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/380/C
        tag: segment_tree|range_merge|sub_consequence|bracket
        """
        s = ac.read_str()
        n = len(s)
        tree = RangeLongestRegularBrackets(n)
        tree.build(s)
        for _ in range(ac.read_int()):
            x, y = ac.read_list_ints_minus_one()
            ac.st(tree.range_longest_regular_brackets(x, y))
        return

    @staticmethod
    def lg_p3372(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P3372
        tag: RangeAddRangeSumMaxMin
        """
        n, m = ac.read_list_ints()
        segment = RangeAddRangeSumMinMax(n)
        segment.build(ac.read_list_ints())

        for _ in range(m):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                x, y, k = lst[1:]
                segment.range_add(x - 1, y - 1, k)
            else:
                x, y = lst[1:]
                ac.st(segment.range_sum(x - 1, y - 1))
        return

    @staticmethod
    def lg_p3870(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P3870
        tag: segment_tree|range_reverse|range_sum
        """
        n, m = ac.read_list_ints()
        segment = RangeRevereRangeBitCount(n)

        for _ in range(m):
            lst = ac.read_list_ints()
            if lst[0] == 0:
                x, y = lst[1:]
                segment.range_reverse(x - 1, y - 1)
            else:
                x, y = lst[1:]
                ac.st(segment.range_bit_count(x - 1, y - 1))
        return

    @staticmethod
    def lg_p1438(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1438
        tag: diff_array|RangeAddRangeSumMaxMin|segment_tree
        """
        n, m = ac.read_list_ints()
        nums = ac.read_list_ints()
        segment = RangeAddRangeSumMinMax(n)

        for _ in range(m):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                x, y, k, d = lst[1:]
                if x == y:
                    segment.range_add(x - 1, x - 1, k)
                    if y <= n - 1:
                        segment.range_add(y, y, -k)
                else:
                    segment.range_add(x - 1, x - 1, k)
                    segment.range_add(x, y - 1, d)
                    cnt = y - x
                    if y <= n - 1:
                        segment.range_add(y, y, -cnt * d - k)
            else:
                x = lst[1]
                ac.st(segment.range_sum(0, x - 1) + nums[x - 1])
        return

    @staticmethod
    def lg_p1253(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1253
        tag: range_add|range_change|segment_tree|range_sum
        """
        n, m = ac.read_list_ints()
        nums = ac.read_list_ints()
        tree = RangeSetAddRangeSumMinMax(n, 1 << 32)
        tree.build(nums)
        for _ in range(m):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                x, y, k = lst[1:]
                tree.range_set_add(x - 1, y - 1, (k, 0))
                for i in range(x - 1, y):
                    nums[i] = k
            elif lst[0] == 2:
                x, y, k = lst[1:]
                tree.range_set_add(x - 1, y - 1, (-tree.inf, k))
                for i in range(x - 1, y):
                    nums[i] += k
            else:
                x, y = lst[1:]
                ac.st(tree.range_max(x - 1, y - 1))
        return

    @staticmethod
    def lg_p3373(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P3373
        tag: range_add|range_mul|segment_tree|range_sum|RangeAffineRangeSum
        """
        n, q, mod = ac.read_list_ints()
        tree = RangeAffineRangeSum(n, mod)
        nums = ac.read_list_ints()
        tree.build(nums)
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                x, y, k = lst[1:]
                tree.range_affine(x - 1, y - 1, k << 32)
            elif lst[0] == 2:
                x, y, k = lst[1:]
                tree.range_affine(x - 1, y - 1, (1 << 32) | k)
            else:
                x, y = lst[1:]
                ans = tree.range_sum(x - 1, y - 1)
                ac.st(ans)
        return

    @staticmethod
    def lg_p4513(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P4513
        tag: segment_tree|range_change|range_merge|sub_consequence
        """
        n, m = ac.read_list_ints()
        segment = RangeSetRangeMaxNonEmpConSubSum(n, 1000)
        segment.build([ac.read_int() for _ in range(n)])
        for _ in range(m):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                a, b = lst[1:]
                a, b = ac.min(a, b), ac.max(a, b)
                ans = segment.range_max_non_emp_con_sub_sum(a - 1, b - 1)
                ac.st(ans)
            else:
                a, s = lst[1:]
                segment.point_set(a - 1, s)
        return

    @staticmethod
    def lg_p1471(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1471
        tag: math|segment_tree|RangeAddRangeSum
        """
        n, m = ac.read_list_ints()
        tree = RangeAddRangeAvgDev(n)
        tree.build(ac.read_list_floats())
        for _ in range(m):
            lst = ac.read_list_floats()
            if lst[0] == 1:
                x, y, k = lst[1:]
                x = int(x)
                y = int(y)
                tree.range_add(x - 1, y - 1, k)
            elif lst[0] == 2:
                x, y = lst[1:]
                x = int(x)
                y = int(y)
                ans = tree.range_avg_dev(x - 1, y - 1)[0]
                ac.st("%.4f" % ans)
            else:
                x, y = lst[1:]
                x = int(x)
                y = int(y)
                ans = tree.range_avg_dev(x - 1, y - 1)[1]
                ac.st("%.4f" % ans)
        return

    @staticmethod
    def lg_p6627(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P6627
        tag: segment_tree|range_xor|discretization
        """
        n = ac.read_int()
        nums = [ac.read_list_ints() for _ in range(n)]
        nodes = {0, -10 ** 9 - 1, 10 ** 9 + 1}
        for lst in nums:
            for va in lst[1:-1]:
                nodes.add(va)
                nodes.add(va - 1)
                nodes.add(va + 1)
        nodes = sorted(list(nodes))
        n = len(nodes)
        ind = {num: i for i, num in enumerate(nodes)}
        tree = RangeXorUpdateRangeXorQuery(n)
        arr = [0] * n
        for lst in nums:
            if lst[0] == 1:
                a, b, w = lst[1:]
                if a > b:
                    a, b = b, a
                tree.range_xor_update(ind[a], ind[b], w)
            elif lst[0] == 2:
                a, w = lst[1:]
                arr[ind[a]] ^= w
            else:
                a, w = lst[1:]
                tree.range_xor_update(0, n - 1, w)
                arr[ind[a]] ^= w
        ans = inf
        res = -inf
        nums = tree.get()
        for i in range(n):
            val = arr[i] ^ nums[i]
            if val > res or (
                    val == res and (abs(ans) > abs(nodes[i]) or (abs(ans) == abs(nodes[i]) and nodes[i] > ans))):
                res = val
                ans = nodes[i]
        ac.lst([res, ans])
        return

    @staticmethod
    def lg_p6492(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P6492
        tag: segment_tree|range_change|range_merge|sub_consequence
        """
        n, q = ac.read_list_ints()
        tree = PointSetRangeLongestAlter(n)
        for _ in range(q):
            i = ac.read_int() - 1
            ac.st(tree.point_set_range_longest_alter(i, i))
        return

    @staticmethod
    def lg_p4145(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P4145
        tag: math|segment_tree|RangeAddRangeSum
        """
        n = ac.read_int()
        tree = RangeSqrtRangeSum(n)
        tree.build(ac.read_list_ints())
        for _ in range(ac.read_int()):
            lst = ac.read_list_ints()
            a, b = [int(w) - 1 for w in lst[1:]]
            if a > b:
                a, b = b, a
            if lst[0] == 0:
                tree.range_sqrt(a, b)
            else:
                ac.st(tree.range_sum(a, b))
        return

    @staticmethod
    def lc_2940(heights: List[int], queries: List[List[int]]) -> List[int]:
        """
        url: https://leetcode.cn/problems/find-building-where-alice-and-bob-can-meet/
        tag: segment_tree_binary_search|static_range
        """
        n = len(heights)
        tree = RangeAscendRangeMax(n)
        tree.build(heights)
        ans = []
        for ll, rr in queries:
            if ll > rr:
                ll, rr = rr, ll
            if heights[ll] < heights[rr]:
                ans.append(rr)
                continue
            if ll == rr:
                ans.append(ll)
                continue
            if rr == n - 1:
                ans.append(-1)
                continue
            h = heights[ll] if heights[ll] > heights[rr] else heights[rr]
            left = tree.range_max_bisect_left(rr + 1, n - 1, h + 1)
            ans.append(left)
        return ans

    @staticmethod
    def lg_p2574(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2574
        tag: segment_tree|range_reverse|range_sum
        """
        n, m = ac.read_list_ints()
        tree = RangeRevereRangeBitCount(n)
        tree.build([int(w) for w in ac.read_str()])

        for _ in range(m):
            op, left, right = ac.read_list_ints()
            if not op:
                tree.range_reverse(left - 1, right - 1)
            else:
                ac.st(tree.range_bit_count(left - 1, right - 1))
        return

    @staticmethod
    def lg_2572(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2572
        tag: segment_tree|range_reverse|range_sum
        """
        n, m = ac.read_list_ints()
        tree = RangeSetReverseRangeSumLongestConSub(n)
        tree.build(ac.read_list_ints())
        ans = []
        for _ in range(m):
            lst = ac.read_list_ints()
            left, right = lst[1:]
            if left > right:
                left, right = right, left
            if lst[0] <= 2:
                tree.range_change_reverse(left, right, lst[0])
            elif lst[0] == 3:
                ans.append(str(tree.range_sum(left, right)))
            else:
                ans.append(str(tree.range_longest_con_sub(left, right)))
        ac.st("\n".join(ans))
        return

    @staticmethod
    def lg_p1558(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1558
        tag: segment_tree|RangeSetRangeOr
        """
        n, t, q = ac.read_list_ints()
        tree = RangeSetRangeOr(n)
        tree.range_set(0, n - 1, 1)
        for _ in range(q):
            lst = ac.read_list_strs()
            if lst[0] == "C":
                a, b, c = [int(w) for w in lst[1:]]
                if a > b:
                    a, b = b, a
                tree.range_set(a - 1, b - 1, 1 << (c - 1))
            else:
                a, b = [int(w) for w in lst[1:]]
                if a > b:
                    a, b = b, a
                ac.st(bin(tree.range_or(a - 1, b - 1)).count("1"))
        return

    @staticmethod
    def lg_p3740(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P3740
        tag: discretization|segment_tree|RangeChangeRangeSum
        """
        n, m = ac.read_list_ints()
        nums = []
        while len(nums) < m * 2:
            nums.extend(ac.read_list_ints())
        nums = [nums[2 * i:2 * i + 2] for i in range(m)]
        nodes = set()
        nodes.add(1)
        nodes.add(n)
        for a, b in nums:
            nodes.add(a)
            nodes.add(b)
            nodes.add(b + 1)
        nodes = list(sorted(nodes))
        ind = {num: i for i, num in enumerate(nodes)}

        n = len(nodes)
        tree = RangeSetRangeSumMinMax(n)
        tree.build([0] * n)
        for i in range(m):
            a, b = nums[i]
            tree.range_set(ind[a], ind[b], i + 1)

        ans = tree.get()
        ac.st(len(set(c for c in ans if c)))
        return

    @staticmethod
    def lg_p4588(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P4588
        tag: segment_tree|PointSetRangeComposite
        """
        for _ in range(ac.read_int()):
            n, mod = ac.read_list_ints()
            m = 32
            tree = PointSetRangeComposite(n, mod, m)
            tree.build([1 << m for _ in range(n)])
            for i in range(n):
                op, x = ac.read_list_ints()
                if op == 1:
                    tree.point_set(i, i, x << m)
                else:
                    tree.point_set(x - 1, x - 1, 1 << m)
                val = tree.range_composite(0, n - 1)
                ac.st((val >> m) % mod)
        return

    @staticmethod
    def lg_p8081(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P8081
        tag: diff_array|counter|action_scop|segment_tree|RangeSetRangeOr
        """
        n = ac.read_int()
        nums = ac.read_list_ints()
        tree = RangeSetRangeSumMinMax(n)
        pre = 0
        ceil = 0
        for i in range(n):
            if nums[i] < 0:
                pre += 1
            else:
                if pre:
                    ceil = max(ceil, pre)
                    low, high = i - 3 * pre, i - pre - 1
                    if high >= 0:
                        tree.range_set(ac.max(0, low), high, 1)
                pre = 0
        if pre:
            ceil = max(ceil, pre)
            low, high = n - 3 * pre, n - pre - 1
            if high >= 0:
                tree.range_set(ac.max(0, low), high, 1)

        ans = tree.range_sum(0, n - 1)
        pre = 0
        res = 0
        for i in range(n):
            if nums[i] < 0:
                pre += 1
            else:
                if pre == ceil:
                    low, high = i - 4 * pre, i - 3 * pre - 1
                    low = ac.max(low, 0)
                    if low <= high:
                        res = ac.max(res, high - low + 1 - tree.range_sum(low, high))
                pre = 0
        if pre == ceil:
            low, high = n - 4 * pre, n - 3 * pre - 1
            low = ac.max(low, 0)
            if low <= high:
                res = ac.max(res, high - low + 1 - tree.range_sum(low, high))
        ac.st(ans + res)
        return

    @staticmethod
    def lg_p8812(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P8812
        tag: segment_tree|RangeDescendRangeMin|discretization
        """
        n, m = ac.read_list_ints()
        goods = [[] for _ in range(n)]
        for _ in range(m):
            s, t, p, c = ac.read_list_ints()
            for _ in range(c):
                a, b = ac.read_list_ints()
                a -= 1
                goods[a].append([1, 10 ** 9 + 1, b])
                b = b * p // 100
                goods[a].append([s, t, b])

        for i in range(n):
            nodes = {0, 10 ** 9 + 1}
            for s, t, _ in goods[i]:
                nodes.add(s - 1)
                nodes.add(s)
                nodes.add(t)
                nodes.add(t + 1)
            nodes = sorted(list(nodes))
            ind = {node: i for i, node in enumerate(nodes)}
            k = len(ind)
            tree = RangeDescendRangeMin(k)
            for s, t, b in goods[i]:
                tree.range_descend(ind[s], ind[t], b)
            res = []
            for x in range(k):
                val = tree.range_min(x, x)
                if val == inf:
                    continue
                if not res or res[-1][2] != val:
                    res.append([nodes[x], nodes[x], val])
                else:
                    res[-1][1] = nodes[x]

            goods[i] = [r[:] for r in res]

        nodes = {0, 10 ** 9 + 1}
        for i in range(n):
            for s, t, _ in goods[i]:
                nodes.add(s)
                nodes.add(t)
        nodes = sorted(list(nodes))
        ind = {node: i for i, node in enumerate(nodes)}
        k = len(ind)
        diff = [0] * k
        for i in range(n):
            for s, t, b in goods[i]:
                diff[ind[s]] += b
                if ind[t] + 1 < k:
                    diff[ind[t] + 1] -= b
        diff = ac.accumulate(diff)[2:]
        ac.st(min(diff))
        return

    @staticmethod
    def cf_482b(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/482/B
        tag: segment_tree|RangeOrRangeAnd
        """
        n, m = ac.read_list_ints()
        tree = RangeOrRangeAnd(n)
        nums = [ac.read_list_ints_minus_one() for _ in range(m)]
        for a, b, c in nums:
            if c != -1:
                tree.range_or(a, b, c + 1)
        if all(tree.range_and(a, b) == c + 1 for a, b, c in nums):
            ac.st("YES")
            ac.lst(tree.get())
        else:
            ac.st("NO")
        return

    @staticmethod
    def cf_987c(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/987/C
        tag: brute_force|segment_tree|prefix_suffix
        """
        n = ac.read_int()
        s = ac.read_list_ints()
        c = ac.read_list_ints()
        ind = {num: i for i, num in enumerate(sorted(list(set(s + c + [0] + [10 ** 9 + 1]))))}
        m = len(ind)
        post = [inf] * n
        tree = RangeDescendRangeMin(m)
        for i in range(n - 1, -1, -1):
            tree.range_descend(ind[s[i]], ind[s[i]], c[i])
            post[i] = tree.range_min(ind[s[i]] + 1, m - 1)

        ans = inf
        tree = RangeDescendRangeMin(m)
        for i in range(n):
            if 1 <= i <= n - 2:
                cur = c[i] + tree.range_min(0, ind[s[i]] - 1) + post[i]
                ans = ac.min(ans, cur)
            tree.range_descend(ind[s[i]], ind[s[i]], c[i])
        ac.st(ans if ans < inf else -1)
        return

    @staticmethod
    def lc_1851(intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        url: https://leetcode.cn/problems/minimum-interval-to-include-each-query/
        tag: segment_tree|RangeChangeRangeMin|offline_query|monotonic_queue
        """
        port = []
        for inter in intervals:
            port.extend(inter)
        port.extend(queries)
        lst = sorted(list(set(port)))

        ind = {num: i for i, num in enumerate(lst)}
        ceil = len(lst)
        tree = RangeDescendRangeMin(ceil)
        for a, b in intervals:
            tree.range_descend(ind[a], ind[b], b - a + 1)
        ans = [tree.range_min(ind[num], ind[num]) for num in queries]
        return [x if x != inf else -1 for x in ans]

    @staticmethod
    def lc_1340(nums: List[int], d: int) -> int:
        """
        url: https://leetcode.cn/problems/jump-game-v/
        tag: segment_tree|linear_dp
        """
        n = len(nums)
        post = [n - 1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] <= nums[i]:
                post[stack.pop()] = i - 1
            stack.append(i)

        pre = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                pre[stack.pop()] = i + 1
            stack.append(i)

        dct = defaultdict(list)
        for i, num in enumerate(nums):
            dct[num].append(i)
        tree = RangeAscendRangeMax(n)
        tree.build([0] * n)
        for num in sorted(dct):
            cur = []
            for i in dct[num]:
                left, right = pre[i], post[i]
                if left < i - d:
                    left = i - d
                if right > i + d:
                    right = i + d
                x = tree.range_max(left, right)
                cur.append([x + 1, i])

            for x, i in cur:
                tree.range_ascend(i, i, x)
        return tree.range_max(0, n - 1)

    @staticmethod
    def abc_332f(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc332/tasks/abc332_f
        tag: RangeAffineRangeSum
        """
        n, m = ac.read_list_ints()
        nums = ac.read_list_ints()
        mod = 998244353
        tree = RangeAffineRangeSum(n, mod)
        tree.build(nums)
        for _ in range(m):
            ll, rr, xx = ac.read_list_ints()
            length = rr - ll + 1
            mul = ((length - 1) * pow(length, -1, mod)) % mod
            add = (xx * pow(length, -1, mod)) % mod
            tree.range_affine(ll - 1, rr - 1, (mul << 32) | add)
        ac.lst(tree.get())
        return

    @staticmethod
    def ac_3805(ac=FastIO()):
        """
        url: https://www.acwing.com/problem/content/3808/
        tag: RangeAddRangeMin
        """
        n = ac.read_int()
        tree = RangeAddRangeSumMinMax(n)
        tree.build(ac.read_list_ints())
        for _ in range(ac.read_int()):
            lst = ac.read_list_ints()
            if len(lst) == 2:
                ll, r = lst
                if ll <= r:
                    ac.st(tree.range_min(ll, r))
                else:
                    ans1 = tree.range_min(ll, n - 1)
                    ans2 = tree.range_min(0, r)
                    ac.st(ac.min(ans1, ans2))
            else:
                ll, r, d = lst
                if ll <= r:
                    tree.range_add(ll, r, d)
                else:
                    tree.range_add(ll, n - 1, d)
                    tree.range_add(0, r, d)
        return

    @staticmethod
    def ac_5037_1(ac=FastIO()):

        n = ac.read_int()
        nums = ac.read_list_ints()
        tree = [RangeRevereRangeBitCount(n) for _ in range(22)]
        for j in range(22):
            lst = [1 if nums[i] & (1 << j) else 0 for i in range(n)]
            tree[j].build(lst)
        for _ in range(ac.read_int()):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr = lst[1:]
                ll -= 1
                rr -= 1
                ans = sum((1 << j) * tree[j].range_bit_count(ll, rr) for j in range(22))
                ac.st(ans)
            else:
                ll, rr, xx = lst[1:]
                ll -= 1
                rr -= 1
                for j in range(22):
                    if (1 << j) & xx:
                        tree[j].range_reverse(ll, rr)

        return

    @staticmethod
    def lc_2276_1():
        """
        url: https://leetcode.cn/problems/count-integers-in-intervals/
        tag: dynamic_segment_tree|union_find_range|SortedList
        """

        class CountIntervals:
            def __init__(self):
                self.n = 10 ** 9 + 7
                self.segment_tree = RangeSetRangeSumMinMaxDynamic(self.n)

            def add(self, left: int, right: int) -> None:
                self.segment_tree.range_set(left, right, 1)

            def count(self) -> int:
                return self.segment_tree.cover[1]

        return CountIntervals

    @staticmethod
    def lc_2276_2():
        """
        url: https://leetcode.cn/problems/count-integers-in-intervals/
        tag: dynamic_segment_tree|union_find_range|SortedList
        """

        class CountIntervals:

            def __init__(self):
                self.lst = SortedList()
                self.cover = 0

            def add(self, left: int, right: int) -> None:
                x = self.lst.bisect_left((left, left))
                if x - 1 >= 0 and self.lst[x - 1][1] >= left:
                    x -= 1

                while 0 <= x < len(self.lst) and not (self.lst[x][0] > right or self.lst[x][1] < left):
                    a, b = self.lst.pop(x)
                    left = left if left < a else a
                    right = right if right > b else b
                    self.cover -= b - a + 1
                self.cover += right - left + 1
                self.lst.add((left, right))

            def count(self) -> int:
                return self.cover

        return CountIntervals

    @staticmethod
    def lc_2286():
        """
        url: https://leetcode.cn/problems/booking-concert-tickets-in-groups/
        tag: segment_tree|RangeAddRangeSumMaxMin
        """

        class BookMyShow:

            def __init__(self, n: int, m: int):
                self.n = n
                self.m = m
                self.tree = RangeAddRangeSumMinMax(n)
                self.cnt = [0] * n
                self.null = SortedList(list(range(n)))

            def gather(self, k: int, max_row: int) -> List[int]:
                max_row += 1
                low = self.tree.range_min(0, max_row - 1)
                if self.m - low < k:
                    return []

                y = self.tree.range_min_bisect_left(self.m - k)
                self.cnt[y] += k
                self.tree.range_add(y, y, k)
                if self.cnt[y] == self.m:
                    self.null.discard(y)
                return [y, self.cnt[y] - k]

            def scatter(self, k: int, max_row: int) -> bool:
                max_row += 1
                s = self.tree.range_sum(0, max_row - 1)
                if self.m * max_row - s < k:
                    return False
                while k:
                    x = self.null[0]
                    rest = k if k < self.m - self.cnt[x] else self.m - self.cnt[x]
                    k -= rest
                    self.cnt[x] += rest
                    self.tree.range_add(x, x, rest)
                    if self.cnt[x] == self.m:
                        self.null.pop(0)
                return True

        return BookMyShow

    @staticmethod
    def lc_3003(s: str, k: int) -> int:
        """
        url: https://leetcode.cn/problems/maximize-the-number-of-partitions-after-operations
        tag: segment_tree|bisect_left|range_or|point_set
        """
        n = len(s)
        s = [ord(w) - ord("a") for w in s]
        tree = PointSetRangeOr(n)
        tree.build([1 << w for w in s])

        pre_ind = [-1] * n
        pre_cnt = [0] * n
        ind = [-1]
        pre = set()
        for i in range(n):
            pre_ind[i] = ind[-1]
            pre_cnt[i] = len(ind) - 1
            if s[i] not in pre and len(pre) == k:
                ind.append(i - 1)
                pre = set()
            pre.add(s[i])
        ind.append(n - 1)

        post_cnt = [0] * (n + 1)
        post = dict()
        j = n - 1
        for i in range(n - 1, -1, -1):
            post[s[i]] = post.get(s[i], 0) + 1
            while len(post) > k:
                post[s[j]] -= 1
                if not post[s[j]]:
                    post.pop(s[j])
                j -= 1
            post_cnt[i] = post_cnt[j + 1] + 1

        ans = post_cnt[0]
        for i in range(n):
            xx = s[i]
            for j in range(26):
                if j == xx or (i + 1 < n and s[i + 1] == j) or (i and s[i - 1] == j):
                    continue
                tree.point_set(i, 1 << j)
                cur_ind = pre_ind[i] + 1
                cur = pre_cnt[i]
                while cur_ind <= i:
                    jj = tree.range_or_bisect_right(cur_ind, n - 1, k)
                    cur += 1
                    cur_ind = jj + 1
                cur += post_cnt[cur_ind]
                if cur > ans:
                    ans = cur
            tree.point_set(i, 1 << xx)
        return ans

    @staticmethod
    def library_check_4(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/1/practice/contest/273169/problem/A
        tag: segment_tree|point_set|range_sum
        """
        n, q = ac.read_list_ints()
        tree = PointSetRangeSum(n)
        tree.build(ac.read_list_ints())
        for _ in range(q):
            op, x, y = ac.read_list_ints()
            if op == 1:
                tree.point_set(x, y)
            else:
                ans = tree.range_sum(x, y - 1)
                ac.st(ans)
        return

    @staticmethod
    def library_check_5(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/1/practice/contest/273169/problem/B
        tag: segment_tree|point_set|range_min
        """
        n, q = ac.read_list_ints()
        tree = PointSetRangeMin(n, inf)
        tree.build(ac.read_list_ints())
        for _ in range(q):
            op, x, y = ac.read_list_ints()
            if op == 1:
                tree.point_set(x, y)
            else:
                ans = tree.range_min(x, y - 1)
                ac.st(ans)
        return

    @staticmethod
    def library_check_6(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/1/practice/contest/273169/problem/C
        tag: segment_tree|point_set|range_min_count
        """
        n, q = ac.read_list_ints()
        tree = PointSetRangeMinCount(n, 0)
        nums = ac.read_list_ints()
        tree.build(nums)
        ac.get_random_seed()
        for _ in range(q):
            op, x, y = ac.read_list_ints()
            if op == 1:
                tree.point_set(x, y)
            else:
                ans = tree.range_min_count(x, y - 1)
                ac.lst(ans)
        return

    @staticmethod
    def library_check_7(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/A
        tag: segment_tree|point_set|range_max_sub_sum
        """
        n, q = ac.read_list_ints()
        tree = PointSetRangeMaxSubSum(n, 0)
        nums = ac.read_list_ints()
        tree.build(nums)
        ans = tree.cover[1]
        ac.st(ac.max(ans, 0))
        for _ in range(q):
            x, y = ac.read_list_ints()
            ans = tree.point_set_range_max_sub_sum(x, y)
            ac.st(ac.max(ans, 0))
        return

    @staticmethod
    def library_check_8(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/B
        tag: segment_tree|point_set|range_sum_bisect_left
        """
        n, q = ac.read_list_ints()
        tree = PointSetRangeSum(n, 0)
        nums = ac.read_list_ints()
        tree.build(nums)
        for _ in range(q):
            x, y = ac.read_list_ints()
            if x == 1:
                nums[y] = 1 - nums[y]
                tree.point_set(y, nums[y])
            else:
                ans = tree.range_sum_bisect_left(y + 1)
                ac.st(ans)
        return

    @staticmethod
    def library_check_9(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/C
        tag: segment_tree|point_set|range_max_bisect_left
        """
        n, q = ac.read_list_ints()
        tree = PointSetRangeMax(n, 0)
        tree.build(ac.read_list_ints())

        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                i, v = lst[1:]
                tree.point_set(i, v)
            else:
                x = lst[1]
                ans = tree.range_max_bisect_left(0, n - 1, x) if tree.cover[1] >= x else -1
                ac.st(ans)
        return

    @staticmethod
    def library_check_10(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/D
        tag: segment_tree|point_set|range_max_bisect_left
        """
        n, q = ac.read_list_ints()
        tree = PointSetRangeMax(n)
        tree.build(ac.read_list_ints())
        for _ in range(q):
            op, x, y = ac.read_list_ints()
            if op == 1:
                tree.point_set(x, y)
            else:
                ans = tree.range_max_bisect_left(y, n - 1, x)
                ac.st(ans)
        return

    @staticmethod
    def library_check_11(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/A
        tag: segment_tree|point_set|range_sum|inversion
        """
        n = ac.read_int()
        tree = PointSetRangeSum(n, 0)
        nums = ac.read_list_ints_minus_one()
        ans = [0] * n
        for j in range(n):
            i = nums[j]
            ans[j] = tree.range_sum(i, n - 1)
            tree.point_set(i, 1)
        ac.lst(ans)
        return

    @staticmethod
    def library_check_12(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/B
        tag: segment_tree|point_set|range_sum|inversion|bisect_left
        """
        n = ac.read_int()
        tree = PointSetRangeSum(n, 0)
        tree.build([1] * n)
        nums = ac.read_list_ints()
        ans = [0] * n
        for j in range(n - 1, -1, -1):
            i = nums[j]
            ans[j] = tree.range_sum_bisect_left(tree.cover[1] - i) + 1
            tree.point_set(ans[j] - 1, 0)
        ac.lst(ans)
        return

    @staticmethod
    def library_check_13(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/C
        tag: segment_tree|point_set|range_sum|range_include
        """
        n = ac.read_int()
        nums = ac.read_list_ints_minus_one()
        tree = PointSetRangeSum(2 * n, 0)
        ans = [0] * n
        pre = [-1] * n
        for j in range(2 * n):
            i = nums[j]
            if pre[i] == -1:
                pre[i] = j
                continue
            ans[i] = tree.range_sum(pre[i], j)
            tree.point_set(pre[i], 1)
        ac.lst(ans)
        return

    @staticmethod
    def library_check_14(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/D
        tag: segment_tree|point_set|range_sum|range_include|reverse_thinking|include_exclude
        """
        n = ac.read_int()
        nums = ac.read_list_ints_minus_one()
        tree = PointSetRangeSum(2 * n, 0)
        ans = [0] * n
        pre = [-1] * n
        for j in range(2 * n):
            i = nums[j]
            if pre[i] == -1:
                pre[i] = j
                continue
            ans[i] = (j - pre[i] - 1) - 2 * tree.range_sum(pre[i], j)
            tree.point_set(pre[i], 1)
        ac.lst(ans)
        return

    @staticmethod
    def library_check_15(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/E
        tag: segment_tree|range_add|point_get
        """
        """
        url: https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/E
        tag: segment_tree|range_add|point_get
        """
        n, q = ac.read_list_ints()
        tree = RangeAddPointGet(n)
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, vv = lst[1:]
                tree.range_add(ll, rr - 1, vv)
            else:
                ans = tree.point_get(lst[1])
                ac.st(ans)
        return

    @staticmethod
    def library_check_16(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/problem/A
        tag: segment_tree|point_set|range_sum
        """
        n = ac.read_int()
        nums = ac.read_list_ints()
        odd = PointSetRangeSum(n)
        lst = [nums[i] if i % 2 else 0 for i in range(n)]
        odd.build(lst)

        even = PointSetRangeSum(n)
        lst = [nums[i] if i % 2 == 0 else 0 for i in range(n)]
        even.build(lst)

        for _ in range(ac.read_int()):
            op, x, y = ac.read_list_ints()
            if op == 0:
                if (x - 1) % 2:
                    odd.point_set(x - 1, y)
                else:
                    even.point_set(x - 1, y)
            else:
                odd_sum = odd.range_sum(x - 1, y - 1)
                even_sum = even.range_sum(x - 1, y - 1)
                ans = odd_sum - even_sum if (x - 1) % 2 else even_sum - odd_sum
                ac.st(ans)
        return

    @staticmethod
    def library_check_17(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/problem/B
        tag: segment_tree|matrix_build|range_mul
        """
        r, n, m = ac.read_list_ints()
        nums = []
        for _ in range(n):
            for _ in range(2):
                nums.extend(ac.read_list_ints())
            ac.read_str()

        tree = MatrixBuildRangeMul(n, 0, r)
        tree.matrix_build(nums)

        for _ in range(m):
            ll, rr = ac.read_list_ints_minus_one()
            ans = tree.range_mul(ll, rr)
            ac.lst((ans[0], ans[1]))
            ac.lst((ans[2], ans[3]))
            ac.st("")
        return

    @staticmethod
    def library_check_18(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/problem/C
        tag: segment_tree|point_set|range_inverse
        """
        n, q = ac.read_list_ints()
        tree = PointSetRangeInversion(n, 40)
        tree.build(ac.read_list_ints_minus_one())

        for _ in range(q):
            op, x, y = ac.read_list_ints_minus_one()
            if op == 0:
                ans = tree.range_inverse(x, y)
                ac.st(ans)
            else:
                tree.point_set(x, y)
        return

    @staticmethod
    def library_check_19(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/problem/D
        tag: segment_tree|point_set|range_or
        """
        n, q = ac.read_list_ints()
        tree = PointSetRangeOr(n)
        tree.build([1 << x for x in ac.read_list_ints_minus_one()])

        for _ in range(q):
            op, x, y = ac.read_list_ints_minus_one()
            if op == 0:
                ans = tree.range_or(x, y)
                ac.st(bin(ans).count("1"))
            else:
                tree.point_set(x, x, 1 << y)
        return

    @staticmethod
    def library_check_20(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/1/practice/contest/279634/problem/A
        tag: segment_tree|range_add|point_get
        """
        n, q = ac.read_list_ints()
        tree = RangeAddPointGet(n)

        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, v = lst[1:]
                tree.range_add(ll, rr - 1, v)
            else:
                ans = tree.point_get(lst[1])
                ac.st(ans)
        return

    @staticmethod
    def library_check_21(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/1/practice/contest/279634/problem/A
        tag: segment_tree|range_ascend|point_get
        """
        n, q = ac.read_list_ints()
        tree = RangeAscendPointGet(n)

        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, v = lst[1:]
                tree.range_ascend(ll, rr - 1, v)
            else:
                ans = tree.point_get(lst[1])
                ac.st(ans)
        return

    @staticmethod
    def library_check_22(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/1/practice/contest/279634/problem/A
        tag: segment_tree|range_set|point_get
        """
        n, q = ac.read_list_ints()
        tree = RangeSetPointGet(n)
        tree.build([0] * n)
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, v = lst[1:]
                tree.range_set(ll, rr - 1, v)
            else:
                ans = tree.point_get(lst[1])
                ac.st(ans)
        return

    @staticmethod
    def library_check_23(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/problem/E
        tag: segment_tree|bisect_left|brute_force|classical|range_min|point_set
        """
        n, q = ac.read_list_ints()
        tree = PointSetRangeMin(n, inf)
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                i, h = lst[1:]
                tree.point_set(i, h)
            else:
                ll, rr, p = lst[1:]
                ans = 0
                while ll <= rr - 1:
                    x = tree.range_min_bisect_left(ll, rr - 1, p)
                    if x == -1:
                        break
                    ll = x
                    tree.point_set(ll, inf)
                    ans += 1
                ac.st(ans)
        return

    @staticmethod
    def library_check_24(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/A
        tag: segment_tree|range_add|range_min
        """
        n, q = ac.read_list_ints()
        tree = RangeAddRangeSumMinMax(n)
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, v = lst[1:]
                tree.range_add(ll, rr - 1, v)
            else:
                ll, rr = lst[1:]
                ans = tree.range_min(ll, rr - 1)
                ac.st(ans)
        return

    @staticmethod
    def library_check_25(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/B
        tag: segment_tree|range_affine|range_sum
        """
        n, q = ac.read_list_ints()
        mod = 10 ** 9 + 7
        tree = RangeAffineRangeSum(n, mod)
        tree.build([1] * n)
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, b = lst[1:]
                tree.range_affine(ll, rr - 1, (b << 32))
            else:
                ll, rr = lst[1:]
                ans = tree.range_sum(ll, rr - 1)
                ac.st(ans)
        return

    @staticmethod
    def library_check_26(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/C
        tag: segment_tree|range_or|range_and
        """
        n, q = ac.read_list_ints()
        tree = RangeOrRangeAnd(n)
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, b = lst[1:]
                tree.range_or(ll, rr - 1, b)
            else:
                ll, rr = lst[1:]
                ans = tree.range_and(ll, rr - 1)
                ac.st(ans)
        return

    @staticmethod
    def library_check_27(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/D
        tag: segment_tree|range_add|range_sum
        """
        n, q = ac.read_list_ints()
        tree = RangeAddRangeSumMinMax(n)
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, b = lst[1:]
                tree.range_add(ll, rr - 1, b)
            else:
                ll, rr = lst[1:]
                ans = tree.range_sum(ll, rr - 1)
                ac.st(ans)
        return

    @staticmethod
    def library_check_28(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/E
        tag: segment_tree|range_set|range_min
        """
        n, q = ac.read_list_ints()
        tree = RangeSetRangeSumMinMax(n)
        tree.build([0] * n)
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, b = lst[1:]
                tree.range_set(ll, rr - 1, b)
            else:
                ll, rr = lst[1:]
                ans = tree.range_min(ll, rr - 1)
                ac.st(ans)
        return

    @staticmethod
    def library_check_29(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/F
        tag: segment_tree|range_set|range_sum
        """
        n, q = ac.read_list_ints()
        tree = RangeSetRangeSumMinMax(n)
        tree.build([0] * n)
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, b = lst[1:]
                tree.range_set(ll, rr - 1, b)
            else:
                ll, rr = lst[1:]
                ans = tree.range_sum(ll, rr - 1)
                ac.st(ans)
        return

    @staticmethod
    def library_check_30(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/3/practice/contest/280799/problem/A
        tag: segment_tree|range_set|range_max_non_emp_con_sub_sum
        """
        n, q = ac.read_list_ints()
        tree = RangeSetRangeMaxNonEmpConSubSum(n)
        tree.build([0] * n)
        for _ in range(q):
            ll, rr, v = ac.read_list_ints()
            tree.range_set(ll, rr - 1, v)
            ans = ac.max(tree.cover[1], 0)
            ac.st(ans)
        return

    @staticmethod
    def library_check_31(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/3/practice/contest/280799/problem/B
        tag: segment_tree|range_reverse|range_bit_count_bisect_left
        """
        n, m = ac.read_list_ints()
        tree = RangeRevereRangeBitCount(n)
        for _ in range(m):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr = lst[1:]
                tree.range_reverse(ll, rr - 1)
            else:
                ans = tree.range_bit_count_bisect_left(lst[1] + 1)
                ac.st(ans)
        return

    @staticmethod
    def library_check_32(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/3/practice/contest/280799/problem/C
        tag: segment_tree|range_add|range_max|bisect_left
        """
        n, m = ac.read_list_ints()
        tree = RangeAddRangeSumMinMax(n)
        for _ in range(m):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, v = lst[1:]
                tree.range_add(ll, rr - 1, v)
            else:
                x, ll = lst[1:]
                ans = tree.range_max_bisect_left(ll, n - 1, x)
                ac.st(ans)
        return

    @staticmethod
    def library_check_33(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/A
        tag: segment_tree|range_change_add|range_sum
        """
        n, q = ac.read_list_ints()
        tree = RangeSetAddRangeSumMinMax(n, 1)
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, v = lst[1:]
                tree.range_set_add(ll, rr - 1, (v, 0))
            elif lst[0] == 2:
                ll, rr, v = lst[1:]
                tree.range_set_add(ll, rr - 1, (-tree.initial, v))
            else:
                ll, rr = lst[1:]
                ans = tree.range_sum(ll, rr - 1)
                ac.st(ans)
        return

    @staticmethod
    def library_check_34(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/B
        tag: segment_tree|diff_array|range_add|point_get|range_sum
        """
        n, q = ac.read_list_ints()
        tree = RangeAddPointGet(n)
        diff = RangeAddRangeSumMinMax(n + 1)
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, a, d = lst[1:]
                tree.range_add(ll - 1, rr - 1, a)
                if ll <= rr - 1:
                    diff.range_add(ll, rr - 1, d)
                    diff.range_add(rr, rr, -d * (rr - ll))
            else:
                ans = diff.range_sum(0, lst[1] - 1) + tree.point_get(lst[1] - 1)
                ac.st(ans)
        return

    @staticmethod
    def library_check_35(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/C
        tag: segment_tree|range_set|range_seg_count_length
        """
        q = ac.read_int()
        n = 10 ** 6 + 10
        tree = RangeSetRangeSegCountLength(n)
        base = 5 * 10 ** 5
        for _ in range(q):
            lst = ac.read_list_strs()
            ll, d = [int(w) for w in lst[1:]]
            ll += base
            rr = ll + d - 1
            if lst[0] == "W":
                tree.range_set(ll, rr, 0)
            else:
                tree.range_set(ll, rr, 1)
            ac.lst([tree.cover[1], tree.sum[1]])
        return

    @staticmethod
    def library_check_36(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/D
        tag: segment_tree|range_add|range_weighted_sum
        """
        n, q = ac.read_list_ints()
        tree = RangeAddRangeWeightedSum(n)
        tree.build(ac.read_list_ints())
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, d = lst[1:]
                tree.range_add(ll - 1, rr - 1, d)
            else:
                ll, rr = lst[1:]
                ans = tree.range_weighted_sum(ll - 1, rr - 1)
                ac.st(ans)
        return

    @staticmethod
    def library_check_37(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/E
        tag: segment_tree|range_chmin_chmax|point_get
        """
        n, q = ac.read_list_ints()
        tree = RangeChminChmaxPointGet(n, 0, 10 ** 5)
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, hh = lst[1:]
                tree.range_chmin_chmax(ll, rr, hh, tree.high_initial)
            else:
                ll, rr, hh = lst[1:]
                tree.range_chmin_chmax(ll, rr, tree.low_initial, hh)
        ans = tree.get()
        ac.st("\n".join(str(x) for x in ans))
        return

    @staticmethod
    def library_check_38(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/F
        tag: segment_tree_dynamic|range_set|range_sum_bisect_left
        """
        n = ac.read_int()
        tree = RangeSetPreSumMaxDynamicDct(n, 10 ** 5, -1 << 32)
        while True:
            lst = ac.read_list_strs()
            if lst[0] == "I":
                ll, rr, hh = [int(w) for w in lst[1:]]
                tree.range_set(ll - 1, rr - 1, hh)
            elif lst[0] == "Q":
                hh = int(lst[1])
                ans = tree.range_pre_sum_max_bisect_left(hh)
                ac.st(ans)
            else:
                break
        return

    @staticmethod
    def abc_287g(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc287/tasks/abc287_g
        tag: segment_tree|range_sum|dynamic|offline
        """
        n = ac.read_int()
        nums = [ac.read_list_ints() for _ in range(n)]
        q = ac.read_int()
        queries = [ac.read_list_ints() for _ in range(q)]
        nodes = set()
        for a, _ in nums:
            nodes.add(a)
        for lst in queries:
            if lst[0] == 1:
                nodes.add(lst[2])
        nodes = sorted(nodes)
        ind = {num: i for i, num in enumerate(nodes)}
        n = len(nodes)
        tree = PointAddRangeSum1Sum2(n)
        for a, b in nums:
            tree.point_add(ind[a], (b, a * b))
        for lst in queries:
            if lst[0] == 1:
                x, y = lst[1:]
                x -= 1
                a, b = nums[x]
                tree.point_add(ind[a], (-b, -b * a))
                nums[x][0] = y
                a, b = nums[x]
                tree.point_add(ind[a], (b, b * a))
            elif lst[0] == 2:
                x, y = lst[1:]
                x -= 1
                a, b = nums[x]
                tree.point_add(ind[a], (-b, -b * a))
                nums[x][1] = y
                a, b = nums[x]
                tree.point_add(ind[a], (b, b * a))
            else:
                x = lst[1]
                tot = tree.cover1[1]
                if tot < x:
                    ac.st(-1)
                else:
                    rest, c, i = tree.range_sum2_bisect_left(tot - x)
                    rest += c * nodes[i]
                    ac.st(tree.cover2[1] - rest)
        return

    @staticmethod
    def cf_85d(ac=FastIO()):
        """
        url: https://codeforces.com/contest/85/problem/D
        tag: segment_tree|point_add|range_sum
        """
        n = ac.read_int()
        queries = [ac.read_list_strs() for _ in range(n)]
        nodes = {0}
        for lst in queries:
            if lst[0] != "sum":
                nodes.add(int(lst[1]))
        nodes = sorted(nodes)
        m = len(nodes)
        ind = {num: i for i, num in enumerate(nodes)}
        tree = PointAddRangeSumMod5(m)
        for lst in queries:
            if lst[0] == "add":
                x = int(lst[1])
                tree.point_add(ind[x], (1, x))
            elif lst[0] == "del":
                x = int(lst[1])
                tree.point_add(ind[x], (-1, -x))
            else:
                ans = tree.cover[1][3]
                ac.st(ans)
        return

    @staticmethod
    def cf_52c(ac=FastIO()):
        """
        url: https://codeforces.com/contest/52/problem/C
        tag: segment_tree|circular_array|range_add|range_min
        """
        n = ac.read_int()  # inf = 1 << 64
        tree = RangeAddRangeSumMinMax(n)
        tree.build(ac.read_list_ints())
        tot = 0
        for _ in range(ac.read_int()):
            lst = ac.read_list_ints()
            if len(lst) == 2:
                x, y = lst
                ans = inf
                for a, b in [(x, y)] if x <= y else [(x, n - 1), (0, y)]:
                    cur = tree.range_min(a, b)
                    ans = ac.min(ans, cur)
                ac.st(ans + tot)
            else:
                x, y, v = lst
                if x <= y:
                    tree.range_add(x, y, v)
                else:
                    tot += v
                    if y + 1 <= x - 1:
                        tree.range_add(y + 1, x - 1, -v)
        return

    @staticmethod
    def cf_474e(ac=FastIO()):
        """
        url: https://codeforces.com/contest/474/problem/E
        tag: segment_tree|point_set|range_max_index|linear_dp|classical
        """
        n, d = ac.read_list_ints()
        nums = ac.read_list_ints()
        nodes = sorted(set(nums))
        dct = {num: i for i, num in enumerate(nodes)}
        m = len(nodes)
        tree = PointSetRangeMaxIndex(m)
        pre = [-1] * n
        for x, num in enumerate(nums):
            cur_val = 0
            cur_ind = -1
            i = bisect.bisect_right(nodes, num - d) - 1
            if i >= 0:
                val, ind = tree.range_max_index(0, i)
                if val > cur_val:
                    cur_val = val
                    cur_ind = ind
            i = bisect.bisect_left(nodes, num + d)
            if i < m:
                val, ind = tree.range_max_index(i, m - 1)
                if val > cur_val:
                    cur_val = val
                    cur_ind = ind
            pre[x] = cur_ind
            tree.point_set_index(dct[num], x, cur_val + 1)

        ans, ind = tree.range_max_index(0, m - 1)
        lst = [ind]
        while pre[lst[-1]] != -1:
            lst.append(pre[lst[-1]])
        lst.reverse()
        ac.st(ans)
        ac.lst([x + 1 for x in lst])
        return

    @staticmethod
    def ac_246(ac=FastIO()):
        """
        url: https://www.acwing.com/problem/content/246/
        tag: segment_tree|range_change|range_merge|sub_consequence
        """
        n, m = ac.read_list_ints()
        segment = RangeSetRangeMaxNonEmpConSubSum(n, 1001)
        segment.build(ac.read_list_ints())
        for _ in range(m):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                a, b = lst[1:]
                a, b = ac.min(a, b), ac.max(a, b)
                ans = segment.range_max_non_emp_con_sub_sum(a - 1, b - 1)
                ac.st(ans)
            else:
                a, s = lst[1:]
                segment.point_set(a - 1, s)
        return

    @staticmethod
    def cf_920f_2(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/920/F
        tag: union_find|all_factor_cnt|range_sum|point_add
        """
        n, m = ac.read_list_ints()
        nums = ac.read_list_ints()
        uf = UnionFind(n + 1)
        at = AllFactorCnt(10 ** 6)
        tree = PointAddRangeSum(n)
        tree.build(nums)
        for i in range(m):
            op, ll, rr = ac.read_list_ints_minus_one()
            if op == 0:
                ll = uf.find(ll)
                while ll <= rr:
                    pre = nums[ll]
                    nums[ll] = at.all_factor_cnt[pre]
                    cur = nums[ll]
                    if cur < pre:
                        tree.point_add(ll + 1, cur - pre)
                    if cur <= 2:
                        uf.union_right(ll, ll + 1)
                        ll = uf.find(ll + 1)
                    else:
                        ll += 1
            else:
                ans = tree.range_sum(ll + 1, rr + 1)
                ac.st(ans)
        return

    @staticmethod
    def cf_438d(ac=FastIO()):
        """
        url: https://codeforces.com/contest/438/problem/D
        tag: segment_tree|point_set|range_mod|range_sum|classical
        """
        n, q = ac.read_list_ints()
        tree = RangeModPointSetRangeSum(n)
        tree.build(ac.read_list_ints())
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ans = tree.range_sum(lst[1] - 1, lst[2] - 1)
                ac.st(ans)
            elif lst[0] == 2:
                tree.range_mod(lst[1] - 1, lst[2] - 1, lst[3])
            else:
                tree.point_set(lst[1] - 1, lst[2])
        return

    @staticmethod
    def cf_1187d(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/1187/D
        tag: segment_tree|point_set|range_min|classical
        """
        for _ in range(ac.read_int()):

            def check():
                n = ac.read_int()
                a = ac.read_list_ints()
                b = ac.read_list_ints()
                if Counter(a) != Counter(b):
                    ac.st("NO")
                    return
                tree = PointSetRangeMin(n, n + 1)
                tree.build(a)
                dct = [deque() for _ in range(n + 1)]
                for i in range(n):
                    dct[a[i]].append(i)
                for i in range(n):
                    x = b[i]
                    j = dct[x].popleft()
                    if tree.range_min(0, j) != x:
                        ac.st("NO")
                        return
                    tree.point_set(j, n + 1)
                ac.st("YES")
                return

            check()
        return

    @staticmethod
    def cf_914d(ac=FastIO()):
        """
        url: https://codeforces.com/contest/914/problem/D
        tag: segment_tree|point_set|range_gcd
        """
        n = ac.read_int()
        tree = PointSetRangeGcd(n)
        tree.build(ac.read_list_ints())
        for _ in range(ac.read_int()):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, xx = lst[1:]
                ans = tree.range_gcd_check(ll - 1, rr - 1, xx)
                ac.st("YES" if ans else "NO")
            else:
                ll, xx = lst[1:]
                tree.point_set(ll - 1, xx)
        return

    @staticmethod
    def cf_1567e(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/1567/E
        tag: segment_tree|point_set|range_ascend_sub_cnt
        """
        _, q = ac.read_list_ints()
        nums = ac.read_list_ints()
        tree = PointSetRangeAscendSubCnt(nums)
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, xx = lst[1:]
                tree.point_set(ll - 1, xx)
            else:
                ll, rr = lst[1:]
                ans = tree.range_ascend_sub_cnt(ll - 1, rr - 1)
                ac.st(ans)
        return

    @staticmethod
    def cf_522d(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/522/D
        tag: segment_tree|point_set|range_min|offline_query
        """
        ac.get_random_seed()
        n, q = ac.read_list_ints()
        nums = ac.read_list_ints()
        tree = PointSetRangeMin(n, n)
        queries = [[] for _ in range(n)]
        for i in range(q):
            ll, rr = ac.read_list_ints_minus_one()
            queries[rr].append((i, ll))
        ans = [-1] * q

        pre = [-1] * n
        dct = dict()
        for i in range(n):
            if nums[i] ^ ac.random_seed in dct:
                pre[i] = dct[nums[i] ^ ac.random_seed]
            dct[nums[i] ^ ac.random_seed] = i

        for rr in range(n):
            if pre[rr] != -1:
                tree.point_set(pre[rr], rr - pre[rr])
            for i, ll in queries[rr]:
                cur = tree.range_min(ll, rr)
                if cur < n:
                    ans[i] = cur
        for a in ans:
            ac.st(a)
        return

    @staticmethod
    def lg_p1972(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1972
        tag: point_add|range_sum|tree_array|offline_query
        """
        n = ac.read_int()
        nums = ac.read_list_ints()
        q = ac.read_int()
        queries = [[] for _ in range(n)]
        for i in range(q):
            ll, rr = ac.read_list_ints_minus_one()
            queries[rr].append((i, ll))

        ans = [0] * q
        tree = PointAddRangeSum(n)
        tree.build([1] * n)
        pre = dict()
        for rr in range(n):
            if nums[rr] in pre:
                tree.point_add(pre[nums[rr]] + 1, -1)
            pre[nums[rr]] = rr
            for i, ll in queries[rr]:
                ans[i] = tree.range_sum(ll + 1, rr + 1)
        for a in ans:
            ac.st(a)
        return

    @staticmethod
    def cf_703d(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/703/D
        tag: segment_tree|point_add|range_xor|offline_query
        """
        ac.get_random_seed()
        n = ac.read_int()
        nums = ac.read_list_ints()
        q = ac.read_int()
        queries = [[] for _ in range(n)]
        for i in range(q):
            ll, rr = ac.read_list_ints_minus_one()
            queries[rr].append((i, ll))

        ans = [0] * q
        tree = PointSetRangeXOr(n)
        tree.build(nums)
        pre_xor = [0] * (n + 1)

        pre = dict()
        for rr in range(n):
            pre_xor[rr + 1] = pre_xor[rr] ^ nums[rr]
            if nums[rr] ^ ac.random_seed in pre:
                tree.point_set(pre[nums[rr] ^ ac.random_seed], 0)
            pre[nums[rr] ^ ac.random_seed] = rr
            for i, ll in queries[rr]:
                ans[i] = tree.range_xor(ll, rr) ^ pre_xor[rr + 1] ^ pre_xor[ll]
        for a in ans:
            ac.st(a)
        return

    @staticmethod
    def cf_1609e(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/1609/E
        tag: segment_tree|point_set|range_cover
        """
        n, q = ac.read_list_ints()
        s = ac.read_str()
        tree = PointSetRangeNotExistABC(n)
        tree.build(s)
        for _ in range(q):
            ll, s = ac.read_list_strs()
            ans = tree.point_set(int(ll) - 1, s)
            ac.st(ans)
        return

    @staticmethod
    def main(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc285/tasks/abc285_f
        tag: segment_tree|point_add|range_sum|range_ascend_sub_cnt|point_set
        """
        n = ac.read_int()
        tree = PointSetRangeAscendSubCnt([ord(w) - ord("a") for w in ac.read_str()])
        tree_cnt = [PointAddRangeSum(n) for _ in range(26)]
        for x in range(n):
            tree_cnt[tree.lst[x]].point_add(x + 1, 1)

        for _ in range(ac.read_int()):

            def check():
                lst = ac.read_list_strs()
                if lst[0] == '1':
                    i, w = int(lst[1]) - 1, ord(lst[2]) - ord("a")
                    tree_cnt[tree.lst[i]].point_add(i + 1, -1)
                    tree.point_set(i, w)
                    tree_cnt[tree.lst[i]].point_add(i + 1, 1)
                else:
                    ll, rr = [int(w) - 1 for w in lst[1:]]
                    ans = tree.range_ascend_sub_cnt(ll, rr)
                    length = rr - ll + 1
                    if ans == length * (length + 1) // 2:
                        if all(tree_cnt[i].range_sum(ll + 1, rr + 1) == tree_cnt[i].range_sum(1, n) for i in
                               range(tree.lst[ll] + 1, tree.lst[rr])):
                            ac.st("Yes")
                            return
                    ac.st("No")
                return

            check()
        return

    @staticmethod
    def cf_1208d(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/1208/D
        tag: segment_tree|reverse_thinking|construction|point_set|range_sum_bisect_left
        """
        n = ac.read_int()
        tree = PointSetRangeSum(n)
        tree.build(list(range(1, n + 1)))
        pre = ac.read_list_ints()
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            ind = tree.range_sum_bisect_right(pre[i])
            ans[i] = ind + 1
            tree.point_set(ind, 0)
        ac.lst(ans)
        return

    @staticmethod
    def abc_327f(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc327/tasks/abc327_f
        tag: segment_tree|range_add|range_max
        """
        n, d, w = ac.read_list_ints()
        d -= 1
        w -= 1
        m = 2 * 10 ** 5
        pos = [[] for _ in range(m + 1)]
        for _ in range(n):
            t, x = ac.read_list_ints()
            pos[x].append(t)
        tree = RangeAddRangeSumMinMax(m + 1)
        ans = 0
        for s in range(w):
            for t in pos[s]:
                low = ac.max(t, d)
                high = ac.min(m, t + d)
                tree.range_add(low, high, 1)
        for s in range(m + 1 - w):
            for t in pos[s + w]:
                low = ac.max(t, d)
                high = ac.min(m, t + d)
                tree.range_add(low, high, 1)
            ans = ac.max(ans, tree.ceil[1])
            for t in pos[s]:
                low = ac.max(t, d)
                high = ac.min(m, t + d)
                tree.range_add(low, high, -1)
        ac.st(ans)
        return

    @staticmethod
    def cf_558e(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/558/E
        tag: segment_tree|range_set|range_sum|alphabet
        """
        n, q = ac.read_list_ints()
        s = ac.read_str()
        tree = [RangeSetRangeSumMinMax(n, 0) for _ in range(26)]
        for i in range(n):
            x = ord(s[i]) - ord("a")
            tree[x].range_set(i, i, 1)

        for _ in range(q):
            ll, rr, k = ac.read_list_ints()
            ll -= 1
            rr -= 1
            cnt = [tree[i].range_sum(ll, rr) for i in range(26)]
            if k == 0:
                for i in range(26):
                    if cnt[i]:
                        tree[i].range_set(ll, rr, 0)
                for i in range(25, -1, -1):
                    if cnt[i]:
                        tree[i].range_set(ll, ll + cnt[i] - 1, 1)
                        ll += cnt[i]
            else:
                for i in range(26):
                    if cnt[i]:
                        tree[i].range_set(ll, rr, 0)
                for i in range(26):
                    if cnt[i]:
                        tree[i].range_set(ll, ll + cnt[i] - 1, 1)
                        ll += cnt[i]
        ans = [""] * n
        for i in range(26):
            lst = tree[i].get()
            for j in range(n):
                if lst[j]:
                    ans[j] = chr(i + ord("a"))
        ac.st("".join(ans))
        return

    @staticmethod
    def cf_1557d(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1557/problem/D
        tag: segment_tree|range_ascend|range_max_index|dp
        """
        m, n = ac.read_list_ints()
        queries = [ac.read_list_ints() for _ in range(n)]
        nodes = set()
        row = [[] for _ in range(m + 1)]
        for i, ll, rr in queries:
            nodes.add(ll)
            nodes.add(rr)
            row[i].append((ll, rr))
        nodes = sorted(nodes)
        ind = {num: i for i, num in enumerate(nodes)}
        k = len(ind)
        tree = RangeAscendRangeMaxIndex(k, 0)
        dp = [0] * (m + 1)
        pre = [0] * (m + 1)
        for i in range(1, m + 1):
            cur = 0
            cur_ind = 0
            for ll, rr in row[i]:
                res = tree.range_max_index(ind[ll], ind[rr])
                if res[0] > cur:
                    cur, cur_ind = res
            dp[i] = cur + 1
            pre[i] = cur_ind
            for ll, rr in row[i]:
                tree.range_ascend(ind[ll], ind[rr], i, cur + 1)
        x = dp.index(max(dp))
        lst = [x]
        while pre[lst[-1]]:
            lst.append(pre[lst[-1]])
        ac.st(m - len(lst))
        dct = set(lst)
        ac.lst([x for x in range(1, m + 1) if x not in dct])
        return

    @staticmethod
    def cf_1114f(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/1114/F
        tag: segment_tree|range_set|range_sum|range_mul
        """
        primes = PrimeSieve().eratosthenes_sieve(300)
        mod = 10 ** 9 + 7
        pf = PrimeFactor(300)
        n, q = ac.read_list_ints()
        nums = ac.read_list_ints()
        uf = dict()
        for f in primes:
            uf[f] = RangeSetRangeSumMinMax(n, 0)
        tree = RangeMulRangeMul(n, mod)
        tree.build(nums)
        for i in range(n):
            for p, _ in pf.prime_factor[nums[i]]:
                uf[p].range_set(i, i, 1)
        for _ in range(q):
            lst = ac.read_list_strs()
            if lst[0] == "MULTIPLY":
                ll, rr, x = [int(w) for w in lst[1:]]
                tree.range_mul_update(ll - 1, rr - 1, x)
                for p, _ in pf.prime_factor[x]:
                    uf[p].range_set(ll - 1, rr - 1, 1)
            else:
                ll, rr = [int(w) for w in lst[1:]]
                ans = tree.range_mul_query(ll - 1, rr - 1)
                for p in uf:
                    if uf[p].range_sum(ll - 1, rr - 1) > 0:
                        ans *= (p - 1)
                        ans *= pow(p, -1, mod)
                ac.st(ans % mod)
        return

    @staticmethod
    def cf_292e(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/292/E
        tag: segment_tree|range_set|point_get
        """
        n, m = ac.read_list_ints()
        a = ac.read_list_ints()
        b = ac.read_list_ints()
        tree = RangeSetPointGet(n, -n)
        for _ in range(m):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                x, y, k = lst[1:]
                x -= 1
                y -= 1
                tree.range_set(y, y + k - 1, -y + x)
            else:
                x = lst[1] - 1
                y = tree.point_get(x)
                if y == -n:
                    ac.st(b[x])
                else:
                    i = x + tree.point_get(x)
                    ac.st(a[i])
        return

    @staticmethod
    def cf_1881g(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1881/problem/G
        tag: segment_tree|range_add|range_palindrome
        """
        for _ in range(ac.read_int()):
            n, m = ac.read_list_ints()
            tree = RangeAddRangePalindrome(n)
            s = [ord(w) - ord("a") for w in ac.read_str()]
            tree.build(s)
            for _ in range(m):
                lst = ac.read_list_ints()
                if lst[0] == 1:
                    ll, rr, x = lst[1:]
                    tree.range_add(ll - 1, rr - 1, x)
                else:
                    ll, rr = lst[1:]
                    ans = tree.range_palindrome(ll - 1, rr - 1)
                    ac.st("YES" if not ans else "NO")
        return

    @staticmethod
    def lc_1622_1():
        """
        url: https://leetcode.cn/problems/fancy-sequence/
        tag: segment_tree|range_affine|range_sum
        """

        class Fancy:

            def __init__(self):
                n = 10 ** 5
                self.ind = 0
                self.mod = 10 ** 9 + 7
                self.tree = RangeAffineRangeSum(n, self.mod)
                return

            def append(self, val: int) -> None:
                self.ind += 1
                self.tree.range_affine(self.ind - 1, self.ind - 1, (1 << 32) | val)
                return

            def addAll(self, inc: int) -> None:
                if self.ind:
                    self.tree.range_affine(0, self.ind - 1, (1 << 32) | inc)
                return

            def multAll(self, m: int) -> None:
                if self.ind:
                    self.tree.range_affine(0, self.ind - 1, m << 32)
                return

            def getIndex(self, idx: int) -> int:
                if idx >= self.ind:
                    return -1
                return self.tree.range_sum(idx, idx) % self.mod

        return Fancy

    @staticmethod
    def lc_1622_2():
        """
        url: https://leetcode.cn/problems/fancy-sequence/
        tag: segment_tree|range_affine|range_sum
        """

        class Fancy:

            def __init__(self):
                self.lst = []
                self.add = 0
                self.mul = 1
                self.mod = 10 ** 9 + 7

            @lru_cache(None)
            def ppow(self, a):
                return pow(a, -1, self.mod)

            def append(self, val: int) -> None:
                self.lst.append((val - self.add) * self.ppow(self.mul))

            def addAll(self, inc: int) -> None:
                self.add = (self.add + inc) % self.mod

            def multAll(self, m: int) -> None:
                self.add = (self.add * m) % self.mod
                self.mul = (self.mul * m) % self.mod

            def getIndex(self, idx: int) -> int:
                if idx >= len(self.lst):
                    return -1
                return (self.lst[idx] * self.mul + self.add) % self.mod

        return Fancy

    @staticmethod
    def cf_915e(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/915/E
        tag: segment_tree|range_set|range_sum|dynamic
        """
        n, q = [ac.read_int() for _ in range(2)]
        tree = RangeSetRangeSumMinMaxDynamicDct(n + 1, 4 * 10 ** 5, -1)
        tree.range_set(1, n, 1)
        for _ in range(q):
            ll, rr, k = ac.read_list_ints()
            if k == 1:
                tree.range_set(ll, rr, 0)
            else:
                tree.range_set(ll, rr, 1)
            ac.st(tree.cover[1])
        return

    @staticmethod
    def lg_p5848(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P5848
        tag: segment_tree|range_set|range_pre_max_sum|dynamic
        """
        n = ac.read_int()
        tree = RangeSetPreSumMaxDynamic(n, -inf)
        while True:
            lst = ac.read_list_strs()
            if lst[0] == "I":
                ll, rr, hh = [int(w) for w in lst[1:]]
                tree.range_set(ll - 1, rr - 1, hh)
            elif lst[0] == "Q":
                hh = int(lst[1])
                ans = tree.range_pre_sum_max_bisect_left(hh)
                ac.st(ans)
            else:
                break
        return

    @staticmethod
    def cf_877e(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/877/E
        tag: segment_tree|range_reverse|dfs_order|range_bit_count
        """
        n = ac.read_int()
        parent = [-1] + ac.read_list_ints_minus_one()
        dct = [[] for _ in range(n)]
        for i in range(1, n):
            dct[parent[i]].append(i)
        start, end = DFS().gen_bfs_order_iteration(dct, 0)
        tree = RangeRevereRangeBitCount(n)
        lst = ac.read_list_ints()
        nums = [0] * n
        for i in range(n):
            nums[start[i]] = lst[i]
        tree.build(nums)
        for _ in range(ac.read_int()):
            lst = ac.read_list_strs()
            if lst[0] == "get":
                x = int(lst[1]) - 1
                ans = tree.range_bit_count(start[x], end[x])
                ac.st(ans)
            else:
                x = int(lst[1]) - 1
                tree.range_reverse(start[x], end[x])
        return

    @staticmethod
    def cf_1108e2(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1108/problem/E2
        tag: segment_tree|range_add|range_min|prefix_suffix|bryte_force|brain_teaser
        """
        n, m = ac.read_list_ints()
        nums = ac.read_list_ints()
        lst = [ac.read_list_ints_minus_one() for _ in range(m)]

        tree = RangeAddRangeSumMinMax(n)
        tree.build(nums)
        cur_min = nums[:]
        tmp = sorted(lst, key=lambda it: it[1])
        j = 0
        for i in range(n):
            while j < m and tmp[j][1] < i:
                a, b = tmp[j]
                tree.range_add(a, b, -1)
                j += 1

            if i:
                cur = tree.range_min(0, i - 1)
                if cur < cur_min[i]:
                    cur_min[i] = cur

        tmp = sorted(lst, key=lambda it: -it[0])
        tree = RangeAddRangeSumMinMax(n)
        tree.build(nums)
        j = 0
        for i in range(n - 1, -1, -1):
            while j < m and tmp[j][0] > i:
                a, b = tmp[j]
                tree.range_add(a, b, -1)
                j += 1
            if i + 1 < n:
                cur = tree.range_min(i + 1, n - 1)
                if cur < cur_min[i]:
                    cur_min[i] = cur
        cur_min = [nums[i] - cur_min[i] for i in range(n)]
        ans = max(cur_min)
        res = cur_min.index(ans)
        ac.st(ans)
        tmp = [i + 1 for i in range(m) if not lst[i][0] <= res <= lst[i][1]]
        ac.st(len(tmp))
        ac.lst(tmp)
        return

    @staticmethod
    def cf_1234d(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1234/problem/D
        tag: segment_tree|point_set|range_or
        """
        s = [1 << (ord(w) - ord("a")) for w in ac.read_str()]
        n = len(s)
        tree = PointSetRangeOr(n)
        tree.build(s)
        for _ in range(ac.read_int()):
            lst = ac.read_list_strs()
            if lst[0] == "1":
                pos, w = lst[1:]
                tree.point_set(int(pos) - 1, 1 << (ord(w) - ord("a")))
            else:
                ll, rr = lst[1:]
                ans = tree.range_or(int(ll) - 1, int(rr) - 1)
                ac.st(bin(ans).count("1"))
        return
