"""
Algorithm：hash|contribution_method|matrix_hash|tree_hash|string_hash|prefix_hash|suffix_hash|hash_crush
Description：prefix_suffix|counter|index|prefix_sum

====================================LeetCode====================================
2143（https://leetcode.cn/problems/choose-numbers-from-two-arrays-in-range/）prefix_sum|hash|counter
17（https://leetcode.cn/problems/find-longest-subarray-lcci/）prefix_sum|hash
1590（https://leetcode.cn/problems/make-sum-divisible-by-p/）prefix_sum|hash|mod|counter
2588（https://leetcode.cn/problems/count-the-number-of-beautiful-subarrays/）prefix_sum|hash|counter
02（https://leetcode.cn/contest/hhrc2022/problems/0Wx4Pc/）prefix_sum|hash|brain_teaser|greedy
03（https://leetcode.cn/contest/hhrc2022/problems/VAc7h3/）tree_hash
2031（https://leetcode.cn/problems/count-subarrays-with-more-ones-than-zeros/）prefix_sum|hash|counter
2025（https://leetcode.cn/problems/maximum-number-of-ways-to-partition-an-array/description/）hash|contribution_method|counter
895（https://leetcode.cn/problems/maximum-frequency-stack/description/）hash|stack
1658（https://leetcode.cn/problems/minimum-operations-to-reduce-x-to-zero/description/）prefix_sum|hash|brain_teaser|greedy
2227（https://leetcode.cn/problems/encrypt-and-decrypt-strings/）brain_teaser|reverse_thinking

===================================CodeForces===================================
1692H（https://codeforces.com/contest/1692/problem/H）hash|prefix_min

=====================================LuoGu======================================
P2697（https://www.luogu.com.cn/problem/P2697）hash|prefix_sum
P1114（https://www.luogu.com.cn/problem/P1114）hash|prefix_sum
P4889（https://www.luogu.com.cn/problem/P4889）math|hash|counter
P6273（https://www.luogu.com.cn/problem/P6273）hash|prefix|counter
P8630（https://www.luogu.com.cn/problem/P8630）hash|counter|permutation|brute_force

====================================AtCoder=====================================
ARC061B（https://atcoder.jp/contests/abc045/tasks/arc061_b）hash|inclusion_exclusion|counter


=====================================AcWing=====================================

"""
import random
from collections import defaultdict
from itertools import accumulate
from typing import List

from src.utils.fast_io import FastIO


class Solution:
    def __init__(self):
        return

    @staticmethod
    def lc_2143(nums1: List[int], nums2: List[int]) -> int:
        """
        url: https://leetcode.cn/problems/choose-numbers-from-two-arrays-in-range/
        tag: prefix_sum|hash|counter|classical|linear_dp
        """
        n = len(nums1)
        mod = 10 ** 9 + 7
        pre = defaultdict(int)
        pre[-nums1[0]] += 1
        pre[nums2[0]] += 1
        ans = pre[0]
        for i in range(1, n):
            cur = defaultdict(int)
            cur[-nums1[i]] += 1
            cur[nums2[i]] += 1
            for p in pre:
                cur[p - nums1[i]] += pre[p]
                cur[p + nums2[i]] += pre[p]
            ans += cur[0]
            ans %= mod
            pre = cur
        return ans

    @staticmethod
    def lc_1658(nums: List[int], x: int) -> int:
        """
        url: https://leetcode.cn/problems/minimum-operations-to-reduce-x-to-zero/description/
        tag: prefix_sum|hash|brain_teaser|greedy|reverse_thinking
        """
        pre = {0: -1}
        cur = 0
        n = len(nums)
        s = sum(nums)
        ans = -1 if s != x else 0
        for i, w in enumerate(nums):
            cur += w
            if cur - (s - x) in pre and i - pre[cur - (s - x)] > ans:
                ans = i - pre[cur - (s - x)]
            if cur not in pre:
                pre[cur] = i
        return n - ans if ans > -1 else ans

    @staticmethod
    def lc_2025(nums: List[int], k: int) -> int:
        """
        url: https://leetcode.cn/problems/maximum-number-of-ways-to-partition-an-array/description/
        tag: hash|contribution_method|counter
        """
        n = len(nums)
        ans = 0
        pre = list(accumulate(nums, initial=0))
        for i in range(1, n):
            if pre[i] == pre[-1] - pre[i]:
                ans += 1

        cnt = [0] * n
        dct = defaultdict(int)
        for i in range(n - 2, -1, -1):
            b = pre[-1] - pre[i + 1]
            a = pre[i + 1]
            dct[a - b] += 1
            cnt[i] += dct[nums[i] - k]

        dct = defaultdict(int)
        for i in range(1, n):
            b = pre[-1] - pre[i]
            a = pre[i]
            dct[a - b] += 1
            cnt[i] += dct[k - nums[i]]

        return max(ans, max(cnt))

    @staticmethod
    def arc_061b(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc045/tasks/arc061_b
        tag: hash|inclusion_exclusion|counter
        """
        h, w, n = ac.read_list_ints()
        cnt = [0] * 10
        dct = defaultdict(int)
        for _ in range(n):
            a, b = ac.read_list_ints()
            for x in range(3):
                for y in range(3):
                    if 3 <= x + a <= h and 3 <= y + b <= w:
                        dct[(x + a, y + b)] += 1
        for k in dct:
            cnt[dct[k]] += 1

        cnt[0] = (h - 2) * (w - 2) - sum(cnt[1:])
        for a in cnt:
            ac.st(a)
        return

    @staticmethod
    def lg_p4889(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P4889
        tag: math|hash|counter|classical
        """
        n, m = ac.read_list_ints()
        height = ac.read_list_ints()
        cnt = defaultdict(int)
        ans = 0
        for i in range(n):
            ans += cnt[height[i] - i]
            cnt[height[i] - i] += 1

        cnt = defaultdict(int)
        for i in range(n):
            ans += cnt[height[i] + i]
            ans += cnt[i - height[i]]
            cnt[height[i] + i] += 1
        ac.st(ans)
        return

    @staticmethod
    def lg_p6273(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P6273
        tag: hash|prefix|counter|brain_teaser
        """
        ac.read_int()
        s = ac.read_str()
        st = list(set(s))
        ind = {w: i for i, w in enumerate(st)}
        m = len(ind)
        cnt = [0] * m
        pre = defaultdict(int)
        pre[tuple(cnt)] = 1
        ans = 0
        mod = 10 ** 9 + 7
        for w in s:
            if w == st[0]:
                for i in range(m):
                    if i != ind[w]:
                        cnt[i] -= 1
            else:
                cnt[ind[w]] += 1
            tp = tuple(cnt)
            ans += pre[tp]
            pre[tp] += 1
            ans %= mod
        ac.st(ans)
        return

    @staticmethod
    def lc_895():
        """
        url: https://leetcode.cn/problems/maximum-frequency-stack/description/
        tag: hash|stack
        """
        class FreqStack:
            def __init__(self):
                self.freq = defaultdict(list)
                self.dct = defaultdict(int)
                self.ceil = 0

            def push(self, val: int) -> None:
                self.dct[val] += 1
                self.freq[self.dct[val]].append(val)
                if self.dct[val] > self.ceil:
                    self.ceil = self.dct[val]
                return

            def pop(self) -> int:
                val = self.freq[self.ceil].pop()
                self.dct[val] -= 1
                if not self.freq[self.ceil]:
                    self.ceil -= 1
                return val

        FreqStack()
        return
