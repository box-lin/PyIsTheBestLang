"""
Algorithm：bfs|deque_bfs|discretization_bfs|bound_bfs|coloring_method|odd_circle
Description：multi_source_bfs|bilateral_bfs|0-1bfs|bilateral_bfs|a-star|heuristic_search

====================================LeetCode====================================
1036（https://leetcode.cn/problems/escape-a-large-maze/）bound_bfs|discretization_bfs
2493（https://leetcode.cn/problems/divide-nodes-into-the-maximum-number-of-groups/）union_find|bfs|brute_force|specific_plan|coloring_method|bipartite_graph
2290（https://leetcode.cn/problems/minimum-obstacle-removal-to-reach-corner/）0-1bfs|deque_bfs
1368（https://leetcode.cn/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/）0-1bfs|deque_bfs
2258（https://leetcode.cn/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/）binary_search|bfs|implemention
2092（https://leetcode.cn/problems/find-all-people-with-secret/）bfs
2608（https://leetcode.cn/contest/biweekly-contest-101/problems/shortest-cycle-in-a-graph/）bfs|undirected_smallest_circle|brute_force|shortest_path
1197（https://leetcode.cn/problems/minimum-knight-moves/?envType=study-plan-v2&id=premium-algo-100）bilateral_bfs
1654（https://leetcode.cn/problems/minimum-jumps-to-reach-home/）bfs|implemention
1926（https://leetcode.cn/problems/nearest-exit-from-entrance-in-maze/）deque_bfs|in_place_hash
909（https://leetcode.cn/problems/snakes-and-ladders/）01-bfs|implemention
1210（https://leetcode.cn/problems/minimum-moves-to-reach-target-with-rotations/description/）01-bfs|implemention
1298（https://leetcode.cn/problems/maximum-candies-you-can-get-from-boxes/）bfs
928（https://leetcode.cn/problems/minimize-malware-spread-ii/description/）brute_force|bfs
994（https://leetcode.cn/problems/rotting-oranges/description/）deque_bfs|implemention

=====================================LuoGu======================================
P1144（https://www.luogu.com.cn/problem/P1144）number_of_shortest_path
P1747（https://www.luogu.com.cn/problem/P1747）bilateral_bfs|shortest_path
P5507（https://www.luogu.com.cn/problem/P5507）bilateral_bfs|shortest_path
P2040（https://www.luogu.com.cn/problem/P2040）bfs
P2335（https://www.luogu.com.cn/problem/P2335）bfs
P2385（https://www.luogu.com.cn/problem/P2385）bfs|shortest_path|shortest_path
P2630（https://www.luogu.com.cn/problem/P2630）bfs|implemention|lexicographical_order
P1332（https://www.luogu.com.cn/problem/P1332）bfs
P1330（https://www.luogu.com.cn/problem/P1330）bfs|level_wise|coloring_method|union_find|odd_circle
P1215（https://www.luogu.com.cn/problem/P1215）bfs|implemention|hash
P1037（https://www.luogu.com.cn/problem/P1037）bfs|implemention|brute_force
P2853（https://www.luogu.com.cn/problem/P2853）bfs|counter
P2881（https://www.luogu.com.cn/problem/P2881）bfs|complexity
P2895（https://www.luogu.com.cn/problem/P2895）bfs|implemention
P2960（https://www.luogu.com.cn/problem/P2960）bfs
P2298（https://www.luogu.com.cn/problem/P2298）bfs
P3139（https://www.luogu.com.cn/problem/P3139）bfs|memory_search
P3183（https://www.luogu.com.cn/problem/P3183）bfs|counter|number_of_path|dfs|dp
P4017（https://www.luogu.com.cn/problem/P4017）bfs|counter|number_of_path|dfs|dp
P3395（https://www.luogu.com.cn/problem/P3395）bfs|implemention
P3416（https://www.luogu.com.cn/problem/P3416）bfs|memory_search
P3916（https://www.luogu.com.cn/problem/P3916）reverse_thinking|reverse_graph|reverse_order
P3958（https://www.luogu.com.cn/problem/P3958）build_graph|bfs
P4328（https://www.luogu.com.cn/problem/P4328）bfs|implemention
P4961（https://www.luogu.com.cn/problem/P4961）brute_force|implemention|counter
P6207（https://www.luogu.com.cn/problem/P6207）bfs|shortest_path|specific_plan
P6582（https://www.luogu.com.cn/problem/P6582）bfs|comb|counter|fast_power
P7243（https://www.luogu.com.cn/problem/P7243）bfs|gcd
P3496（https://www.luogu.com.cn/problem/P3496）brain_teaser|bfs|coloring_method|level_wise
P1432（https://www.luogu.com.cn/problem/P1432）memory_search|bfs
P1807（https://www.luogu.com.cn/problem/P1807）dag|longest_path|dag_dp|topological_sort
P1379（https://www.luogu.com.cn/problem/P1379）bilateral_bfs
P5507（https://www.luogu.com.cn/problem/P5507）bilateral_bfs|a-star|heuristic_search
P5908（https://www.luogu.com.cn/problem/P5908）bfs
P1038（https://www.luogu.com.cn/problem/P1038）topological_sorting
P1126（https://www.luogu.com.cn/problem/P1126）bfs
P1213（https://www.luogu.com.cn/problem/P1213）state_compression|01-bfs
P1902（https://www.luogu.com.cn/problem/P1902）binary_search|bfs|in_place_hash
P2199（https://www.luogu.com.cn/problem/P2199）deque_bfs|01-bfs
P2226（https://www.luogu.com.cn/problem/P2226）bfs
P2296（https://www.luogu.com.cn/problem/P2296）reverse_graph|bfs
P2919（https://www.luogu.com.cn/problem/P2919）bfs
P2937（https://www.luogu.com.cn/problem/P2937）01-bfs|monotonic_queue
P3456（https://www.luogu.com.cn/problem/P3456）bfs
P3496（https://www.luogu.com.cn/problem/P3496）brain_teaser|bfs
P3818（https://www.luogu.com.cn/problem/P3818）01-bfs|deque_bfs
P3855（https://www.luogu.com.cn/problem/P3855）bfs|md_state
P3869（https://www.luogu.com.cn/problem/P3869）bfs|state_compression
P4554（https://www.luogu.com.cn/problem/P4554）classical|01-bfs|implemention
P4667（https://www.luogu.com.cn/problem/P4667）01-bfs|implemention
P5096（https://www.luogu.com.cn/problem/P5096）state_compression|bfs|implemention
P5099（https://www.luogu.com.cn/problem/P5099）01-bfs|implemention
P5195（https://www.luogu.com.cn/problem/P5195）bfs
P6131（https://www.luogu.com.cn/problem/P6131）bfs|union_find
P6909（https://www.luogu.com.cn/problem/P6909）preprocess|bfs
P8628（https://www.luogu.com.cn/problem/P8628）01-bfs
P8673（https://www.luogu.com.cn/problem/P8673）01-bfs|implemention
P8674（https://www.luogu.com.cn/problem/P8674）preprocess|build_graph|bfs|implemention
P9065（https://www.luogu.com.cn/problem/P9065）brain_teaser|bfs|brute_force

===================================CodeForces===================================
1594D（https://codeforces.com/contest/1594/problem/D）build_graph|coloring_method|bfs|bipartite_graph
1272E（https://codeforces.com/problemset/problem/1272/E）reverse_graph|multi_source_bfs
1572A（https://codeforces.com/problemset/problem/1572/A）brain_teaser|build_graph|bfs|circle_judge|dag_dp|classical
1037D（https://codeforces.com/problemset/problem/1037/D）01-bfs|implemention|classical
1176E（https://codeforces.com/contest/1176/problem/E）bds|color_method|classical

====================================AtCoder=====================================
ARC090B（https://atcoder.jp/contests/abc087/tasks/arc090_b）bfs|differential_constraint|O(n^2)
ABC133E（https://atcoder.jp/contests/abc133/tasks/abc133_e）bfs|coloring_method|counter
ABC070D（https://atcoder.jp/contests/abc070/tasks/abc070_d）classical|lca|offline_lca
ABC336F（https://atcoder.jp/contests/abc336/tasks/abc336_f）bilateral_bfs|classical|matrix_rotate
ABC339B（https://atcoder.jp/contests/abc339/tasks/abc339_b）bfs|visit
ABC339D（https://atcoder.jp/contests/abc339/tasks/abc339_d）bfs


=====================================AcWing=====================================
173（https://www.acwing.com/problem/content/175/）multi_source_bfs|classical
175（https://www.acwing.com/problem/content/177/）monotonic_queue|bfs
177（https://www.acwing.com/problem/content/179/）multi_source_bfs|bilateral_bfs
4415（https://www.acwing.com/problem/content/description/4418）bfs|coloring_method|odd_circle|specific_plan|counter
4481（https://www.acwing.com/problem/content/description/4484/）01-bfs

"""

from collections import deque, defaultdict
from typing import List

from src.graph.union_find.template import UnionFind
from src.utils.fast_io import FastIO
from src.utils.fast_io import inf


