"""
Algorithm：block_query|offline_query|sort|two_pointers
Description：sort the query interval into blocks and alternate between moving two pointers dynamically maintain query values

====================================LeetCode====================================
1157（https://leetcode.cn/problems/online-majority-element-in-subarray/description/）range_super_mode|CF1514D|random_guess|binary_search|bit_operation|segment_tree

=====================================LuoGu======================================
P3396（https://www.luogu.com.cn/problem/P3396）sqrt_decomposition
P3765（https://www.luogu.com.cn/problem/P3765）range_super_mode
P3567（https://www.luogu.com.cn/problem/P3567）range_super_mode

===================================CodeForces===================================
220B（https://codeforces.com/contest/220/problem/B）block_query|counter
86D（https://codeforces.com/contest/86/problem/D）block_query|math
617E（https://codeforces.com/contest/617/problem/E）block_query|xor_pair|counter
1514D（https://codeforces.com/contest/1514/problem/D）range_super_mode|random_guess|binary_search|bit_operation|segment_tree
1468M（https://codeforces.com/problemset/problem/1468/M）sqrt_decomposition
1207F（https://codeforces.com/problemset/problem/1207/F）sqrt_decomposition
797E（https://codeforces.com/problemset/problem/797/E）sqrt_decomposition
677D（https://codeforces.com/contest/677/problem/D）sqrt_decomposition
425D（https://codeforces.com/problemset/problem/425/D）sqrt_decomposition
1921F（https://codeforces.com/contest/1921/problem/F）sqrt_decomposition
103D（https://codeforces.com/contest/103/problem/D）sqrt_decomposition
1806E（https://codeforces.com/problemset/problem/1806/E）sqrt_decomposition

====================================AtCoder=====================================
ABC132F（https://atcoder.jp/contests/abc132/tasks/abc132_f）block_query|counter|dp|prefix_sum


"""
import bisect
from collections import defaultdict, Counter
from itertools import accumulate
from operator import xor
from typing import List

from src.data_structure.segment_tree.template import PointSetMergeRangeMode, PointSetBitRangeMode, \
    PointSetRandomRangeMode
from src.data_structure.sqrt_decomposition.template import BlockSize
from src.utils.fast_io import FastIO, inf


