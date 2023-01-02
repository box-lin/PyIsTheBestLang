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

    def read_strs(self):
        return self._read().split()

    def read_list_str(self):
        return self._read().split()

    @staticmethod
    def st(x):
        return sys.stdout.write(str(x) + '\n')

    @staticmethod
    def lst(x):
        return sys.stdout.write(" ".join(str(w) for w in x) + '\n')

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


def get_k_bin_of_n(n, k):
    # 整数n的k进制计算（支持正数进制与负数进制）
    if n == 0:
        return [0]
    if k == 0:
        return []
    # 支持正负数
    pos = 1 if k > 0 else -1
    k = abs(k)
    lst = []
    while n:
        lst.append(n % k)
        n //= k
        n *= pos
    lst.reverse()
    return lst


def main(ac=FastIO()):
    st = "0123456789" + "".join(chr(i+ord("A")) for i in range(26))

    def check(num):
        cur = get_k_bin_of_n(num, n)
        return "".join(st[i] for i in cur)

    n = ac.read_int()
    for i in range(1, n):
        lst = []
        for j in range(1, i+1):
            x = check(i)
            y = check(j)
            z = check(i*j)
            lst.append(f"{x}*{y}={z}")
        ac.lst(lst)
    return


main()
