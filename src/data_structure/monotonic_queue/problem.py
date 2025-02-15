"""
Algorithm：deque|monotonic_queue|monotonic_queue
Description：sliding_window|monotonic

====================================LeetCode====================================
239（https://leetcode.cn/problems/sliding-window-maximum/）sliding_window_maximum
1696（https://leetcode.cn/problems/jump-game-vi/）monotonic_queue|dp
862（https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/description/）prefix_sum|monotonic_queue|dp
1425（https://leetcode.cn/problems/constrained-subsequence-sum/）monotonic_queue|dp


====================================LeetCode====================================
1918D（https://codeforces.com/contest/1918/problem/D）binary_search|greedy|monotonic_queue

=====================================LuoGu======================================
P2251（https://www.luogu.com.cn/problem/P2251）sliding_window_minimum
P2032（https://www.luogu.com.cn/problem/P2032）sliding_window_maximum
P1750（https://www.luogu.com.cn/problem/P1750）pointer|sliding_window|stack|queue
P2311（https://www.luogu.com.cn/problem/P2311）sliding_window
P7175（https://www.luogu.com.cn/problem/P7175）monotonic_queue|implemention
P7793（https://www.luogu.com.cn/problem/P7793）monotonic_queue
P2216（https://www.luogu.com.cn/problem/P2216）sliding_window|sub_matrix
P1886（https://www.luogu.com.cn/problem/P1886）sliding_window
P1725（https://www.luogu.com.cn/problem/P1725）monotonic_queue|pointer|sliding_window|liner_dp
P2827（https://www.luogu.com.cn/problem/P2827）monotonic_queue
P3800（https://www.luogu.com.cn/problem/P3800）monotonic_queue|matrix_dp
P1016（https://www.luogu.com.cn/problem/P1016）monotonic_queue|greedy|implemention
P1714（https://www.luogu.com.cn/problem/P1714）prefix_sum|sliding_window
P2629（https://www.luogu.com.cn/problem/P2629）circular_array|prefix_sum|sliding_window
P3522（https://www.luogu.com.cn/problem/P3522）monotonic_stack
P3957（https://www.luogu.com.cn/problem/P3957）binary_search|monotonic_queue|dp
P4085（https://www.luogu.com.cn/problem/P4085）two_pointers|monotonic_queue|sliding_window
P4392（https://www.luogu.com.cn/problem/P4392）sliding_window|monotonic_queue

=====================================AcWing=====================================
133（https://www.acwing.com/problem/content/135/）monotonic_queue
135（https://www.acwing.com/problem/content/137/）monotonic_queue

"""
from collections import deque
from typing import List

from src.basis.binary_search.template import BinarySearch
from src.data_structure.monotonic_queue.template import PriorityQueue
from src.utils.fast_io import FastIO
from src.utils.fast_io import inf