class Solution:
    def __init__(self):
        return

    @staticmethod
    def abc_132f(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc132/tasks/abc132_f
        tag: block_query|counter|dp|prefix_sum
        """
        mod = 10 ** 9 + 7
        n, k = ac.read_list_ints()
        cnt, _ = BlockSize().get_divisor_split(n)
        m = len(cnt)
        dp = cnt[:]
        for _ in range(k - 1):
            pre = list(ac.accumulate(dp)[1:])[::-1]
            dp = [(cnt[i] * pre[i]) % mod for i in range(m)]
        ac.st(sum(dp) % mod)
        return

    @staticmethod
    def cf1514_d(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1514/problem/D
        tag: range_super_mode|random_guess|binary_search|bit_operation|segment_tree
        """
        n, m = ac.read_list_ints()
        nums = ac.read_list_ints()
        cnt = [0] * (n + 1)
        freq = [0] * (n + 1)
        size = int(n ** 0.5) + 500

        queries = [[] for _ in range(size)]

        for i in range(m):
            a, b = ac.read_list_ints_minus_one()
            queries[b // size].append([a, b, i])

        def update(num, p):
            nonlocal cnt, ceil
            if p == 1:
                cnt[num] += 1
                freq[cnt[num] - 1] -= 1
                freq[cnt[num]] += 1
                if cnt[num] > ceil:
                    ceil = cnt[num]
            else:
                cnt[num] += -1
                freq[cnt[num] + 1] -= 1
                freq[cnt[num]] += 1
                if not freq[cnt[num] + 1] and ceil == cnt[num] + 1:
                    ceil = cnt[num]
            return

        ans = [0] * m
        x = y = 0
        cnt[nums[0]] = 1
        freq[1] = 1
        ceil = 1
        for i in range(size):
            if i % 2:
                queries[i].sort(key=lambda it: -it[0])
            else:
                queries[i].sort(key=lambda it: it[0])
            for a, b, j in queries[i]:
                while y > b:
                    update(nums[y], -1)
                    y -= 1
                while y < b:
                    y += 1
                    update(nums[y], 1)
                while x > a:
                    x -= 1
                    update(nums[x], 1)
                while x < a:
                    update(nums[x], -1)
                    x += 1
                if ceil * 2 <= b - a + 1:
                    ans[j] = 1
                else:
                    ans[j] = ceil - (b - a + 1 - ceil + 1) + 1
        for a in ans:
            ac.st(a)
        return

    @staticmethod
    def cf1514_d_2(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1514/problem/D
        tag: range_super_mode|random_guess|binary_search|bit_operation|segment_tree|random_seed
        """
        n, m = ac.read_list_ints()
        nums = ac.read_list_ints()
        ind = [[] for _ in range(1 << 20)]
        cnt = [0] * 20
        pre = [cnt[:]]
        for i, num in enumerate(nums):
            ind[num].append(i)
            for j in range(20):
                if num & (1 << j):
                    cnt[j] += 1
            pre.append(cnt[:])
        for _ in range(m):
            x, y = ac.read_list_ints_minus_one()
            num = 0
            length = y - x + 1
            for j in range(20):
                if pre[y + 1][j] - pre[x][j] >= length / 2:
                    num |= 1 << j

            ceil = bisect.bisect_right(ind[num], y) - bisect.bisect_left(ind[num], x)
            if ceil * 2 <= length:
                ac.st(1)
            else:
                ac.st(ceil - (length - ceil + 1) + 1)
        return

    @staticmethod
    def cf1514_d_3(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1514/problem/D
        tag: range_super_mode|random_guess|binary_search|bit_operation|segment_tree|random_seed
        """
        n, m = ac.read_list_ints()
        nums = ac.read_list_ints()
        ds = PointSetBitRangeMode(nums, 20)
        ds = PointSetRandomRangeMode(nums)
        ds = PointSetMergeRangeMode(nums)
        for _ in range(m):
            ll, rr = ac.read_list_ints_minus_one()
            length = rr - ll + 1
            ans = ds.range_mode(ll, rr, (length + 1) // 2)
            if ans == -1:
                ac.st(1)
                continue
            cnt = ds.dct[ans].bisect_right(rr) - ds.dct[ans].bisect_left(ll)
            ac.st(length - ((length - cnt) * 2 + 1) + 1)
        return

    @staticmethod
    def cf_220b(ac=FastIO()):
        """
        url: https://codeforces.com/contest/220/problem/B
        tag: block_query|counter|sqrt_decomposition|offline_query|classical
        """
        n, m = ac.read_list_ints()
        nums = ac.read_list_ints()
        size = int(n ** 0.5) + 1

        queries = [[] for _ in range(size)]
        for i in range(m):
            a, b = ac.read_list_ints_minus_one()
            queries[b // size].append([a, b, i])

        def update(num, p):
            nonlocal cur, cnt
            if num == cnt[num]:
                cur -= 1
            cnt[num] += p
            if num == cnt[num]:
                cur += 1
            return

        cur = 0
        ans = [0] * m
        x = y = 0
        cnt = defaultdict(int)
        cnt[nums[0]] = 1
        if nums[0] == 1:
            cur += 1
        for i in range(size):
            if i % 2:
                queries[i].sort(key=lambda it: -it[0])
            else:
                queries[i].sort(key=lambda it: it[0])
            for a, b, j in queries[i]:
                while y > b:
                    update(nums[y], -1)
                    y -= 1
                while y < b:
                    y += 1
                    update(nums[y], 1)
                while x > a:
                    x -= 1
                    update(nums[x], 1)
                while x < a:
                    update(nums[x], -1)
                    x += 1
                ans[j] = cur
        for a in ans:
            ac.st(a)
        return

    @staticmethod
    def cf_86d(ac=FastIO()):
        """
        url: https://codeforces.com/contest/86/problem/D
        tag: sqrt_decomposition|offline_query|math
        """
        n, t = ac.read_list_ints()
        nums = ac.read_list_ints()
        size = int(n ** 0.5) + 1

        queries = [[] for _ in range(t)]
        for i in range(t):
            a, b = ac.read_list_ints_minus_one()
            queries[b // size].append([a, b, i])

        def update(p, z):
            nonlocal cur
            num = nums[p]
            cur -= cnt[num] * cnt[num] * num
            cnt[num] += z
            cur += cnt[num] * cnt[num] * num
            return

        cnt = [0] * (10 ** 6 + 1)
        x = y = 0
        ans = [0] * t
        cnt = Counter()
        cur = nums[0]
        cnt[nums[0]] = 1
        for i in range(size):
            if i % 2:
                queries[i].sort(key=lambda it: -it[0])
            else:
                queries[i].sort(key=lambda it: it[0])

            for a, b, j in queries[i]:
                while y > b:
                    update(y, -1)
                    y -= 1
                while y < b:
                    y += 1
                    update(y, 1)

                while x > a:
                    x -= 1
                    update(x, 1)
                while x < a:
                    update(x, -1)
                    x += 1
                ans[j] = cur
        for a in ans:
            ac.st(a)
        return

    @staticmethod
    def cf_617e(ac=FastIO()):
        """
        url: https://codeforces.com/contest/617/problem/E
        tag: sqrt_decomposition|offline_query|xor_pair|counter
        """
        n, m, k = ac.read_list_ints()
        nums = ac.read_list_ints()
        pre = list(accumulate(nums, xor, initial=0))

        size = int(n ** 0.5) + 1
        queries = [[] for _ in range(size)]
        for i in range(m):
            a, b = ac.read_list_ints()
            queries[b // size].append([a, b, i])

        def update(num, p):
            nonlocal cur
            if p == 1:
                cur += dct[num ^ k]
                dct[num] += 1
            else:
                dct[num] -= 1
                cur -= dct[num ^ k]
            return

        dct = [0] * (2 * 10 ** 6 + 1)
        x = y = 0
        ans = [0] * m
        dct[pre[0]] += 1
        cur = 0
        for i in range(size):
            if i % 2:
                queries[i].sort(key=lambda it: -it[0])
            else:
                queries[i].sort(key=lambda it: it[0])
            for a, b, j in queries[i]:
                a -= 1
                while y > b:
                    update(pre[y], -1)
                    y -= 1
                while y < b:
                    y += 1
                    update(pre[y], 1)
                while x > a:
                    x -= 1
                    update(pre[x], 1)
                while x < a:
                    update(pre[x], -1)
                    x += 1
                ans[j] = cur
        for a in ans:
            ac.st(a)
        return

    @staticmethod
    def cf_1806e(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/1806/E
        tag: sqrt_decomposition
        """
        n, q = ac.read_list_ints()
        nums = ac.read_list_ints()
        parent = [-1] + ac.read_list_ints_minus_one()
        fxx = [0] * n
        depth = [0] * n
        cnt = [0] * n
        for i in range(n):
            fxx[i] += nums[i] * nums[i]
            if i:
                fxx[i] += fxx[parent[i]]
                depth[i] = depth[parent[i]] + 1
            cnt[depth[i]] += 1

        size = 100
        dct = dict()
        for _ in range(q):
            x, y = ac.read_list_ints_minus_one()
            if x > y:
                y, x = x, y
            stack = [(x, y)]
            while x != y and x * n + y not in dct:
                x, y = parent[x], parent[y]
                stack.append((x, y))
            m = len(stack)
            val = dct[x * n + y] if x != y else fxx[x]
            if x != y and cnt[depth[x]] <= size:
                dct[x * n + y] = val
            for i in range(m - 2, -1, -1):
                x, y = stack[i]
                val += nums[x] * nums[y]
                if cnt[depth[x]] <= size:
                    dct[x * n + y] = val
            ac.st(val)
        return

    @staticmethod
    def lg_p3396(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P3396
        tag: sqrt_decomposition
        """
        n, q = ac.read_list_ints()
        nums = ac.read_list_ints()
        size = ac.min(n - 1, 10 ** 7 // n)  # 100
        pre = [[]]
        for p in range(1, size + 1):
            lst = [0] * p
            for i in range(n):
                lst[(i + 1) % p] += nums[i]
            pre.append(lst[:])
        for _ in range(q):
            lst = ac.read_list_strs()
            if lst[0] == "A":
                x, y = [int(w) for w in lst[1:]]
                if x <= size:
                    ac.st(pre[x][y])
                else:
                    w = y if y else x
                    ans = 0
                    while w <= n:
                        ans += nums[w - 1]
                        w += x
                    ac.st(ans)
            else:
                x, y = [int(w) for w in lst[1:]]
                num = nums[x - 1]
                nums[x - 1] = y
                for p in range(1, size + 1):
                    pre[p][x % p] -= num
                    pre[p][x % p] += y
        return

    @staticmethod
    def cf_103d(ac=FastIO()):
        """
        url: https://codeforces.com/contest/103/problem/D
        tag: sqrt_decomposition
        """
        n = ac.read_int()
        nums = ac.read_list_ints()
        size = ac.min(n, 100)
        q = ac.read_int()
        queries = [ac.read_list_ints() for _ in range(q)]
        ind = [[] for _ in range(size + 1)]
        for i in range(q):
            t, k = queries[i]
            if k <= size:
                ind[k].append(i)
        ans = [-1] * q
        for k in range(1, size + 1):
            if ind[k]:
                cur = [0] * (n + 1)
                for i in range(n):
                    cur[i + 1] = cur[ac.max(0, i - k + 1)] + nums[i]
                for x in ind[k]:
                    t, k = queries[x]
                    xx = (n - t) // k + 1
                    s = t - 1
                    end = s + (xx - 1) * k
                    ans[x] = cur[end + 1] - cur[ac.max(s - k + 1, 0)]
        for i in range(q):
            t, k = queries[i]
            if k > size:
                t -= 1
                res = 0
                for x in range(t, n, k):
                    res += nums[x]
                ac.st(res)
            else:
                ac.st(ans[i])
        return

    @staticmethod
    def cf_1921(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1921/problem/F
        tag: sqrt_decomposition
        """

        def ind_to_rk(ii, kk):
            return ii // kk + 1

        for _ in range(ac.read_int()):
            n, q = ac.read_list_ints()
            nums = ac.read_list_ints()
            size = ac.min(n, 150)
            queries = [ac.read_list_ints() for _ in range(q)]
            ind = [[] for _ in range(size + 1)]
            for i in range(q):
                s, k, c = queries[i]
                if k <= size:
                    ind[k].append(i)
            ans = [-1] * q
            for k in range(1, size + 1):
                if ind[k]:
                    cur = [0] * (n + 1)
                    pre = [0] * (n + 1)
                    for i in range(n):
                        r = ind_to_rk(i, k)
                        cur[i + 1] = cur[ac.max(i - k + 1, 0)] + nums[i] * r
                        pre[i + 1] = pre[ac.max(i - k + 1, 0)] + nums[i]
                    for x in ind[k]:
                        s, k, c = queries[x]
                        s -= 1
                        e = s + (c - 1) * k
                        length = c * k
                        res = cur[e + 1] - cur[ac.max(e + 1 - length, 0)]
                        res -= (s // k) * (pre[e + 1] - pre[ac.max(e + 1 - length, 0)])
                        ans[x] = res
                    del cur

            for i in range(q):
                s, k, c = queries[i]
                if k > size:
                    s -= 1
                    res = 0
                    for x in range(s, s + k * c - 1, k):
                        res += nums[x] * (((x + 1) - s) // k + 1)
                    ans[i] = res
            ac.lst(ans)
        return

    @staticmethod
    def cf_425d(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/425/D
        tag: sqrt_decomposition
        """
        n = ac.read_int()
        dct = dict()
        for _ in range(n):
            a, b = ac.read_list_ints()
            if a not in dct:
                dct[a] = set()
            dct[a].add(b)

        ans = 0
        size = int(n ** 0.5) + 1
        res = []
        for a in sorted(dct):
            if len(dct[a]) <= size:
                lst = sorted(list(dct[a]))
                m = len(lst)
                for i in range(m):
                    x = lst[i]
                    for j in range(i + 1, m):
                        y = lst[j]
                        length = y - x
                        for z in [a - length, a + length]:
                            if z in dct and len(dct[z]) > size:
                                if x in dct[z] and y in dct[z]:
                                    ans += 1
                        z = a + length
                        if z in dct and len(dct[z]) <= size and x in dct[z] and y in dct[z]:
                            ans += 1

            else:
                res.append(a)
        m = len(res)
        for i in range(m):
            x = res[i]
            for j in range(i + 1, m):
                y = res[j]
                length = y - x
                for z in sorted(dct[x]):
                    if z + length in dct[x] and z + length in dct[y] and z in dct[y]:
                        ans += 1
        ac.st(ans)
        return

    @staticmethod
    def cf_677d(ac=FastIO()):
        """
        url: https://codeforces.com/contest/677/problem/D
        tag: sqrt_decomposition
        """
        m, n, p = ac.read_list_ints()
        grid = [ac.read_list_ints() for _ in range(m)]
        dct = [[] for _ in range(p + 1)]
        for i in range(m):
            for j in range(n):
                dct[grid[i][j]].append(i * n + j)
        pre = defaultdict(lambda: inf)
        for x in dct[1]:
            i, j = x // n, x % n
            if i == j == 0:
                pre[x] = 0
            else:
                pre[x] = i + j
        dis = [m * n + 1] * n * m
        for y in range(2, p + 1):
            m1 = len(dct[y - 1])
            m2 = len(dct[y])
            if m1 * m2 < m * n:
                cur = defaultdict(lambda: inf)
                for x in pre:
                    i1, j1 = x // n, x % n
                    for yy in dct[y]:
                        i2, j2 = yy // n, yy % n
                        cur[yy] = ac.min(cur[yy], pre[x] + abs(i2 - i1) + abs(j2 - j1))
            else:
                for i in range(m * n):
                    dis[i] = m * n + 1
                nodes = [[] for _ in range(m * n + 1)]
                for x in pre:
                    nodes[pre[x]].append(x)
                    dis[x] = pre[x]

                for d in range(m * n + 1):
                    for x in nodes[d]:
                        i, j = x // n, x % n
                        if dis[x] < d:
                            continue
                        for a, b in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                            if 0 <= a < m and 0 <= b < n and dis[a * n + b] > d + 1:
                                dis[a * n + b] = d + 1
                                nodes[d + 1].append(a * n + b)
                cur = defaultdict(lambda: inf)
                for x in dct[y]:
                    cur[x] = dis[x]
            pre = cur
        ac.st(min(pre.values()))
        return

    @staticmethod
    def cf_797e(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/797/E
        tag: sqrt_decomposition
        """
        n = ac.read_int()
        nums = ac.read_list_ints()
        q = ac.read_int()
        queries = [ac.read_list_ints() for _ in range(q)]
        dct = [[] for _ in range(n + 1)]
        ans = [0] * q
        for i in range(q):
            _, k = queries[i]
            dct[k].append(i)
        size = int(n ** 0.5) + 1
        for k in range(1, n + 1):
            if k <= size:
                dp = [0] * (n + 1)
                for i in range(n - 1, -1, -1):
                    dp[i] = dp[ac.min(n, i + nums[i] + k)] + 1
                for i in dct[k]:
                    ans[i] = dp[queries[i][0] - 1]
            else:
                break
        for i in range(q):
            if ans[i] == 0:
                p, k = queries[i]
                p -= 1
                res = 0
                while p < n:
                    res += 1
                    p += nums[p] + k
                ans[i] = res
        for a in ans:
            ac.st(a)
        return

    @staticmethod
    def cf_1207f(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/1207/F
        tag: sqrt_decomposition
        """
        n = 5 * 10 ** 5
        q = ac.read_int()
        nums = [0] * n
        size = 400
        pre = [0] * (size + 1) * (size + 1)
        for _ in range(q):
            op, x, y = ac.read_list_ints()
            if op == 2:
                if x <= size:
                    ac.st(pre[x * (size + 1) + y])
                else:
                    w = y if y else x
                    ans = 0
                    while w <= n:
                        ans += nums[w - 1]
                        w += x
                    ac.st(ans)
            else:
                nums[x - 1] += y
                for p in range(1, size + 1):
                    pre[p * (size + 1) + x % p] += y
        return

    @staticmethod
    def cf_1468m(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/1468/M
        tag: sqrt_decomposition
        """
        for _ in range(ac.read_int()):

            def check():
                nums = [ac.read_list_ints() for _ in range(ac.read_int())]
                nodes = []
                for ls in nums:
                    nodes.extend(ls[1:])
                n = sum(ls[0] for ls in nums)
                size = int(n ** 0.5) + 1
                nodes = sorted(set(nodes))
                ind = {num: i for i, num in enumerate(nodes)}
                nums = [[ind[x] for x in ls[1:]] for ls in nums]
                length = len(nums)
                res = []
                dct = dict()
                for i in range(length):
                    if len(nums[i]) > size:
                        res.append(i)
                    lst = sorted(nums[i])
                    m = len(lst)
                    for j in range(m):
                        for k in range(j + 1, m):
                            x, y = lst[j], lst[k]
                            if x * n + y in dct:
                                ac.lst([dct[x * n + y] + 1, i + 1])
                                return
                            dct[x * n + y] = i
                m = len(res)
                for i in range(m):
                    x = res[i]
                    pre = set(nums[x])
                    for j in range(i + 1, m):
                        y = res[j]
                        cnt = 0
                        for num in nums[y]:
                            if num in pre:
                                cnt += 1
                        if cnt >= 2:
                            ac.lst([x + 1, y + 1])
                            return

                ac.st(-1)
                return

            check()

        return

    @staticmethod
    def lc_1157():
        """
        url: https://leetcode.cn/problems/online-majority-element-in-subarray
        tag: range_super_mode|point_set
        """

        class MajorityChecker:

            def __init__(self, arr: List[int]):
                self.ds = PointSetMergeRangeMode(arr)
                self.ds = PointSetBitRangeMode(arr, 20)
                self.ds = PointSetRandomRangeMode(arr)

            def query(self, left: int, right: int, threshold: int) -> int:
                return self.ds.range_mode(left, right, threshold - 1)

        return MajorityChecker

    @staticmethod
    def lg_p3567(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P3567
        tag: range_super_mode
        """
        n, m = ac.read_list_ints()
        nums = ac.read_list_ints()
        ds = PointSetBitRangeMode(nums, 20)
        ds = PointSetRandomRangeMode(nums)
        ds = PointSetMergeRangeMode(nums)
        for _ in range(m):
            ll, rr = ac.read_list_ints_minus_one()
            ans = ds.range_mode(ll, rr)
            ac.st(ans if ans > -1 else 0)
        return

    @staticmethod
    def lg_p3765(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P3765
        tag: range_super_mode
        """
        n, m = ac.read_list_ints()
        nums = ac.read_list_ints()
        ds = PointSetBitRangeMode(nums, 20)
        ds = PointSetRandomRangeMode(nums)
        ds = PointSetMergeRangeMode(nums)
        for _ in range(m):
            lst = ac.read_list_ints()
            ll, rr = lst[0] - 1, lst[1] - 1
            winner = ds.range_mode(ll, rr)
            if winner == -1:
                winner = lst[2]
            ac.st(winner)
            for x in lst[4:]:
                ds.point_set(x - 1, winner)
        ac.st(ds.range_mode(0, n - 1))
        return
