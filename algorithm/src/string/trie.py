import unittest
from algorithm.src.fast_io import FastIO
from typing import List
from collections import Counter

"""
算法：Trie字典树，也叫前缀树
功能：处理字符串以及结合位运算相关，01Trie通用用于查询位运算极值
题目：

===================================力扣===================================
2416. 字符串的前缀分数和（https://leetcode.cn/problems/sum-of-prefix-scores-of-strings/）单词组前缀计数
1803. 统计异或值在范围内的数对有多少（https://leetcode.cn/problems/count-pairs-with-xor-in-a-range/）经典01Trie，查询异或值在一定范围的数组对
677. 键值映射（https://leetcode.cn/problems/map-sum-pairs/）

===================================洛谷===================================
P8306 字典树（https://www.luogu.com.cn/problem/P8306）
P4551 最长异或路径（https://www.luogu.com.cn/problem/P4551）关键是利用异或的性质，将任意根节点作为中转站
P3864 [USACO1.2]命名那个数字 Name That Number（https://www.luogu.com.cn/problem/P3864）使用哈希枚举或者进行字典树存储
P5755 [NOI2000] 单词查找树（https://www.luogu.com.cn/problem/P5755）字典树节点计数

================================CodeForces================================
Fixed Prefix Permutations（https://codeforces.com/problemset/problem/1792/D）变形后使用字典树进行计数查询
D. Vasiliy's Multiset（https://codeforces.com/problemset/problem/706/D）经典01Trie，增加与删除数字，最大异或值查询


参考：OI WiKi（）
"""


class Node:
    def __init__(self):
        self.data = 0
        self.left = None  # bit为0
        self.right = None  # bit为1
        self.count = 0


class Trie01Node:
    def __init__(self):
        # 使用自定义节点实现
        self.root = Node()
        self.cur = None
        self.n = 31

    def add(self, val):
        self.cur = self.root
        for i in range(self.n, -1, -1):
            v = val & (1 << i)
            if v:
                # 1 走右边
                if not self.cur.right:
                    self.cur.right = Node()
                self.cur = self.cur.right
                self.cur.count += 1
            else:
                # 0 走左边
                if not self.cur.left:
                    self.cur.left = Node()
                self.cur = self.cur.left
                self.cur.count += 1
        self.cur.data = val
        return

    def delete(self, val):
        self.cur = self.root
        for i in range(self.n, -1, -1):
            v = val & (1 << i)
            if v:
                # 1 走右边
                if self.cur.right.count == 1:
                    self.cur.right = None
                    break
                self.cur = self.cur.right
                self.cur.count -= 1
            else:
                # 0 走左边
                if self.cur.left.count == 1:
                    self.cur.left = None
                    break
                self.cur = self.cur.left
                self.cur.count -= 1
        return

    def query(self, val):
        self.cur = self.root
        for i in range(self.n, -1, -1):
            v = val & (1 << i)
            if v:
                # 1 优先走相反方向的左边
                if self.cur.left and self.cur.left.count > 0:
                    self.cur = self.cur.left
                elif self.cur.right and self.cur.right.count > 0:
                    self.cur = self.cur.right
            else:
                # 0 优先走相反方向的右边
                if self.cur.right and self.cur.right.count > 0:
                    self.cur = self.cur.right
                elif self.cur.left and self.cur.left.count > 0:
                    self.cur = self.cur.left
        return val ^ self.cur.data


class Trie01Dict:
    def __init__(self, n):
        # 使用字典数据结构实现
        self.dct = dict()
        # 确定序列长度
        self.n = n
        return

    def update(self, num, cnt):
        cur = self.dct
        for i in range(self.n, -1, -1):
            # 更新当前哈希下的数字个数
            cur["cnt"] = cur.get("cnt", 0) + cnt
            # 哈希的键
            w = 1 if num & (1 << i) else 0
            if w not in cur:
                cur[w] = dict()
            cur = cur[w]
        cur["cnt"] = cur.get("cnt", 0) + cnt
        return

    def query(self, num, ceil):

        def dfs(xor, cur, i):
            # 前缀异或和，当前哈希树，以及剩余序列所处的位数
            nonlocal res
            # 超出范围剪枝
            if xor > ceil:
                return
            # 搜索完毕剪枝
            if i == -1:
                res += cur["cnt"]
                return
            # 最大值也不超出范围剪枝
            if xor + (1 << (i + 2) - 1) <= ceil:
                res += cur["cnt"]
                return
            # 当前哈希的键
            w = 1 if num & (1 << i) else 0
            if 1 - w in cur:
                dfs(xor | (1 << i), cur[1 - w], i - 1)
            if w in cur:
                dfs(xor, cur[w], i - 1)
            return

        # 使用深搜查询异或值不超出范围的数对个数
        res = 0
        dfs(0, self.dct, self.n)
        return res


