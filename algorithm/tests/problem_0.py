import copy
import random
import heapq
import math
import sys
import bisect
import datetime
from functools import lru_cache
from collections import deque
from collections import Counter
from collections import defaultdict
from itertools import combinations
from itertools import permutations
from types import GeneratorType
from functools import cmp_to_key
inf = float("inf")
sys.setrecursionlimit(10000000)


class FastIO:
    def __init__(self):
        return

    @staticmethod
    def _read():
        return sys.stdin.readline().strip()

    def read_int(self):
        return int(self._read())

    def read_float(self):
        return int(self._read())

    def read_ints(self):
        return map(int, self._read().split())

    def read_floats(self):
        return map(float, self._read().split())

    def read_ints_minus_one(self):
        return map(lambda x: int(x) - 1, self._read().split())

    def read_list_ints(self):
        return list(map(int, self._read().split()))

    def read_list_floats(self):
        return list(map(float, self._read().split()))

    def read_list_ints_minus_one(self):
        return list(map(lambda x: int(x) - 1, self._read().split()))

    def read_str(self):
        return self._read()

    def read_list_strs(self):
        return self._read().split()

    def read_list_str(self):
        return list(self._read())

    @staticmethod
    def st(x):
        return sys.stdout.write(str(x) + '\n')

    @staticmethod
    def lst(x):
        return sys.stdout.write(" ".join(str(w) for w in x) + '\n')

    @staticmethod
    def round_5(f):
        res = int(f)
        if f - res >= 0.5:
            res += 1
        return res

    @staticmethod
    def bootstrap(f, stack=[]):
        def wrappedfunc(*args, **kwargs):
            if stack:
                return f(*args, **kwargs)
            else:
                to = f(*args, **kwargs)
                while True:
                    if isinstance(to, GeneratorType):
                        stack.append(to)
                        to = next(to)
                    else:
                        stack.pop()
                        if not stack:
                            break
                        to = stack[-1].send(to)
                return to
        return wrappedfunc


def main(ac=FastIO()):
    n = ac.read_int()
    nums = [ac.read_list_ints() for _ in range(n)]
    m, r = ac.read_ints()
    pre = {(0, 0, 0): 1}
    dp = [[[0, 0] for _ in range(r+1)] for _ in range(m+1)]
    for rmb, rp, time in nums:
        for i in range(m, rmb-1, -1):
            for j in range(r, rp-1, -1):
                tm, cost = dp[i-rmb][j-rp]
                cur = [tm+1, cost+time]
                pre = dp[i][j]
                if cur[0] > pre[0] or (cur[0] == pre[0] and cur[1] < pre[1]):
                    dp[i][j] = cur[:]

    cur = [0, 0]
    for i in range(m+1):
        for j in range(r+1):
            pre = dp[i][j]
            if cur[0] < pre[0] or (cur[0] == pre[0] and cur[1] > pre[1]):
                cur = pre
    ac.st(cur[-1])
    return


main()
