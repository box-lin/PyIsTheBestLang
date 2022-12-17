"""

"""
"""
算法：堆（优先队列）
功能：通常用于需要贪心的场景
题目：
P1168 中位数（https://www.luogu.com.cn/problem/P1168） 用两个堆维护中位数
P1801 黑匣子（https://www.luogu.com.cn/problem/P1801）用两个堆维护第K小
P2085 最小函数值（https://www.luogu.com.cn/problem/P2085）用数学加一个堆维护前K小
P1631 序列合并（https://www.luogu.com.cn/problem/P1631）用一个堆维护前K小
P4053 建筑抢修（https://www.luogu.com.cn/problem/P4053）用一个堆延迟选择贪心维护最优
P1878 舞蹈课（https://www.luogu.com.cn/problem/P1878）用哈希加一个堆进行模拟计算

L0630 课程表（https://leetcode.cn/problems/course-schedule-iii/）用一个堆延迟选择贪心维护最优
L2454 下一个更大元素 IV（https://leetcode.cn/problems/next-greater-element-iv/）使用两个堆维护下下个更大元素即出队两次时遇见的元素
L2402 会议室 III（https://leetcode.cn/problems/meeting-rooms-iii/）使用两个堆模拟进行会议室安排并进行计数
L2386 找出数组的第 K 大和（https://leetcode.cn/problems/find-the-k-sum-of-an-array/）转换思路使用堆维护最大和第 K 次出队的则为目标结果
L2163 删除元素后和的最小差值（https://leetcode.cn/problems/minimum-difference-in-sums-after-removal-of-elements/）预处理前缀后缀最大最小的 K 个数和再进行枚举分割点


参考：OI WiKi（xx）
"""

import bisect
import random
import re
import unittest

from typing import List
import heapq
import math
from collections import defaultdict, Counter, deque
from functools import lru_cache
from itertools import combinations
from sortedcontainers import SortedList, SortedDict, SortedSet

from sortedcontainers import SortedDict
from functools import reduce
from operator import xor
from functools import lru_cache

import random
from itertools import permutations, combinations
import numpy as np

from decimal import Decimal

import heapq
import copy


class HeapqMedian:
    def __init__(self, mid):
        # 使用两个堆动态维护奇数长度数组的中位数
        self.mid = mid
        self.left = []
        self.right = []
        return

    def add(self, num):
        # 根据大小先放入左右两边的堆
        if num > self.mid:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)
        n = len(self.left) + len(self.right)

        if n % 2 == 0:
            # 如果是奇数长度则更新中位数并保持左右两边数组长度相等
            if len(self.left) > len(self.right):
                heapq.heappush(self.right, self.mid)
                self.mid = -heapq.heappop(self.left)
            elif len(self.right) > len(self.left):
                heapq.heappush(self.left, -self.mid)
                self.mid = heapq.heappop(self.right)
        return

    def query(self):
        return self.mid


class TestGeneral(unittest.TestCase):

    def test_heapq_median(self):
        ceil = 1000
        num = random.randint(0, ceil)
        lst = SortedList([num])
        hm = HeapqMedian(num)
        for i in range(ceil):
            num = random.randint(0, ceil)
            lst.add(num)
            hm.add(num)
            if i % 2:
                assert lst[(i + 2) // 2] == hm.query()
        return


if __name__ == '__main__':
    unittest.main()