class Solution:
    def __int__(self):
        return

    @staticmethod
    def lc_1803(nums: List[int], low: int, high: int) -> int:

        count = Counter(nums)

        # 确定二进制序列的长度
        big = max(nums)
        n = 0
        while (1 << (n + 1)) - 1 < big:
            n += 1
        trie = Trie01Dict(n)
        trie.update(0, 0)
        # 滚动更新字典树同时查询符合条件的数对个数
        ans = 0
        for num in count:
            ans += count[num]*(trie.query(num, high) - trie.query(num, low - 1))
            trie.update(num, count[num])
        return ans

    @staticmethod
    def cf_706d(ac=FastIO()):
        q = ac.read_int()
        trie = Trie01Node()
        trie.add(0)
        for _ in range(q):
            op, x = ac.read_list_strs()
            if op == "+":
                trie.add(int(x))
            elif op == "-":
                trie.delete(int(x))
            else:
                ac.st(trie.query(int(x)))
        return


class TriePrefixKeyValue:
    # L677
    def __init__(self):
        self.dct = dict()
        return

    def update(self, word, val):
        # 更新单词与前缀计数
        cur = self.dct
        for w in word:
            if w not in cur:
                cur[w] = dict()
            cur = cur[w]
        cur["val"] = val
        return

    def query(self, word):
        # 查询前缀单词个数
        cur = self.dct
        for w in word:
            if w not in cur:
                return 0
            cur = cur[w]

        def dfs(dct):
            nonlocal res
            if "val" in dct:
                res += dct["val"]
            for s in dct:
                if s != "val":
                    dfs(dct[s])
            return
        res = 0
        dfs(cur)
        return res


class TrieCount:
    def __init__(self):
        self.dct = dict()
        return

    def update(self, word):
        # 更新单词与前缀计数
        cur = self.dct
        for w in word:
            if w not in cur:
                cur[w] = dict()
            cur = cur[w]
            cur["cnt"] = cur.get("cnt", 0) + 1
        return

    def query(self, word):
        # 查询前缀单词个数
        cur = self.dct
        for w in word:
            if w not in cur:
                return 0
            cur = cur[w]
        return cur["cnt"]


class TrieBit:
    def __init__(self):
        self.dct = dict()
        self.n = 32
        return

    def update(self, num):
        cur = self.dct
        for i in range(self.n, -1, -1):
            w = 1 if num & (1 << i) else 0
            if w not in cur:
                cur[w] = dict()
            cur = cur[w]
            cur["cnt"] = cur.get("cnt", 0) + 1
        return

    def query(self, num):
        cur = self.dct
        ans = 0
        for i in range(self.n, -1, -1):
            w = 1 if num & (1 << i) else 0
            if 1 - w in cur:
                cur = cur[1 - w]
                ans += 1 << i
            else:
                cur = cur[w]
        return ans

    def delete(self, num):
        cur = self.dct
        for i in range(self.n, -1, -1):
            w = num & (1 << i)
            if cur[w].get("cnt", 0) == 1:
                del cur[w]
                break
            cur = cur[w]
            cur["cnt"] -= 1
        return


class TestGeneral(unittest.TestCase):

    def test_trie_count(self):
        tc = TrieCount()
        words = ["happy", "hello", "leetcode", "let"]
        for word in words:
            tc.update(word)
        assert tc.query("h") == 2
        assert tc.query("le") == 2
        assert tc.query("lt") == 0
        return


if __name__ == '__main__':
    unittest.main()
