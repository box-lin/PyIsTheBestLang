"""
Algorithm：kmp
Description：string|prefix_suffix

====================================LeetCode====================================
214（https://leetcode.com/problems/shortest-palindrome/）longest_palindrome_prefix
796（https://leetcode.com/problems/rotate-string/）rotate_string
25（https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/）find|kmp|substring
1392（https://leetcode.com/problems/longest-happy-prefix/）longest_prefix_suffix|kmp|z_function|template
2223（https://leetcode.com/problems/longest-happy-prefix/）z_function
6918（https://leetcode.com/problems/shortest-string-that-contains-three-strings/）kmp|prefix_suffix|greedy|brain_teaser
2851（https://leetcode.com/problems/string-transformation/description/）kmp|matrix_fast_power|string_hash

=====================================LuoGu======================================
3375（https://www.luogu.com.cn/problem/P3375）longest_prefix_suffix|find
4391（https://www.luogu.com.cn/problem/P4391）brain_teaser|kmp|n-pi[n-1]

===================================CodeForces===================================
1326D2（https://codeforces.com/problemset/problem/1326/D2）manacher|greedy|prefix_suffix|longest_prefix_suffix|palindrome_substring
432D（https://codeforces.com/contest/432/problem/D）kmp|z_function
25E（https://codeforces.com/contest/25/problem/E）kmp|prefix_suffix|greedy|longest_common_prefix_suffix

=====================================AcWing=====================================

141（https://www.acwing.com/problem/content/143/）kmp|circular_section
160（https://www.acwing.com/problem/content/162/）z_function|template
3823（https://www.acwing.com/problem/content/3826/）kmp|z_function


"""

from collections import Counter
from itertools import permutations

from src.mathmatics.fast_power.template import MatrixFastPower
from src.strings.kmp.template import KMP
from src.utils.fast_io import FastIO