class Solution:
    def __init__(self):
        return

    @staticmethod
    def lc_2608_1(n: int, edges: List[List[int]]) -> int:
        """
        url: https://leetcode.cn/contest/biweekly-contest-101/problems/shortest-cycle-in-a-graph/
        tag: bfs|undirected_smallest_circle|brute_force|shortest_path
        """
        # 求无向图的最小环
        graph = [[] for _ in range(n)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        ans = inf
        for i in range(n):
            dist = [inf] * n
            par = [-1] * n
            dist[i] = 0
            q = deque([i])
            while q:
                x = q.popleft()
                for child in graph[x]:
                    if dist[x] > ans:
                        break
                    if dist[child] == inf:
                        dist[child] = 1 + dist[x]
                        par[child] = x
                        q.append(child)
                    elif par[x] != child and par[child] != x:
                        cur = dist[x] + dist[child] + 1
                        ans = ans if ans < cur else cur
        return ans if ans != inf else -1

    @staticmethod
    def lc_2608_2(n: int, edges: List[List[int]]) -> int:
        """
        url: https://leetcode.cn/contest/biweekly-contest-101/problems/shortest-cycle-in-a-graph/
        tag: bfs|undirected_smallest_circle|brute_force|shortest_path
        """
        # 求无向图的最小环
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        ans = float('inf')
        for i in range(n):
            q = deque([(i, -1, 1)])  # 节点编号，父节点编号，当前路径长度
            visited = {(i, -1)}
            while q:
                u, parent, dist = q.popleft()
                if dist > ans:
                    break
                for v in graph[u]:
                    if v == parent:  # 避免重复访问父节点
                        continue
                    if v == i:  # 找到当前起点的最小环
                        ans = ans if ans < dist else dist
                        break
                    if (v, u) not in visited:
                        visited.add((v, u))
                        q.append((v, u, dist + 1))
        return ans if ans < float('inf') else -1

    @staticmethod
    def lc_2608_3(n: int, edges: List[List[int]]) -> int:
        """
        url: https://leetcode.cn/contest/biweekly-contest-101/problems/shortest-cycle-in-a-graph/
        tag: bfs|undirected_smallest_circle|brute_force|shortest_path
        """
        # 求无向图的最小环
        inf = float('inf')
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)  # build_graph|

        def bfs(start: int) -> int:
            nonlocal inf
            dis = [-1] * n  # dis[i] 表示从 start 到 i 的shortest_path长度
            dis[start] = 0
            q = deque([(start, -1)])
            res = inf
            while q:
                x, fa = q.popleft()
                for y in g[x]:
                    if dis[y] < 0:  # 第一次遇到
                        dis[y] = dis[x] + 1
                        q.append((y, x))
                    elif y != fa:  # 第二次遇到
                        # 由于是 bfs，后面不会遇到更短的环，直接返回
                        res = res if res < dis[x] + dis[y] + 1 else dis[x] + dis[y] + 1
            return res  # 该连通分量无环

        ans = min(bfs(i) for i in range(n))
        return ans if ans < inf else -1

    @staticmethod
    def lc_2608_4(n: int, edges: List[List[int]]) -> int:
        """
        url: https://leetcode.cn/contest/biweekly-contest-101/problems/shortest-cycle-in-a-graph/
        tag: bfs|undirected_smallest_circle|brute_force|shortest_path
        """
        # 求无向图的最小环，brute_force边
        graph = [set() for _ in range(n)]
        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)

        ans = inf
        for x, y in edges:
            graph[x].discard(y)
            graph[y].discard(x)
            dis = [inf] * n
            dis[x] = 0
            stack = deque([x])
            while stack:
                m = len(stack)
                for _ in range(m):
                    i = stack.popleft()
                    for j in graph[i]:
                        if dis[j] == inf:
                            dis[j] = dis[i] + 1
                            stack.append(j)
            ans = ans if ans < dis[y] else dis[y]
            graph[x].add(y)
            graph[y].add(x)
        return ans + 1 if ans < inf else -1

    @staticmethod
    def lg_p1807_1(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1807
        tag: dag|longest_path|dag_dp|topological_sort
        """
        # 有向无环图 DAG topological_sorting求最长路
        n, m = ac.read_list_ints()
        edge = [dict() for _ in range(n)]
        pre = [set() for _ in range(n)]
        for _ in range(m):
            u, v, w = ac.read_list_ints()
            u -= 1
            v -= 1
            edge[u][v] = ac.max(edge[u].get(v, -ac.inf), w)
            pre[v].add(u)

        # 注意这里可能有 0 之外的入度为 0 的点，需要先拓扑消除
        stack = deque([i for i in range(1, n) if not pre[i]])
        while stack:
            i = stack.popleft()
            for j in edge[i]:
                pre[j].discard(i)
                if not pre[j]:
                    stack.append(j)

        # bfs|最长路，进一步还可以确定相应的具体路径
        visit = [-ac.inf] * n
        visit[0] = 0
        stack = deque([0])
        while stack:
            i = stack.popleft()
            for j in edge[i]:
                w = edge[i][j]
                pre[j].discard(i)
                if visit[i] + w > visit[j]:
                    visit[j] = visit[i] + w
                if not pre[j]:
                    stack.append(j)

        ac.st(visit[-1] if visit[-1] > -ac.inf else -1)
        return

    @staticmethod
    def lg_p1807_2(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1807
        tag: dag|longest_path|dag_dp|topological_sort
        """
        # 有向无环图 DAG dfs|求最长路
        n, m = ac.read_list_ints()
        edge = [dict() for _ in range(n)]
        for _ in range(m):
            u, v, w = ac.read_list_ints()
            u -= 1
            v -= 1
            edge[u][v] = ac.max(edge[u].get(v, -ac.inf), w)

        @ac.bootstrap
        def dfs(x):
            if x == n - 1:
                ans[x] = 0
                yield
            res = -ac.inf
            for y in edge[x]:
                yield dfs(y)
                cur = edge[x][y] + ans[y]
                res = res if res > cur else cur
            ans[x] = res
            yield

        ans = [-ac.inf] * n
        dfs(0)
        ac.st(ans[0] if ans[0] > -ac.inf else -1)
        return

    @staticmethod
    def cf_1272e(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/1272/E
        tag: reverse_graph|multi_source_bfs
        """
        # reverse_graph与多源 bfs 
        n = ac.read_int()
        nums = ac.read_list_ints()
        ans = [-1] * n

        edge = [[] for _ in range(n)]
        for i in range(n):
            for x in [i + nums[i], i - nums[i]]:
                if 0 <= x < n:
                    edge[x].append(i)

        # 多源 bfs
        for x in [0, 1]:
            stack = [i for i in range(n) if nums[i] % 2 == x]
            visit = set(stack)
            step = 1
            while stack:
                nex = []
                for i in stack:
                    for j in edge[i]:
                        if j not in visit:
                            ans[j] = step
                            nex.append(j)
                            visit.add(j)
                step += 1
                stack = nex
        ac.lst(ans)
        return

    @staticmethod
    def lg_p3183(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P3183
        tag: bfs|counter|number_of_path|dfs|dp
        """
        # 模板: 有向无环图路径条数
        n, m = ac.read_list_ints()
        edge = [[] for _ in range(n)]
        degree = [0] * n
        out_degree = [0] * n
        for _ in range(m):
            i, j = ac.read_list_ints_minus_one()
            edge[i].append(j)
            degree[j] += 1
            out_degree[i] += 1
        ind = [i for i in range(n) if degree[i] and not out_degree[i]]
        cnt = [0] * n
        stack = [i for i in range(n) if not degree[i]]
        for x in stack:
            cnt[x] = 1
        while stack:  # 也可以dfs|
            nex = []
            for i in stack:
                for j in edge[i]:
                    degree[j] -= 1
                    cnt[j] += cnt[i]
                    if not degree[j]:
                        nex.append(j)
            stack = nex
        ans = sum(cnt[i] for i in ind)
        return ans

    @staticmethod
    def lg_p1747(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1747
        tag: bilateral_bfs|shortest_path
        """
        # 双向 bfs 搜索
        x0, y0 = ac.read_list_ints()
        x2, y2 = ac.read_list_ints()

        def check(x1, y1):
            if (x1, y1) == (1, 1):
                return 0

            visit1 = {(x1, y1): 0}
            visit2 = {(1, 1): 0}
            direc = [[1, 2], [1, -2], [-1, 2], [-1, -2],
                     [2, 1], [2, -1], [-2, 1], [-2, -1]]
            direc.extend([[2, 2], [2, -2], [-2, 2], [-2, -2]])
            stack1 = [[x1, y1]]
            stack2 = [[1, 1]]
            step = 1

            while True:
                nex1 = []
                for i, j in stack1:
                    for a, b in direc:
                        if 0 < i + a <= 20 and 0 < j + b <= 20 and (i + a, j + b) not in visit1:
                            visit1[(i + a, j + b)] = step
                            nex1.append([i + a, j + b])
                            if (i + a, j + b) in visit2:
                                return step + visit2[(i + a, j + b)]

                stack1 = nex1

                nex2 = []
                for i, j in stack2:
                    for a, b in direc:
                        if 0 < i + a <= 20 and 0 < j + b <= 20 and (i + a, j + b) not in visit2:
                            visit2[(i + a, j + b)] = step
                            nex2.append([i + a, j + b])
                            if (i + a, j + b) in visit1:
                                return step + visit1[(i + a, j + b)]

                stack2 = nex2
                step += 1

        ac.st(check(x0, y0))
        ac.st(check(x2, y2))
        return

    @staticmethod
    def lc_2290(grid: List[List[int]]) -> int:
        """
        url: https://leetcode.cn/problems/minimum-obstacle-removal-to-reach-corner/
        tag: 0-1bfs|deque_bfs
        """
        # 队列实现0-1 bfs 即优先选择距离较短的路线
        m, n = len(grid), len(grid[0])
        visit = [[0] * n for _ in range(m)]
        q = deque([(0, 0, 0)])
        while q:
            # 也可以 Dijkstra 求解
            d, x, y = q.popleft()
            for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= nx < m and 0 <= ny < n and not visit[nx][ny]:
                    if [nx, ny] == [m - 1, n - 1]:
                        return d + grid[nx][ny]
                    visit[nx][ny] = 1
                    if not grid[nx][ny]:
                        q.appendleft((d, nx, ny))
                    else:
                        q.append((d + 1, nx, ny))
        return -1

    @staticmethod
    def lc_2493(n: int, edges: List[List[int]]) -> int:
        """
        url: https://leetcode.cn/problems/divide-nodes-into-the-maximum-number-of-groups/
        tag: union_find|bfs|brute_force|specific_plan|coloring_method|bipartite_graph
        """
        # 利用union_find和bfs连通块分组并brute_force最佳specific_plan，也就是coloring_method判断是否可以形成bipartite_graph
        dct = [[] for _ in range(n)]
        uf = UnionFind(n)
        for i, j in edges:
            uf.union(i - 1, j - 1)
            dct[i - 1].append(j - 1)
            dct[j - 1].append(i - 1)

        group = uf.get_root_part()
        ans = 0
        for g in group:
            cur = -inf
            lst = group[g]
            edge = [[i - 1, j - 1] for i, j in edges if uf.find(i - 1) == uf.find(j - 1) == g]
            for i in lst:
                stack = [i]
                visit = {i: 1}
                deep = 1
                while stack:
                    nex = []
                    for x in stack:
                        for y in dct[x]:
                            if y not in visit:
                                visit[y] = visit[x] + 1
                                deep = visit[x] + 1
                                nex.append(y)
                    stack = nex[:]
                if all(abs(visit[x] - visit[y]) == 1 for x, y in edge):
                    if deep > cur:
                        cur = deep
            if cur == -inf:
                return -1
            ans += cur
        return ans

    @staticmethod
    def lc_1368(grid: List[List[int]]) -> int:
        """
        url: https://leetcode.cn/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/
        tag: 0-1bfs|deque_bfs
        """
        # 队列实现0-1 bfs 即优先选择距离较短的路线
        m, n = len(grid), len(grid[0])
        ceil = int(1e9)
        dist = [0] + [ceil] * (m * n - 1)
        seen = set()
        q = deque([(0, 0)])

        while q:
            # 也可以 Dijkstra 求解
            x, y = q.popleft()
            if (x, y) in seen:
                continue
            seen.add((x, y))
            cur_pos = x * n + y
            for i, (nx, ny) in enumerate([(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]):
                new_pos = nx * n + ny
                new_dis = dist[cur_pos] + (1 if grid[x][y] != i + 1 else 0)
                if 0 <= nx < m and 0 <= ny < n and new_dis < dist[new_pos]:  # 注意这里放缩
                    dist[new_pos] = new_dis  # 每个点最多入队首一次队尾一次因此时间复杂度O(mn)
                    if grid[x][y] == i + 1:
                        q.appendleft((nx, ny))
                    else:
                        q.append((nx, ny))
        return dist[m * n - 1]

    @staticmethod
    def lc_1926(maze: List[List[str]], entrance: List[int]) -> int:
        """
        url: https://leetcode.cn/problems/nearest-exit-from-entrance-in-maze/
        tag: deque_bfs|in_place_hash
        """
        # 双端队列01-bfsin_place_hash
        m, n = len(maze), len(maze[0])
        x0, y0 = entrance[:]
        stack = deque([[x0, y0, 0]])
        maze[x0][y0] = "+"
        while stack:
            i, j, d = stack.popleft()
            for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                if 0 <= x < m and 0 <= y < n and maze[x][y] == ".":
                    if x in [0, m - 1] or y in [0, n - 1]:
                        return d + 1
                    stack.append([x, y, d + 1])
                    maze[x][y] = "+"
        return -1

    @staticmethod
    def cf_1572a(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/1572/A
        tag: brain_teaser|build_graph|bfs|circle_judge|dag_dp|classical
        """
        # bfs 判断 DAG circle_judge和无环时的最长路（注意起点可能有多个）
        for _ in range(ac.read_int()):
            n = ac.read_int()
            dct = [dict() for _ in range(n)]
            degree = [0] * n
            for i in range(n):
                lst = ac.read_list_ints_minus_one()[1:]
                for j in lst:
                    dct[j][i] = 0 if i > j else 1
                degree[i] = len(lst)

            # 配置起点
            visit = [0] * n
            stack = [i for i in range(n) if not degree[i]]
            while stack:
                nex = []
                for i in stack:
                    for j in dct[i]:
                        degree[j] -= 1
                        # topological_sorting的同时更新最长路
                        if visit[i] + dct[i][j] > visit[j]:
                            visit[j] = visit[i] + dct[i][j]
                        if not degree[j]:
                            nex.append(j)
                stack = nex
            if max(degree) == 0:
                ac.st(max(visit) + 1)
            else:
                ac.st(-1)
        return

    @staticmethod
    def cf_1037d(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/1037/D
        tag: 01-bfs|implemention|classical
        """
        # 队列与集合判断 bfs_order 即bfs|序
        n = ac.read_int()
        edge = [[] for _ in range(n)]
        for _ in range(n - 1):
            i, j = ac.read_list_ints_minus_one()
            edge[i].append(j)
            edge[j].append(i)

        dct = [set() for _ in range(n)]
        stack = [(0, -1)]
        parent = [-1] * n
        while stack:
            nex = []
            for i, fa in stack:
                for j in edge[i]:
                    if j != fa:
                        nex.append((j, i))
                        dct[i].add(j)
                        parent[j] = i
            stack = nex[:]

        nums = ac.read_list_ints_minus_one()
        stack = deque([{0}])
        for num in nums:
            if not stack or num not in stack[0]:
                ac.st("NO")
                return
            stack[0].discard(num)
            if not stack[0]:
                stack.popleft()
            if dct[num]:
                stack.append(dct[num])
        ac.st("YES")
        return

    @staticmethod
    def lg_p1099(ac=FastIO()):
        # 求最小偏心距在tree_diameter上two_pointers与单调队列
        n, s = ac.read_list_ints()
        dct = [dict() for _ in range(n)]
        for _ in range(n - 1):
            i, j, w = ac.read_list_ints()
            dct[i - 1][j - 1] = w
            dct[j - 1][i - 1] = w

        def bfs_diameter(src):
            res, node = 0, src
            stack = [[src, 0]]
            parent = [-1] * n
            while stack:
                u, dis = stack.pop()
                if dis > res:
                    res = dis
                    node = u
                for v in dct[u]:
                    if v != parent[u]:
                        parent[v] = u
                        stack.append([v, dis + dct[u][v]])
            pa = [node]
            while parent[pa[-1]] != -1:
                pa.append(parent[pa[-1]])
            pa.reverse()
            return node, pa

        # tree_diameter与路径
        start, _ = bfs_diameter(0)
        end, path = bfs_diameter(start)

        def bfs_distance(src):
            dis = [0] * n
            stack = [[src, -1, 1]]
            while stack:
                u, fa, state = stack.pop()
                if state:
                    stack.append([u, fa, 0])
                    for v in dct[u]:
                        if v != fa:
                            stack.append([v, u, 1])
                else:
                    x = 0
                    for v in dct[u]:
                        if v != fa:
                            x = ac.max(x, dct[u][v] + dis[v])
                    dis[u] = x
            return dis

        # tree_diameter上的端点往 start 与往 end 方向的最长距离
        dis1 = bfs_distance(start)  # start -> end
        dis2 = bfs_distance(end)  # end -> start

        def bfs_node(src):
            stack = [[src, -1, 0]]
            res = 0
            while stack:
                u, fa, dis = stack.pop()
                res = ac.max(res, dis)
                for v in dct[u]:
                    if v != fa and v not in diameter:
                        stack.append([v, u, dis + dct[u][v]])
            diameter[src] = res
            return

        # tree_diameter上的端点往非tree_diameter端点上的最远距离
        diameter = {node: 0 for node in path}
        for node in diameter:
            bfs_node(node)

        # two_pointers|sliding_window单调队列记录tree_diameter范围点往非tree_diameter方向延申的最远距离
        m = len(path)
        ans = inf
        gap = 0
        j = 0
        q = deque()
        q.append([diameter[path[0]], 0])
        for i in range(m):
            while q and q[0][1] < i:
                q.popleft()
            if i:
                gap -= dct[path[i - 1]][path[i]]

            # two_pointers与单调队列
            while j + 1 < m and gap + dct[path[j]][path[j + 1]] <= s:
                gap += dct[path[j]][path[j + 1]]
                while q and q[-1][0] < diameter[path[j + 1]]:
                    q.pop()
                q.append([diameter[path[j + 1]], j + 1])
                j += 1

            ans = ac.min(ans, max(dis2[path[i]], dis1[path[j]], q[0][0]))
        ac.st(ans)
        return

    @staticmethod
    def abc_133e(ac=FastIO()):
        # bfscoloring_methodcounter
        n, k = ac.read_list_ints()
        mod = 1000000007
        dct = [[] for _ in range(n)]
        degree = [0] * n
        for _ in range(n - 1):
            i, j = ac.read_list_ints_minus_one()
            dct[i].append(j)
            dct[j].append(i)
            degree[i] += 1
            degree[j] += 1
        if n == 1:
            ac.st(k)
            return
        root = [i for i in range(n) if degree[i] == 1][0]
        stack = [[root, -1, 0, 0]]
        ans = 1
        while stack:
            i, fa, pre, c = stack.pop()
            if pre == 0:
                ans *= (k - c)
            elif pre == 1:
                ans *= (k - 1 - c)
            else:
                ans *= (k - 2 - c)
            ans %= mod
            cnt = 0
            for j in dct[i]:
                if j != fa:
                    cnt += 1
                    stack.append([j, i, pre + 1, cnt - 1])
        ac.st(ans)
        return

    @staticmethod
    def ac_173(ac=FastIO()):
        """
        url: https://www.acwing.com/problem/content/175/
        tag: multi_source_bfs|classical
        """
        # multi_source_bfs模板题
        m, n = ac.read_list_ints()
        grid = [ac.read_list_str() for _ in range(m)]
        stack = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    grid[i][j] = 0
                    stack.append([i, j])
                else:
                    grid[i][j] = inf
        while stack:
            nex = []
            for i, j in stack:
                for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == inf:
                        nex.append([x, y])
                        grid[x][y] = grid[i][j] + 1
            stack = nex[:]
        for g in grid:
            ac.lst(g)
        return

    @staticmethod
    def ac_175(ac=FastIO()):
        """
        url: https://www.acwing.com/problem/content/177/
        tag: monotonic_queue|bfs
        """
        for _ in range(ac.read_int()):

            # 双端priority_queue 01 bfs模板题注意build_graph|
            m, n = ac.read_list_ints()
            grid = [ac.read_str() for _ in range(m)]
            dct = [dict() for _ in range((m + 1) * (n + 1))]
            for i in range(m):
                for j in range(n):
                    x1, x2, x3, x4 = i * (n + 1) + j, i * (n + 1) + j + 1, \
                                     (i + 1) * (n + 1) + j, (i + 1) * (n + 1) + j + 1
                    if grid[i][j] == "/":
                        dct[x2][x3] = dct[x3][x2] = 0
                        dct[x1][x4] = dct[x4][x1] = 1
                    else:
                        dct[x2][x3] = dct[x3][x2] = 1
                        dct[x1][x4] = dct[x4][x1] = 0
            visit = [inf] * ((m + 1) * (n + 1))
            visit[0] = 0
            stack = deque([0])
            while stack and visit[-1] == inf:
                i = stack.popleft()
                d = visit[i]
                for j in dct[i]:
                    dd = d + dct[i][j]
                    if dd < visit[j]:
                        visit[j] = dd
                        if dd == d + 1:
                            stack.append(j)
                        else:
                            stack.appendleft(j)
            ac.st(visit[-1] if visit[-1] < inf else "NO SOLUTION")
        return

    @staticmethod
    def ac_177(ac=FastIO()):
        """
        url: https://www.acwing.com/problem/content/179/
        tag: multi_source_bfs|bilateral_bfs
        """
        for _ in range(ac.read_int()):
            # 多源bilateral_bfs
            m, n = ac.read_list_ints()
            grid = [ac.read_str() for _ in range(m)]
            ghost = []
            boy = []
            girl = []
            for i in range(m):
                for j in range(n):
                    w = grid[i][j]
                    if w == "M":
                        boy = [i, j]
                    elif w == "G":
                        girl = [i, j]
                    elif w == "Z":
                        ghost.append([i, j])

            # 男孩
            dis_boy = [[inf] * n for _ in range(m)]
            stack_boy = [boy]
            for i, j in stack_boy:
                dis_boy[i][j] = 0

            dis_girl = [[inf] * n for _ in range(m)]
            stack_girl = [girl]
            for i, j in stack_girl:
                dis_girl[i][j] = 0

            dis_ghost = [[inf] * n for _ in range(m)]
            stack_ghost = ghost[:]
            for i, j in stack_ghost:
                dis_ghost[i][j] = 0
            pre = 0

            ans = inf
            while ans == inf and stack_girl and stack_boy:
                pre += 1
                for _ in range(2):
                    nex_ghost = []
                    for i, j in stack_ghost:
                        for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                            if 0 <= x < m and 0 <= y < n and dis_ghost[x][y] == inf:
                                dis_ghost[x][y] = pre
                                nex_ghost.append([x, y])
                    stack_ghost = nex_ghost[:]

                for _ in range(3):
                    nex_boy = []
                    for i, j in stack_boy:
                        if dis_ghost[i][j] == inf:
                            for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                                if 0 <= x < m and 0 <= y < n and dis_boy[x][y] == inf and grid[x][y] != "X" and \
                                        dis_ghost[x][y] == inf:
                                    dis_boy[x][y] = pre
                                    nex_boy.append([x, y])
                                    if dis_girl[x][y] < inf:
                                        ans = pre
                    stack_boy = nex_boy[:]

                for _ in range(1):
                    nex = []
                    for i, j in stack_girl:
                        if dis_ghost[i][j] == inf:
                            for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                                if 0 <= x < m and 0 <= y < n and dis_girl[x][y] == inf and grid[x][y] != "X" and \
                                        dis_ghost[x][y] == inf:
                                    dis_girl[x][y] = pre
                                    if dis_boy[x][y] < inf:
                                        ans = pre
                                    nex.append([x, y])
                    stack_girl = nex[:]

            ac.st(ans if ans < inf else -1)
        return

    @staticmethod
    def lg_p1213(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1213
        tag: state_compression|01-bfs
        """
        # state_compression优化01-bfs
        nex = {0: 1, 1: 2, 2: 3, 3: 0}
        lst = "ABDE,ABC,BCEF,ADG,BDEFH,CFI,DEGH,GHI,EFHI".split(",")
        ind = dict()
        for i, st in enumerate(lst):
            ind[i + 1] = [ord(w) - ord("A") for w in st]

        grid = []
        for _ in range(3):
            grid.extend([(num - 3) // 3 for num in ac.read_list_ints()])

        def list_to_num(ls):
            res = 0
            for num in ls:
                res *= 4
                res += num
            return res

        def num_to_list(num):
            res = []
            while num:
                res.append(num % 4)
                num //= 4
            while len(res) < 9:
                res.append(0)
            return res[::-1]

        ans = ""
        start = list_to_num(grid)
        target = list_to_num([3] * 9)

        stack = deque([start])
        visit = dict()
        visit[start] = ""
        if start == target:
            ac.st("")
            return

        while stack:
            state = stack.popleft()
            pre = visit[state]
            if ans and len(pre) > len(ans):
                continue
            if state == target:
                if len(pre) < len(ans) or (len(pre) == len(ans) and pre < ans) or not ans:
                    ans = pre
                continue

            state = num_to_list(state)
            for i in range(9):
                tmp = state[:]
                for w in ind[i + 1]:
                    tmp[w] = nex[tmp[w]]
                cur = list_to_num(tmp)
                if cur not in visit:
                    visit[cur] = pre + str(i + 1)
                    stack.append(cur)
        ac.lst(list(ans))
        return

    @staticmethod
    def lg_p1902(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1902
        tag: binary_search|bfs|in_place_hash
        """
        # binary_search|bfs与in_place_hash路径最大值的最小值
        m, n = ac.read_list_ints()
        grid = [ac.read_list_ints() for _ in range(m)]
        for j in range(n):
            grid[0][j] = -grid[0][j] - 1
        dct = dict()

        def check(x):
            # in_place_hash节省空间
            stack = [(0, j) for j in range(n)]
            cnt = 0
            while stack and cnt < n:
                i, j = stack.pop()
                cnt += 1 if i == m - 1 else 0
                if i + 1 < m:
                    a, b = i + 1, j
                    w = grid[a][b]
                    if x >= w >= 0:
                        stack.append((a, b))
                        grid[a][b] = -w - 1
                if i - 1 >= 0:
                    a, b = i - 1, j
                    w = grid[a][b]
                    if x >= w >= 0:
                        stack.append((a, b))
                        grid[a][b] = -w - 1
                if j + 1 < n:
                    a, b = i, j + 1
                    w = grid[a][b]
                    if x >= w >= 0:
                        stack.append((a, b))
                        grid[a][b] = -w - 1
                if j - 1 >= 0:
                    a, b = i, j - 1
                    w = grid[a][b]
                    if x >= w >= 0:
                        stack.append((a, b))
                        grid[a][b] = -w - 1
            # in_place_hash复原
            for i in range(1, m):
                for j in range(n):
                    w = grid[i][j]
                    if w < 0:
                        grid[i][j] = -w - 1
            return cnt == n

        low = 0
        high = 1000
        while low < high - 1:
            mid = low + (high - low) // 2
            if check(mid):
                high = mid
                dct[mid] = True
            else:
                low = mid
                dct[mid] = False

        if low in dct:
            ac.st(low if dct[low] else high)
        elif high in dct and not dct[high]:
            ac.st(low)
        else:
            ac.st(low if check(low) else high)
        return

    @staticmethod
    def lg_p2199(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2199
        tag: deque_bfs|01-bfs
        """
        # 队列01-bfs判定距离最近的可视范围
        m, n = ac.read_list_ints()
        grid = [ac.read_list_str() for _ in range(m)]
        ind = [[0, 1], [0, -1], [1, 0], [-1, 0],
               [1, 1], [1, -1], [-1, 1], [-1, -1]]
        while True:
            lst = ac.read_list_ints_minus_one()
            if lst == [-1, -1, -1, -1]:
                break
            end = [lst[0], lst[1]]
            start = [lst[2], lst[3]]

            # 奖杯的可视范围
            seen = set()
            i, j = end
            seen.add((i, j))
            for a, b in ind:
                x, y = i, j
                while 0 <= x < m and 0 <= y < n and grid[x][y] != "X":
                    seen.add((x, y))
                    x += a
                    y += b
            if (start[0], start[1]) in seen:
                ac.st(0)
                continue

            # 01-bfs队列
            visit = [[inf] * n for _ in range(m)]
            stack = deque([[0, start[0], start[1]]])
            ans = -1
            visit[start[0]][start[1]] = 0
            while stack and ans == -1:
                d, i, j = stack.popleft()
                for a, b in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                    if 0 <= a < m and 0 <= b < n and grid[a][b] != "X" and visit[a][b] == inf:
                        visit[a][b] = d + 1
                        stack.append([d + 1, a, b])
                        if (a, b) in seen:
                            ans = d + 1
                            break
            ac.st(ans if ans != -1 else "Poor Harry")
        return

    @staticmethod
    def lg_p2226(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2226
        tag: bfs
        """
        # 有限制地BDS转向
        m, n = ac.read_list_ints()
        s1, s2, e1, e2 = ac.read_list_ints_minus_one()
        grid = [ac.read_list_ints() for _ in range(m)]
        ind = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for t in range(1, 11):
            stack = deque([[s1, s2, -1, 0]])
            visit = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(m)]
            ans = -1
            while stack and ans == -1:
                i, j, d, total = stack.popleft()
                pre = visit[i][j][d] if d != -1 else inf
                for dd in range(4):
                    x, y = i + ind[dd][0], j + ind[dd][1]
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1 and (dd == d or pre >= t):
                        nex = pre + 1 if d == dd else 1
                        if visit[x][y][dd] < nex:
                            visit[x][y][dd] = nex
                            stack.append([x, y, dd, total + 1])
                            if (x, y) == (e1, e2):
                                ans = total + 1
                                break
            if ans != -1:
                ac.lst([t, ans])
        return

    @staticmethod
    def lg_p2296(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2296
        tag: reverse_graph|bfs
        """
        # 正向与reverse_graph跑两次bfs
        n, m = ac.read_list_ints()
        dct = [set() for _ in range(n)]
        rev = [set() for _ in range(n)]
        for _ in range(m):
            x, y = ac.read_list_ints_minus_one()
            if x != y:
                dct[x].add(y)
                rev[y].add(x)
        s, t = ac.read_list_ints_minus_one()

        # 终点可达
        reach = [0] * n
        reach[t] = 1
        stack = [t]
        while stack:
            i = stack.pop()
            for j in rev[i]:
                if not reach[j]:
                    reach[j] = 1
                    stack.append(j)
        if not all(reach[x] for x in dct[s]):
            ac.st(-1)
            return

        # 起点出发shortest_path
        visit = [inf] * n
        visit[s] = 0
        stack = deque([s])
        while stack:
            i = stack.popleft()
            for j in dct[i]:
                if all(reach[k] for k in dct[j]) and visit[j] == inf:
                    visit[j] = visit[i] + 1
                    stack.append(j)
        ac.st(visit[t] if visit[t] < inf else -1)
        return

    @staticmethod
    def lg_p2919(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2919
        tag: bfs
        """
        # bfs按元素值sorting后从大到小遍历
        m, n = ac.read_list_ints()
        grid = []
        for _ in range(m):
            grid.append(ac.read_list_ints())
        nodes = []
        for i in range(m):
            for j in range(n):
                nodes.append([i, j])
        nodes = deque(sorted(nodes, reverse=True, key=lambda it: grid[it[0]][it[1]]))

        ans = 0
        while nodes:
            i, j = nodes.popleft()
            if grid[i][j] == -1:
                continue
            ans += 1
            stack = [[grid[i][j], i, j]]
            grid[i][j] = -1
            while stack:
                val, i, j = stack.pop()
                for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1],
                             [i - 1, j - 1], [i - 1, j + 1], [i + 1, j - 1], [i + 1, j + 1]]:
                    if 0 <= x < m and 0 <= y < n and -1 < grid[x][y] <= val:
                        stack.append([grid[x][y], x, y])
                        grid[x][y] = -1
        ac.st(ans)
        return

    @staticmethod
    def lg_p2937(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2937
        tag: 01-bfs|monotonic_queue
        """
        # 01-bfspriority_queue
        n, m = ac.read_list_ints()
        grid = [ac.read_str() for _ in range(m)]
        visit = [[[inf] * 4 for _ in range(n)] for _ in range(m)]
        res = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "C":
                    res.append([i, j])
        start, end = res[0], res[1]
        ind = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        stack = deque([[d, start[0], start[1]] for d in range(4)])
        visit[start[0]][start[1]] = [0, 0, 0, 0]
        while stack:
            d, i, j = stack.popleft()
            x, y = i + ind[d][0], j + ind[d][1]
            if 0 <= x < m and 0 <= y < n and grid[x][y] != "*" and visit[x][y][d] > visit[i][j][d]:
                visit[x][y][d] = visit[i][j][d]
                stack.appendleft([d, x, y])
            for dd in [d - 1, d + 1]:
                dd %= 4
                x, y = i + ind[dd][0], j + ind[dd][1]
                if 0 <= x < m and 0 <= y < n and grid[x][y] != "*" and visit[x][y][dd] > visit[i][j][d] + 1:
                    visit[x][y][dd] = visit[i][j][d] + 1
                    stack.append([dd, x, y])
        ac.st(min(visit[end[0]][end[1]]))
        return

    @staticmethod
    def lg_p3456(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P3456
        tag: bfs
        """
        #  bfs 与周边山峰山谷
        n = ac.read_int()
        grid = [ac.read_list_ints() for _ in range(n)]
        visit = [[0] * n for _ in range(n)]
        ceil = floor = 0
        for x in range(n):
            for y in range(n):
                if visit[x][y]:
                    continue
                visit[x][y] = 1
                stack = [[x, y]]
                big = small = False
                while stack:
                    i, j = stack.pop()
                    for a, b in ((i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1),
                                 (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)):
                        if 0 <= a < n and 0 <= b < n:
                            if grid[a][b] > grid[x][y]:
                                big = True
                            elif grid[a][b] < grid[x][y]:
                                small = True
                            else:
                                if not visit[a][b]:
                                    stack.append([a, b])
                                    visit[a][b] = 1
                if small and big:
                    continue
                else:
                    if big:
                        ceil += 1
                    elif small:
                        floor += 1
                    else:
                        ceil += 1
                        floor += 1
        ac.lst([ceil, floor][::-1])
        return

    @staticmethod
    def lg_p3818(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P3818
        tag: 01-bfs|deque_bfs
        """
        # 队列 01-bfs 状态bfs|
        m, n, d, r = ac.read_list_ints()
        grid = []
        for _ in range(m):
            grid.append(ac.read_str())
        visit = [[[None] * 2 for _ in range(n)] for _ in range(m)]
        visit[0][0][0] = 0
        stack = deque([[0, 0, 0]])
        while stack:
            i, j, s = stack.popleft()
            if i == m - 1 and j == n - 1:
                ac.st(visit[i][j][s])
                return
            if s == 0 and 0 <= i + d < m and 0 <= j + r < n and not visit[i + d][j + r][1] and grid[i + d][
                j + r] != "#":
                visit[i + d][j + r][1] = visit[i][j][s] + 1
                stack.append([i + d, j + r, 1])
            for x, y in [[i - 1, j], [i, j + 1], [i + 1, j], [i, j - 1]]:
                if 0 <= x < m and 0 <= y < n and not visit[x][y][s] and grid[x][y] != "#":
                    visit[x][y][s] = visit[i][j][s] + 1
                    stack.append([x, y, s])
        ac.st(-1)
        return

    @staticmethod
    def lg_p3855(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P3855
        tag: bfs|md_state
        """
        # 定义四维状态的bfs
        m, n = ac.read_list_ints()
        grid = [ac.read_str() for _ in range(m)]
        gg = [-1, -1]
        mm = [-1, -1]
        tt = [-1, -1]
        for i in range(m):
            for j in range(n):
                w = grid[i][j]
                if w == "G":
                    gg = [i, j]
                elif w == "M":
                    mm = [i, j]
                elif w == "T":
                    tt = [i, j]

        visit = [[[[-1 for _ in range(n)] for _ in range(m)] for _ in range(n)] for _ in range(m)]
        stack = deque([[gg[0], gg[1], mm[0], mm[1]]])
        visit[gg[0]][gg[1]][mm[0]][mm[1]] = 0
        while stack:
            a, b, c, d = stack.popleft()
            ind = [[1, 0, 1, 0], [-1, 0, -1, 0], [0, 1, 0, -1], [0, -1, 0, 1]]
            for a0, b0, c0, d0 in ind:
                if 0 <= a + a0 < m and 0 <= b + b0 < n and grid[a + a0][b + b0] == "X":
                    continue
                if 0 <= c + c0 < m and 0 <= d + d0 < n and grid[c + c0][d + d0] == "X":
                    continue
                if 0 <= a + a0 < m and 0 <= b + b0 < n and grid[a + a0][b + b0] != "#":
                    x, y = a + a0, b + b0
                else:
                    x, y = a, b
                if 0 <= c + c0 < m and 0 <= d + d0 < n and grid[c + c0][d + d0] != "#":
                    p, q = c + c0, d + d0
                else:
                    p, q = c, d

                if visit[x][y][p][q] == -1:
                    visit[x][y][p][q] = visit[a][b][c][d] + 1
                    stack.append([x, y, p, q])
                    if [x, y] == [p, q] == tt:
                        ac.st(visit[x][y][p][q])
                        return
        ac.st("no")
        return

    @staticmethod
    def lg_p3869(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P3869
        tag: bfs|state_compression
        """
        # bfs||状压记录最少次数
        m, n = ac.read_list_ints()
        grid = [ac.read_str() for _ in range(m)]
        k = ac.read_int()
        pos = dict()
        ind = dict()
        for i in range(k):
            a, b, c, d = ac.read_list_ints_minus_one()
            if (c, d) not in ind:
                ind[(c, d)] = len(ind)
            if (a, b) not in pos:
                pos[(a, b)] = []
            pos[(a, b)].append((c, d))
        k = len(ind)

        visit = [[[inf] * (1 << k) for _ in range(n)] for _ in range(m)]
        ss = [-1, -1]
        tt = [-1, -1]
        for i in range(m):
            for j in range(n):
                w = grid[i][j]
                if w == "S":
                    ss = [i, j]
                elif w == "T":
                    tt = [i, j]
        stack = deque([[ss[0], ss[1], 0]])
        visit[ss[0]][ss[1]][0] = 0
        while stack:
            i, j, state = stack.popleft()
            if [i, j] == tt:
                break
            for a, b in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                if 0 <= a < m and 0 <= b < n:
                    if (a, b) not in ind:
                        if grid[a][b] != "#":
                            cur_state = state
                            if (a, b) in pos:
                                for (c, d) in pos[(a, b)]:
                                    cur_state ^= (1 << ind[(c, d)])
                            if visit[a][b][cur_state] == inf:
                                stack.append([a, b, cur_state])
                                visit[a][b][cur_state] = visit[i][j][state] + 1
                    else:
                        if (grid[a][b] != "#") == (not state & (1 << ind[(a, b)])):
                            cur_state = state
                            if (a, b) in pos:
                                for (c, d) in pos[(a, b)]:
                                    cur_state ^= (1 << ind[(c, d)])
                            if visit[a][b][cur_state] == inf:
                                stack.append([a, b, cur_state])
                                visit[a][b][cur_state] = visit[i][j][state] + 1
        ac.st(min(visit[tt[0]][tt[1]]))
        return

    @staticmethod
    def lg_p4554(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P4554
        tag: classical|01-bfs|implemention
        """
        # classical 01-bfs implemention
        while True:
            lst = ac.read_list_ints()
            if lst == [0, 0]:
                break
            m, n = lst
            grid = [ac.read_str() for _ in range(m)]
            x1, y1, x2, y2 = ac.read_list_ints()
            visit = [[inf] * n for _ in range(m)]
            stack = deque([[x1, y1]])
            visit[x1][y1] = 0
            while stack and visit[x2][y2] == inf:
                x, y = stack.popleft()
                w = grid[x][y]
                d = visit[x][y]
                for a, b in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
                    if 0 <= a < m and 0 <= b < n:
                        cost = d if grid[a][b] == w else d + 1
                        if visit[a][b] > cost:
                            visit[a][b] = cost
                            if cost == d:
                                stack.appendleft([a, b])
                            else:
                                stack.append([a, b])
            ac.st(visit[x2][y2])
        return

    @staticmethod
    def lg_p4667(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P4667
        tag: 01-bfs|implemention
        """
        #  01-bfs implemention
        m, n = ac.read_list_ints()
        grid = [ac.read_str() for _ in range(m)]
        dct = [dict() for _ in range((m + 1) * (n + 1))]
        for i in range(m):
            for j in range(n):
                x1, x2, x3, x4 = i * (n + 1) + j, i * (n + 1) + j + 1, (i + 1) * (n + 1) + j, (i + 1) * (n + 1) + j + 1
                if grid[i][j] == "/":
                    dct[x2][x3] = dct[x3][x2] = 0
                    dct[x1][x4] = dct[x4][x1] = 1
                else:
                    dct[x2][x3] = dct[x3][x2] = 1
                    dct[x1][x4] = dct[x4][x1] = 0
        visit = [inf] * ((m + 1) * (n + 1))
        visit[0] = 0
        stack = deque([[0, 0]])
        while stack and visit[-1] == inf:
            i, d = stack.popleft()
            if visit[i] < d:
                continue
            for j in dct[i]:
                dd = d + dct[i][j]
                if dd < visit[j]:  # 注意这里和dijkstra非常类似也需要判断更小值
                    visit[j] = dd
                    if dd == d + 1:
                        stack.append([j, dd])
                    else:
                        stack.appendleft([j, dd])
        ac.st(visit[-1] if visit[-1] < inf else "NO SOLUTION")
        return

    @staticmethod
    def lg_p5096(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P5096
        tag: state_compression|bfs|implemention
        """
        # 状压|bfs| bfs implemention
        n, m, k = ac.read_list_ints()
        dct = [dict() for _ in range(n)]
        cao = dict()
        for i in range(k):
            cao[ac.read_int() - 1] = i

        for _ in range(m):
            a, b, c = ac.read_list_ints_minus_one()
            dct[a][b] = dct[b][a] = c + 1
        visit = [[0] * (1 << k) for _ in range(n)]
        cnt = [bin(x).count("1") for x in range(1 << k)]
        visit[0][0] = 1
        stack = [[0, 0]]
        while stack:
            i, state = stack.pop()
            for j in dct[i]:
                w = dct[i][j]
                if cnt[state] > w:
                    continue
                nex = state
                if j in cao:
                    nex |= 1 << cao[j]
                if not visit[j][nex]:
                    visit[j][nex] = 1
                    stack.append([j, nex])
                if not visit[j][state]:
                    visit[j][state] = 1
                    stack.append([j, state])
        ans = 0
        for x in range(1 << k):
            if visit[0][x]:
                ans = ac.max(ans, cnt[x])
        ac.st(ans)
        return

    @staticmethod
    def lg_p5099(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P5099
        tag: 01-bfs|implemention
        """
        # 队列 01-bfs bfs|implemention
        n, t = ac.read_list_ints()
        dct = dict()
        for i in range(n):
            x, z = ac.read_list_ints()
            dct[(x, z)] = i
        visit = [inf] * n
        stack = deque([[0, 0, -1]])
        ans = inf
        while stack:
            i, j, ind = stack.popleft()
            d = 0 if ind == -1 else visit[ind]
            if j == t:
                ans = d
                break
            for a in range(-2, 3, 1):
                for b in range(-2, 3, 1):
                    if (i + a, j + b) in dct and visit[dct[(i + a, j + b)]] > d + 1:
                        visit[dct[(i + a, j + b)]] = d + 1
                        stack.append([i + a, j + b, dct[(i + a, j + b)]])
        ac.st(ans if ans < inf else -1)
        return

    @staticmethod
    def lg_p5195(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P5195
        tag: bfs
        """
        # 记录遇到灌木与否的状态 bfs 
        n, m = ac.read_list_ints()
        lst = []
        while len(lst) < m * n:
            lst.extend(ac.read_list_ints())
        grid = [lst[i * n: i * n + n] for i in range(m)]
        del lst
        pos_2 = [-1, -1]
        wood = []
        for i in range(m):
            for j in range(n):
                w = grid[i][j]
                if w == 2:
                    pos_2 = [i, j]
                elif w == 4:
                    wood.append([i, j])
        # 队列实现的bfs|
        visit = [[[inf, inf] for _ in range(n)] for _ in range(m)]
        stack = deque([pos_2 + [0]])
        visit[pos_2[0]][pos_2[1]][0] = 0
        ans = inf
        while stack:
            i, j, state = stack.popleft()
            d = visit[i][j][state]
            if grid[i][j] == 3 and state == 1:
                ans = d
                break
            for a, b in [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]:
                if 0 <= a < m and 0 <= b < n:
                    if state and grid[a][b] != 1 and visit[a][b][state] > d + 1:
                        visit[a][b][state] = d + 1
                        stack.append([a, b, state])
                    if not state and grid[a][b] not in [1, 3]:
                        if grid[a][b] == 4:
                            cur = 1
                        else:
                            cur = 0
                        if visit[a][b][cur] > d + 1:
                            visit[a][b][cur] = d + 1
                            stack.append([a, b, cur])

        ac.st(ans if ans < inf else -1)
        return

    @staticmethod
    def lg_p6131(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P6131
        tag: bfs|union_find
        """
        #  bfs 不同连通块之间的距离
        m, n = ac.read_list_ints()
        grid = [ac.read_list_str() for _ in range(m)]

        # 确定连通块
        color = 0
        dct = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "X":
                    stack = [[i, j]]
                    grid[i][j] = str(color)
                    cur = []
                    while stack:
                        a, b = stack.pop()
                        cur.append([a, b])
                        for x, y in [[a - 1, b], [a + 1, b], [a, b - 1], [a, b + 1]]:
                            if 0 <= x < m and 0 <= y < n and grid[x][y] == "X":
                                stack.append([x, y])
                                grid[x][y] = str(color)
                    color += 1
                    dct.append(cur)

        dis = [[0] * n for _ in range(m)]
        for c in range(3):
            # 分别连通块到每个点的距离
            stack = deque(dct[c])
            cur = [[inf] * n for _ in range(m)]
            for i, j in stack:
                cur[i][j] = 0
            while stack:
                a, b = stack.popleft()
                for x, y in [[a - 1, b], [a + 1, b], [a, b - 1], [a, b + 1]]:
                    if 0 <= x < m and 0 <= y < n:
                        if grid[x][y] != ".":
                            if cur[x][y] > cur[a][b]:
                                cur[x][y] = cur[a][b]
                                stack.append([x, y])
                        else:
                            # 只有遇到 "."才需要增|距离
                            if cur[x][y] > cur[a][b] + 1:
                                cur[x][y] = cur[a][b] + 1
                                stack.append([x, y])
            for i in range(m):
                for j in range(n):
                    dis[i][j] += cur[i][j]
        # brute_force交互节点
        ans = inf
        for i in range(m):
            for j in range(n):
                if grid[i][j] == ".":  # 三个连通块重复counter需要减去二
                    ans = ac.min(ans, dis[i][j] - 2)
                else:
                    ans = ac.min(ans, dis[i][j])
        ac.st(ans)
        return

    @staticmethod
    def lg_p6909(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P6909
        tag: preprocess|bfs
        """
        # preprocess| bfs
        m, n = ac.read_list_ints()
        grid = [ac.read_str() for _ in range(m)]

        up = [[-1] * n for _ in range(m)]
        for j in range(n):
            for i in range(1, m):
                if grid[i][j] == grid[i - 1][j]:
                    up[i][j] = up[i - 1][j]
                else:
                    up[i][j] = i - 1

        down = [[-1] * n for _ in range(m)]
        for j in range(n):
            for i in range(m - 2, -1, -1):
                if grid[i][j] == grid[i + 1][j]:
                    down[i][j] = down[i + 1][j]
                else:
                    down[i][j] = i + 1

        left = [[-1] * n for _ in range(m)]
        for i in range(m):
            for j in range(1, n):
                if grid[i][j] == grid[i][j - 1]:
                    left[i][j] = left[i][j - 1]
                else:
                    left[i][j] = j - 1

        right = [[-1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n - 2, -1, -1):
                if grid[i][j] == grid[i][j + 1]:
                    right[i][j] = right[i][j + 1]
                else:
                    right[i][j] = j + 1

        s = ac.read_str() + "*"
        k = len(s)
        visit = [[-1] * n for _ in range(m)]
        visit[0][0] = 0
        stack = deque([[0, 0, 0, 0]])
        ans = -1
        while stack and ans == -1:
            d, ind, i, j = stack.popleft()
            if s[ind] == grid[i][j]:
                if ind + 1 > visit[i][j]:
                    stack.append([d + 1, ind + 1, i, j])
                    visit[i][j] = ind + 1
                    if ind + 1 == k:
                        ans = d + 1
                        break
            if up[i][j] != -1:
                x, y = up[i][j], j
                if visit[x][y] < ind:
                    visit[x][y] = ind
                    stack.append([d + 1, ind, x, y])
            if down[i][j] != -1:
                x, y = down[i][j], j
                if visit[x][y] < ind:
                    visit[x][y] = ind
                    stack.append([d + 1, ind, x, y])
            if left[i][j] != -1:
                x, y = i, left[i][j]
                if visit[x][y] < ind:
                    visit[x][y] = ind
                    stack.append([d + 1, ind, x, y])
            if right[i][j] != -1:
                x, y = i, right[i][j]
                if visit[x][y] < ind:
                    visit[x][y] = ind
                    stack.append([d + 1, ind, x, y])
        ac.st(ans)
        return

    @staticmethod
    def lg_p9065(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P9065
        tag: brain_teaser|bfs|brute_force
        """
        # brain_teaserbfsbrute_force
        m, n, k = ac.read_list_ints()
        grid = [ac.read_list_ints() for _ in range(m)]
        pos = set(tuple(ac.read_list_ints_minus_one()) for _ in range(k))

        def bfs(s1, s2):
            stack = deque()
            dis = [[inf] * n for _ in range(m)]
            dis[s1][s2] = 0
            stack.append([0, s1, s2])
            while stack:
                d, ii, jj = stack.popleft()
                for x, y in [[ii - 1, jj], [ii + 1, jj], [ii, jj - 1], [ii, jj + 1]]:
                    if 0 <= x < m and 0 <= y < n and d + 1 < dis[x][y] and grid[x][y]:
                        dis[x][y] = d + 1
                        stack.append([d + 1, x, y])
            return dis

        dis1 = bfs(0, 0)
        dis2 = bfs(m - 1, n - 1)
        ans = dis1[m - 1][n - 1]
        if pos:
            pre = defaultdict(lambda: inf)
            for i, j in pos:
                pre[grid[i][j]] = ac.min(pre[grid[i][j]], dis1[i][j])
            floor = min(pre.values())
            for i, j in pos:
                cur = ac.min(pre[grid[i][j]], floor + 1) + dis2[i][j] + 1
                ans = ac.min(ans, cur)
        ac.st(ans if ans < inf else -1)
        return

    @staticmethod
    def cf_1594d(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1594/problem/D
        tag: build_graph|coloring_method|bfs|bipartite_graph
        """
        for _ in range(ac.read_int()):

            def check():
                n, m = ac.read_list_ints()
                dct = [[] for _ in range(n)]
                for _ in range(m):
                    x, y, w = ac.read_list_strs()
                    x = int(x) - 1
                    y = int(y) - 1
                    if w == "imposter":
                        z = 1
                    else:
                        z = 0
                    dct[x].append([y, z])
                    dct[y].append([x, z])
                color = [-1] * n
                ans = 0
                for i in range(n):
                    if color[i] == -1:
                        stack = [i]
                        color[i] = 0
                        cnt = [0, 0]
                        cnt[0] = 1
                        while stack:
                            x = stack.pop()
                            for y, z in dct[x]:
                                ww = color[x] ^ z
                                if color[y] == -1:
                                    color[y] = ww
                                    stack.append(y)
                                    cnt[ww] += 1
                                else:
                                    if color[y] != ww:
                                        ac.st(-1)
                                        return
                        ans += max(cnt)
                ac.st(ans)
                return

            check()
        return

    @staticmethod
    def lc_909(board: List[List[int]]) -> int:
        """
        url: https://leetcode.cn/problems/snakes-and-ladders/
        tag: 01-bfs|implemention
        """

        # 01-bfs|implemention
        def position(num):
            i = (num - 1) // n
            j = (num - 1) % n
            if i % 2:
                return [n - 1 - i, n - 1 - j]
            return [n - 1 - i, j]

        n = len(board)
        visit = {1}
        stack = deque([[1, 0]])
        while stack:
            pre, ans = stack.popleft()
            if pre == n * n:
                return ans
            for nex in range(pre + 1, pre + 7):
                a, b = position(nex)
                if board[a][b] != -1:
                    nex = board[a][b]
                if nex == n * n:
                    return ans + 1
                if nex not in visit:
                    visit.add(nex)
                    stack.append([nex, ans + 1])
        return -1

    @staticmethod
    def lc_994(grid: List[List[int]]) -> int:
        """
        url: https://leetcode.cn/problems/rotting-oranges/description/
        tag: deque_bfs|implemention
        """
        # bfs队列implemention
        m, n = len(grid), len(grid[0])
        stack = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    stack.append([i, j, 0])
        ans = 0
        while stack:
            i, j, d = stack.popleft()
            ans = d
            for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    grid[x][y] = 2
                    stack.append([x, y, d + 1])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return ans

    @staticmethod
    def lc_1036_1(blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        """
        url: https://leetcode.cn/problems/escape-a-large-maze/
        tag: bound_bfs|discretization_bfs
        """

        # bound_bfs和discretization_bfs两种解法
        def check(node):
            stack = [node]
            visit = {tuple(node)}
            while stack:
                nex = []
                for i, j in stack:
                    for x, y in [[i - 1, j], [i + 1, j], [i, j + 1], [i, j - 1]]:
                        if 0 <= x < n and 0 <= y < n and (x, y) not in visit and (x, y) not in block:
                            nex.append([x, y])
                            visit.add((x, y))
                stack = nex
                if len(visit) >= ceil:
                    break
            return visit

        n = 10 ** 6
        block = set(tuple(b) for b in blocked)
        m = len(block)
        ceil = m * m
        visit_s = check(source)
        visit_t = check(target)
        return len(visit_s.intersection(visit_t)) > 0 or (len(visit_s) >= ceil and len(visit_t) >= ceil)

    @staticmethod
    def lc_1036_2(blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        """
        url: https://leetcode.cn/problems/escape-a-large-maze/
        tag: bound_bfs|discretization_bfs
        """
        # bound_bfs和discretization_bfs两种解法
        nodes_r = {0, 10 ** 6 - 1}
        nodes_c = {0, 10 ** 6 - 1}
        for a, b in blocked + [source] + [target]:
            nodes_r.add(a)
            nodes_c.add(b)

        nodes_r = sorted(list(nodes_r))
        m = len(nodes_r)
        ind_r = dict()
        x = 0
        ind_r[nodes_r[0]] = x
        for i in range(1, m):
            if nodes_r[i] == nodes_r[i - 1] + 1:
                x += 1
            else:
                x += 2
            ind_r[nodes_r[i]] = x
        r_id = x

        nodes_c = sorted(list(nodes_c))
        m = len(nodes_c)
        ind_c = dict()
        x = 0
        ind_c[nodes_c[0]] = x
        for i in range(1, m):
            if nodes_c[i] == nodes_c[i - 1] + 1:
                x += 1
            else:
                x += 2
            ind_c[nodes_c[i]] = x
        c_id = x

        blocked = set((ind_r[b[0]], ind_c[b[1]]) for b in blocked)
        source = (ind_r[source[0]], ind_c[source[1]])
        target = (ind_r[target[0]], ind_c[target[1]])
        stack = deque([source])
        visit = {source}
        while stack:
            i, j = stack.popleft()
            for x, y in [[i - 1, j], [i + 1, j], [i, j + 1], [i, j - 1]]:
                if 0 <= x <= r_id and 0 <= y <= c_id and (x, y) not in visit and (x, y) not in blocked:
                    stack.append((x, y))
                    if (x, y) == target:
                        return True
                    visit.add((x, y))
        return False

    @staticmethod
    def ac_4415(ac=FastIO()):
        """
        url: https://www.acwing.com/problem/content/description/4418
        tag: bfs|coloring_method|odd_circle|specific_plan|counter
        """
        # bfscoloring_method，判断有无奇数环，specific_plancounter
        mod = 998244353

        def check():
            n, m = ac.read_list_ints()
            dct = [[] for _ in range(n)]
            for _ in range(m):
                u, v = ac.read_list_ints_minus_one()
                dct[u].append(v)
                dct[v].append(u)

            visit = [-1] * n
            ans = 1
            for i in range(n):
                if visit[i] == -1:
                    # coloring_method模板
                    stack = [i]
                    color = 0
                    visit[i] = color
                    cnt = [1, 0]
                    while stack:
                        color = 1 - color
                        nex = []
                        for x in stack:
                            for y in dct[x]:
                                if visit[y] == -1:
                                    visit[y] = color
                                    cnt[color] += 1
                                    nex.append(y)
                                elif visit[y] != color:
                                    ac.st(0)
                                    return
                        stack = nex
                    res = pow(2, cnt[0], mod) + pow(2, cnt[1], mod)  # specific_plancounter
                    ans *= res
                    ans %= mod
            ac.st(ans)
            return

        for _ in range(ac.read_int()):
            check()
        return

    @staticmethod
    def lg_p1330(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1330
        tag: bfs|level_wise|coloring_method|union_find|odd_circle
        """
        # bfs隔层coloring_method，判断有无奇数环
        n, m = ac.read_list_ints()
        edge = [[] for _ in range(n)]
        for _ in range(m):
            u, v = ac.read_list_ints_minus_one()
            edge[u].append(v)
            edge[v].append(u)

        visit = [-1] * n
        ans = 0
        for i in range(n):
            if visit[i] == -1:
                # bfscoloring_method
                stack = [i]
                color = 0
                visit[i] = color
                cnt = [1, 0]
                while stack:
                    color = 1 - color
                    nex = []
                    for x in stack:
                        for y in edge[x]:
                            if visit[y] == -1:
                                visit[y] = color
                                cnt[color] += 1
                                nex.append(y)
                            elif visit[y] != color:
                                # 奇数环
                                ac.st("Impossible")
                                return
                    stack = nex
                ans += cnt[0] if cnt[0] < cnt[1] else cnt[1]
        ac.st(ans)
        return

    @staticmethod
    def ac_4481(ac=FastIO()):
        """
        url: https://www.acwing.com/problem/content/description/4484/
        tag: 01-bfs
        """
        # 01-bfs
        m, n = ac.read_list_ints()
        r, c = ac.read_list_ints_minus_one()
        x, y = ac.read_list_ints()
        grid = [ac.read_str() for _ in range(m)]

        visit = [[0] * n for _ in range(m)]
        visit[r][c] = 1
        stack = deque([[0, 0, r, c]])
        while stack:
            a, b, x1, y1 = stack.popleft()
            for c, d in [[x1 - 1, y1], [x1 + 1, y1]]:
                if 0 <= c < m and 0 <= d < n and grid[c][d] == "." and not visit[c][d]:
                    visit[c][d] = 1
                    stack.appendleft([a, b, c, d])

            for c, d in [[x1, y1 + 1]]:
                if 0 <= c < m and 0 <= d < n and grid[c][d] == "." and b + \
                        1 <= y and not visit[c][d]:
                    visit[c][d] = 1
                    stack.append([a, b + 1, c, d])

            for c, d in [[x1, y1 - 1]]:
                if 0 <= c < m and 0 <= d < n and grid[c][d] == "." and a + \
                        1 <= x and not visit[c][d]:
                    visit[c][d] = 1
                    stack.append([a + 1, b, c, d])

        ans = 0
        for i in range(m):
            for j in range(n):
                if visit[i][j]:
                    ans += 1
        ac.st(ans)
        return

    @staticmethod
    def lg_p1144(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1144
        tag: number_of_shortest_path|bfs
        """
        mod = 100003
        n, m = ac.read_list_ints()
        dct = [[] for _ in range(n)]
        for _ in range(m):
            x, y = ac.read_list_ints_minus_one()
            dct[x].append(y)
            dct[y].append(x)
        n = len(dct)
        dis = [inf for _ in range(n)]
        cnt = [0] * n
        queue = deque([0])
        dis[0] = 0
        cnt[0] = 1
        while queue:
            u = queue.popleft()
            for v in dct[u]:
                if dis[v] > dis[u] + 1:
                    dis[v] = dis[u] + 1
                    cnt[v] = cnt[u]
                    cnt[v] %= mod
                    queue.append(v)
                elif dis[v] == dis[u] + 1:
                    cnt[v] += cnt[u]
                    cnt[v] %= mod
        for x in cnt:
            ac.st(x)
        return

    @staticmethod
    def abc_070d(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc070/tasks/abc070_d
        tag: classical|bfs|tree_dis
        """
        n = ac.read_int()
        dct = [[] for _ in range(n)]
        for _ in range(n - 1):
            a, b, c = ac.read_list_ints()
            dct[a - 1].append((b - 1, c))
            dct[b - 1].append((a - 1, c))

        q, k = ac.read_list_ints()
        k -= 1
        dis = [0] * n
        stack = [[k, -1]]
        while stack:
            i, fa = stack.pop()
            for j, w in dct[i]:
                if j != fa:
                    stack.append([j, i])
                    dis[j] = dis[i] + w
        for _ in range(q):
            a, b = ac.read_list_ints_minus_one()
            ac.st(dis[a] + dis[b])
        return

    @staticmethod
    def abc_336f(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc336/tasks/abc336_f
        tag: bilateral_bfs|classical|matrix_rotate
        """
        m, n = ac.read_list_ints()
        grid = []
        for _ in range(m):
            grid.extend(ac.read_list_ints())

        def check():
            visit = {tuple(grid): 0}
            stack = [grid[:]]
            for s in range(10):
                nex = []
                for pre in stack:

                    for a, b, c, d in [[0, 0, m - 2, n - 2], [0, 1, m - 2, n - 1], [1, 0, m - 1, n - 2],
                                       [1, 1, m - 1, n - 1]]:
                        tmp = pre[:]
                        for i in range(m):
                            for j in range(n):
                                if a <= i <= c and b <= j <= d:
                                    new_i = c - (i - a)
                                    new_j = d - (j - b)
                                else:
                                    new_i = i
                                    new_j = j
                                tmp[new_i * n + new_j] = pre[i * n + j]
                        if tuple(tmp) not in visit:
                            visit[tuple(tmp)] = s + 1
                            nex.append(tmp[:])
                stack = [ls[:] for ls in nex]
            return visit

        visit1 = check()
        grid = list(range(1, m * n + 1))
        visit2 = check()
        ans = inf
        for k in visit1:
            if k in visit2:
                ans = ac.min(ans, visit1[k] + visit2[k])
        ac.st(ans if ans < inf else -1)
        return