class Solution:
    def __init__(self):
        return

    @staticmethod
    def lg_p1725(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1725
        tag: monotonic_queue|pointer|sliding_window|liner_dp
        """
        n, low, high = ac.read_list_ints()
        n += 1
        nums = ac.read_list_ints()
        dp = [-inf] * n
        dp[0] = nums[0]
        j = 0
        stack = deque()
        for i in range(1, n):
            while stack and stack[0][0] < i - high:
                stack.popleft()
            while j < n and j <= i - low:
                while stack and stack[-1][1] <= dp[j]:
                    stack.pop()
                stack.append([j, dp[j]])
                j += 1
            if stack:
                dp[i] = stack[0][1] + nums[i]
        ans = max(dp[x] for x in range(n) if x + high >= n)
        ac.st(ans)
        return

    @staticmethod
    def lc_239(nums: List[int], k: int) -> List[int]:
        """
        url: https://leetcode.cn/problems/sliding-window-maximum/
        tag: sliding_window_maximum
        """
        return PriorityQueue().sliding_window(nums, k)

    @staticmethod
    def lc_862(nums: List[int], k: int) -> int:
        """
        url: https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/description/
        tag: prefix_sum|monotonic_queue|dp
        """
        n = len(nums)
        stack = deque([0])
        ind = deque([-1])
        pre = 0
        ans = n + 1
        for i in range(n):
            pre += nums[i]
            while stack and stack[0] <= pre - k:
                stack.popleft()
                j = ind.popleft()
                if i - j < ans:
                    ans = i - j
            while stack and stack[-1] >= pre:
                stack.pop()
                ind.pop()
            stack.append(pre)
            ind.append(i)
        return ans if ans < n + 1 else -1

    @staticmethod
    def lg_p2032(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2032
        tag: sliding_window_maximum
        """
        n, k = ac.read_list_ints()
        nums = ac.read_list_ints()
        ans = PriorityQueue().sliding_window(nums, k)
        for a in ans:
            ac.st(a)
        return

    @staticmethod
    def lg_p2251(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2251
        tag: sliding_window_minimum
        """
        n, m = ac.read_list_ints()
        nums = ac.read_list_ints()
        ans = PriorityQueue().sliding_window(nums, m, "min")
        for a in ans:
            ac.st(a)
        return

    @staticmethod
    def lg_p2216(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2216
        tag: sliding_window|sub_matrix|classical|matrix_deque|monotonic_queue
        """
        m, n, k = ac.read_list_ints()
        grid = [ac.read_list_ints() for _ in range(m)]

        ceil = [[0] * n for _ in range(m)]
        floor = [[0] * n for _ in range(m)]
        pq = PriorityQueue()
        for i in range(m):
            ceil[i] = pq.sliding_window_all(grid[i], k, "max")
            floor[i] = pq.sliding_window_all(grid[i], k, "min")
        for j in range(n):
            lst = pq.sliding_window_all([ceil[i][j] for i in range(m)], k, "max")
            for i in range(m):
                ceil[i][j] = lst[i]
            lst = pq.sliding_window_all([floor[i][j] for i in range(m)], k, "min")
            for i in range(m):
                floor[i][j] = lst[i]
        ans = ceil[k - 1][k - 1] - floor[k - 1][k - 1]
        for i in range(k - 1, m):
            for j in range(k - 1, n):
                ans = ac.min(ans, ceil[i][j] - floor[i][j])
        ac.st(ans)
        return

    @staticmethod
    def lg_p1886(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1886
        tag: sliding_window
        """
        n, k = ac.read_list_ints()
        nums = ac.read_list_ints()
        ans1 = []
        ans2 = []
        ceil = deque()
        floor = deque()
        for i in range(n):
            while ceil and ceil[0] < i - k + 1:
                ceil.popleft()
            while ceil and nums[ceil[-1]] <= nums[i]:
                ceil.pop()
            ceil.append(i)

            while floor and floor[0] < i - k + 1:
                floor.popleft()
            while floor and nums[floor[-1]] >= nums[i]:
                floor.pop()
            floor.append(i)

            if i >= k - 1:
                ans1.append(nums[floor[0]])
                ans2.append(nums[ceil[0]])
        ac.lst(ans1)
        ac.lst(ans2)
        return

    @staticmethod
    def lg_p3800(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P3800
        tag: monotonic_queue|matrix_dp
        """
        m, n, k, t = ac.read_list_ints()
        dct = [dict() for _ in range(m)]
        for _ in range(k):
            x, y, val = ac.read_list_ints()
            x -= 1
            y -= 1
            dct[x][y] = val

        dp = [[0] * n for _ in range(2)]
        pre = 0
        for i in range(m):
            cur = 1 - pre
            stack = deque()
            ind = 0
            for j in range(n):
                while stack and stack[0][0] < j - t:
                    stack.popleft()
                while ind < n and ind <= j + t:
                    while stack and stack[-1][1] <= dp[pre][ind]:
                        stack.pop()
                    stack.append([ind, dp[pre][ind]])
                    ind += 1
                dp[cur][j] = dct[i].get(j, 0) + stack[0][1]
            pre = cur
        ac.st(max(dp[pre]))
        return

    @staticmethod
    def ac_133(ac=FastIO()):
        """
        url: https://www.acwing.com/problem/content/135/
        tag: monotonic_queue
        """
        n, m, q, u, v, t = ac.read_list_ints()
        nums1 = ac.read_list_ints()
        nums1 = deque(sorted(nums1, reverse=True))
        nums2 = deque()
        nums3 = deque()
        delta = 0
        ans1 = []
        ans2 = []
        for i in range(1, m + 1):
            a = nums1[0] + delta if nums1 else -inf
            b = nums2[0] + delta if nums2 else -inf
            c = nums3[0] + delta if nums3 else -inf
            if a >= b and a >= c:
                x = a
                nums1.popleft()
                x1 = x * u // v
                nums2.append(x1 - delta - q)
                nums3.append(x - x1 - delta - q)
            elif b >= c and b >= a:
                x = b
                nums2.popleft()
                x1 = x * u // v
                nums2.append(x1 - delta - q)
                nums3.append(x - x1 - delta - q)
            else:
                x = c
                nums3.popleft()
                x1 = x * u // v
                nums2.append(x1 - delta - q)
                nums3.append(x - x1 - delta - q)
            delta += q
            if i % t == 0:
                ans1.append(x)

        ind = 0
        while nums1 or nums2 or nums3:
            a = nums1[0] + delta if nums1 else -inf
            b = nums2[0] + delta if nums2 else -inf
            c = nums3[0] + delta if nums3 else -inf
            if a >= b and a >= c:
                x = a
                nums1.popleft()
            elif b >= c and b >= a:
                x = b
                nums2.popleft()
            else:
                x = c
                nums3.popleft()
            ind += 1
            if ind % t == 0:
                ans2.append(x)
        ac.lst(ans1)
        ac.lst(ans2)
        return

    @staticmethod
    def lg_p1016(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1016
        tag: monotonic_queue|greedy|implemention|classical
        """
        d1, c, d2, p, n = ac.read_list_floats()
        n = int(n)
        nums = [[0, p]] + [ac.read_list_floats() for _ in range(n)] + [[d1, 0]]
        nums.sort()
        stack = deque([[p, c]])
        ans = 0
        in_stack = c
        n = len(nums)
        for i in range(1, n):
            dis = nums[i][0] - nums[i - 1][0]
            if in_stack * d2 < dis:
                ac.st("No Solution")
                return
            while dis:
                x = ac.min(dis / d2, stack[0][1])
                ans += x * stack[0][0]
                dis -= x * d2
                stack[0][1] -= x
                in_stack -= x
                if not stack[0][1]:
                    stack.popleft()
            cur_p = nums[i][1]
            while stack and stack[-1][0] >= cur_p:
                in_stack -= stack.pop()[1]
            stack.append([cur_p, c - in_stack])
            in_stack = c
        ac.st("%.2f" % ans)
        return

    @staticmethod
    def lg_p1714(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1714
        tag: prefix_sum|sliding_window
        """
        n, m = ac.read_list_ints()
        nums = ac.read_list_ints()
        ans = max(nums)
        pre = 0
        stack = deque([[-1, 0]])
        for i in range(n):
            pre += nums[i]
            while stack and stack[0][0] <= i - m - 1:
                stack.popleft()
            while stack and stack[-1][1] >= pre:
                stack.pop()
            stack.append([i, pre])
            if stack:
                ans = ac.max(ans, pre - stack[0][1])
        ac.st(ans)
        return

    @staticmethod
    def lg_p2629(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2629
        tag: circular_array|prefix_sum|sliding_window|classical
        """
        n = ac.read_int()
        nums = ac.read_list_ints()
        ans = pre = 0
        stack = deque([(0, 0)])
        lst = [0]
        for i in range(1, n * 2):
            pre += nums[i % n]
            while stack and stack[0][0] <= i - n:
                stack.popleft()
            while stack and stack[-1][1] >= pre:
                stack.pop()
            stack.append((i, pre))
            if i >= n:
                if stack[0][1] >= lst[i - n]:
                    ans += 1
            if i <= n:
                lst.append(pre)
        ac.st(ans)
        return

    @staticmethod
    def lg_p3957(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P3957
        tag: binary_search|monotonic_queue|dp
        """
        n, d, k = ac.read_list_ints()
        dis = [0]
        score = [0]
        for _ in range(n):
            x, s = ac.read_list_ints()
            dis.append(x)
            score.append(s)
        n += 1

        def check(g):
            dp = [-inf] * n
            stack = deque()
            dp[0] = score[0]
            floor = ac.max(1, d - g)
            ceil = d + g
            j = 0
            for i in range(1, n):
                while stack and stack[0][1] < dis[i] - ceil:
                    stack.popleft()
                while j < n and dis[i] - dis[j] >= floor:
                    if dis[i] - dis[j] > ceil:
                        j += 1
                        continue
                    while stack and stack[-1][0] <= dp[j]:
                        stack.pop()
                    stack.append([dp[j], dis[j]])
                    j += 1
                if stack:
                    dp[i] = stack[0][0] + score[i]
                    if dp[i] >= k:
                        return True
            return False

        ans = BinarySearch().find_int_left(0, dis[-1], check)
        ac.st(ans if check(ans) else -1)
        return

    @staticmethod
    def lg_p4085(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P4085
        tag: two_pointers|monotonic_queue|sliding_window
        """
        n, m = ac.read_list_ints()
        f = []
        s = []
        for i in range(n):
            a, b = ac.read_list_ints()
            f.append(a)
            s.append(b)

        ans = inf
        stack = deque([])
        j = pre = 0
        for i in range(n):
            while stack and stack[0][0] < i:
                stack.popleft()
            while j < n and pre < m:
                pre += f[j]
                while stack and stack[-1][1] <= s[j]:
                    stack.pop()
                stack.append([j, s[j]])
                j += 1
            if pre >= m:
                ans = ac.min(ans, stack[0][1])
            pre -= f[i]
        ac.st(ans)
        return

    @staticmethod
    def lg_p4392(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P4392
        tag: sliding_window|monotonic_queue
        """
        n, m, c = ac.read_list_ints()
        ceil = deque()
        floor = deque()
        nums = ac.read_list_ints()
        ans = False
        for i in range(n):

            while ceil and ceil[0] <= i - m:
                ceil.popleft()
            while floor and floor[0] <= i - m:
                floor.popleft()

            while ceil and nums[ceil[-1]] <= nums[i]:
                ceil.pop()
            ceil.append(i)

            while floor and nums[floor[-1]] >= nums[i]:
                floor.pop()
            floor.append(i)

            if i >= m - 1 and nums[ceil[0]] - nums[floor[0]] <= c:
                ac.st(i - m + 2)
                ans = True
        if not ans:
            ac.st("NONE")
        return

    @staticmethod
    def cf_1918d(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1918/problem/D
        tag: binary_search|greedy|monotonic_queue
        """
        for _ in range(ac.read_int()):
            n = ac.read_int()
            nums = ac.read_list_ints()
            pre = ac.accumulate(nums)

            def check(x):
                dp = [inf] * (n + 1)
                dp[0] = 0
                stack = deque([0])
                for i in range(n):
                    while stack and pre[i] - pre[stack[0]] > x:
                        stack.popleft()
                    dp[i + 1] = dp[stack[0]] + nums[i]
                    while stack and dp[stack[-1]] > dp[i + 1]:
                        stack.pop()
                    stack.append(i + 1)
                    if dp[i + 1] <= x and pre[-1] - pre[i + 1] <= x:
                        return True
                return False

            ans = BinarySearch().find_int_left(0, sum(nums), check)
            ac.st(ans)
        return
