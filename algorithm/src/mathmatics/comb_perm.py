"""

"""
"""
算法：数学排列组合计数
功能：全排列计数，选取comb计数，隔板法
题目：
L2338 统计理想数组的数目（https://leetcode.cn/problems/count-the-number-of-ideal-arrays/）枚举可行的元素组合序列使用隔板法进行计数

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


from itertools import combinations


class CombPerm:
    def __init__(self):
        return

    @staticmethod
    def combination(n, k):
        return combinations(list(range(n)), k)


class TestGeneral(unittest.TestCase):

    def test_combination(self):
        print([item for item in combination(4, 2)])
        return


if __name__ == '__main__':
    unittest.main()