class Solution:
    def __init__(self):
        return

    @staticmethod
    def lg_p3375(ac=FastIO()):
        # KMP字符串匹配
        s1 = ac.read_str()
        s2 = ac.read_str()
        m, n = len(s1), len(s2)
        pi = KMP().prefix_function(s2 + "@" + s1)
        for i in range(n, m + n + 1):
            if pi[i] == n:
                ac.st(i - n + 1 - n)
        ac.lst(pi[:n])
        return

    @staticmethod
    def cf_1326d2(ac=FastIO()):
        #  KMP 最长回文前缀与后缀
        for _ in range(ac.read_int()):
            s = ac.read_str()
            n = len(s)
            i, j = 0, n - 1
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    break
            if i >= j:
                ac.st(s)
                continue

            mid = s[i:j + 1]
            a = KMP().find_longest_palindrome(s)
            s1 = mid[:a]

            a = KMP().find_longest_palindrome(s, "suffix")
            s2 = mid[-a:]
            if len(s1) > len(s2):
                ac.st(s[:i] + s1 + s[j + 1:])
            else:
                ac.st(s[:i] + s2 + s[j + 1:])
        return

    @staticmethod
    def lc_214(s: str) -> str:
        """
        url: https://leetcode.com/problems/shortest-palindrome/
        tag: longest_palindrome_prefix
        """
        #  KMP 最长回文前缀
        k = KMP().find_longest_palindrome(s)
        return s[k:][::-1] + s

    @staticmethod
    def lc_796(s: str, goal: str) -> bool:
        """
        url: https://leetcode.com/problems/rotate-string/
        tag: rotate_string
        """
        ans = KMP().find(s + s, goal)
        return len(ans) > 0 and len(s) == len(goal)

    @staticmethod
    def lc_28(haystack: str, needle: str) -> int:
        ans = KMP().find(haystack, needle)
        return ans[0] if ans else -1

    @staticmethod
    def lc_1392(s: str) -> str:
        """
        url: https://leetcode.com/problems/longest-happy-prefix/
        tag: longest_prefix_suffix|kmp|z_function|template
        """
        # 字符串的最长非空真前缀（同时也是非空真后缀）
        lst = KMP().prefix_function(s)
        return s[:lst[-1]]

    @staticmethod
    def lc_2223(s: str) -> int:
        """
        url: https://leetcode.com/problems/longest-happy-prefix/
        tag: z_function
        """
        # z 函数最长公共前缀
        ans = sum(KMP().z_function(s)) + len(s)
        return ans

    @staticmethod
    def lg_p4391(ac=FastIO()):
        # 最小的循环子串使得其不断重复包含给定字符串
        n = ac.read_int()
        s = ac.read_str()
        pi = KMP().prefix_function(s)
        ac.st(n - pi[-1])
        return

    @staticmethod
    def cf_432d(ac=FastIO()):
        # z函数与kmp算法共同，并reverse_order|counter
        s = ac.read_str()

        n = len(s)
        z = KMP().z_function(s)
        z[0] = n
        ans = []
        for i in range(n - 1, -1, -1):
            if z[i] == n - i:
                ans.append([n - i, 0])
        z.sort()

        j = n - 1
        m = len(ans)
        for i in range(m - 1, -1, -1):
            x = ans[i][0]
            while j >= 0 and z[j] >= x:
                j -= 1
            ans[i][1] = n - j - 1

        ac.st(m)
        for a in ans:
            ac.lst(a)
        return

    @staticmethod
    def ac_141(ac=FastIO()):
        # 利用KMP求每个字符串前缀的最小circular_section
        ind = 0
        while True:
            n = ac.read_int()
            if not n:
                break
            s = ac.read_str()
            ind += 1
            ac.st(f"Test case #{ind}")
            pi = KMP().prefix_function(s)
            for i in range(1, n):
                if i + 1 - pi[i] and (i + 1) % (i + 1 - pi[i]) == 0 and (i + 1) // (i + 1 - pi[i]) > 1:
                    ac.lst([i + 1, (i + 1) // (i + 1 - pi[i])])
            ac.st("")
        return

    @staticmethod
    def ac_160(ac=FastIO()):
        # z函数模板题
        n, m, q = ac.read_list_ints()
        s = ac.read_str()
        t = ac.read_str()
        st = t + "#" + s
        z = KMP().z_function(st)
        cnt = Counter(z[m + 1:])
        for _ in range(q):
            x = ac.read_int()
            ac.st(cnt[x])
        return

    @staticmethod
    def cf_25e(ac=FastIO()):

        # kmp求字符串之间的最长公共prefix_suffix，greedy拼接
        s = [ac.read_str() for _ in range(3)]

        def check(a, b):
            c = b + "#" + a
            f = KMP().prefix_function(c)
            m = len(b)
            if max(f[m:]) == m:
                return a
            x = f[-1]
            return a + b[x:]

        ind = list(range(3))
        ans = sum(len(w) for w in s)
        for item in permutations(ind, 3):
            t1, t2, t3 = [s[x] for x in item]
            cur = len(check(check(t1, t2), t3))
            if cur < ans:
                ans = cur
        ac.st(ans)
        return

    @staticmethod
    def lc_6918(aa: str, bb: str, cc: str) -> str:
        """
        url: https://leetcode.com/problems/shortest-string-that-contains-three-strings/
        tag: kmp|prefix_suffix|greedy|brain_teaser
        """

        def check(a, b):
            c = b + "#" + a
            f = KMP().prefix_function(c)
            m = len(b)
            if max(f[m:]) == m:
                return a
            x = f[-1]
            return a + b[x:]

        # kmp求字符串之间的最长公共prefix_suffix，greedy拼接
        s = [aa, bb, cc]
        ind = list(range(3))
        ans = "".join(s)
        for item in permutations(ind, 3):
            t1, t2, t3 = [s[x] for x in item]
            cur = check(check(t1, t2), t3)
            if len(cur) < len(ans) or (len(cur) == len(ans) and cur < ans):
                ans = cur
        return ans

    @staticmethod
    def lc_2851(s: str, t: str, k: int) -> int:
        """
        url: https://leetcode.com/problems/string-transformation/description/
        tag: kmp|matrix_fast_power|string_hash
        """
        # KMP与fast_power|转移，也可string_hash
        n = len(s)
        mod = 10 ** 9 + 7
        kmp = KMP()
        z = kmp.prefix_function(t + "#" + s + s)
        p = sum(z[i] == n for i in range(2 * n, 3 * n))
        q = n - p
        mat = [[p - 1, p], [q, q - 1]]
        vec = [1, 0] if z[2 * n] == n else [0, 1]
        res = MatrixFastPower().matrix_pow(mat, k, mod)
        ans = vec[0] * res[0][0] + vec[1] * res[0][1]
        return ans % mod

    @staticmethod
    def ac_3823(ac=FastIO()):
        # KMP与扩展KMP即z函数应用模板题
        kmp = KMP()
        for _ in range(ac.read_int()):
            s = ac.read_str()
            if len(s) <= 2:
                ac.st("not exist")
                continue
            pre = kmp.prefix_function(s)
            z = kmp.z_function(s)
            ans = 0
            cnt = Counter(s)
            if s[0] == s[-1] and cnt[s[0]] >= 3:
                ans = 1
            m = len(s)
            for i in range(1, m - 1):
                w = pre[i]
                if z[-w] == w:
                    if w > ans:
                        ans = w
            if not ans:
                ac.st("not exist")
            else:
                ac.st(s[:ans])
        return