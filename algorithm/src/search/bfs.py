import unittest
from collections import deque
from typing import List
from algorithm.src.fast_io import FastIO, inf

"""
算法：广度优先搜索、双端队列BFS
功能：在有向图与无向图进行扩散，多源BFS、双向BFS，0-1BFS（类似SPFA）双向BFS或者A-star启发式搜索
题目：

===================================力扣===================================
2493. 将节点分成尽可能多的组（https://leetcode.cn/problems/divide-nodes-into-the-maximum-number-of-groups/）利用并查集和广度优先搜索进行连通块分组并枚举最佳方案
2290. 到达角落需要移除障碍物的最小数（https://leetcode.cn/problems/minimum-obstacle-removal-to-reach-corner/）使用0-1 BFS进行优化计算最小代价
1368. 使网格图至少有一条有效路径的最小代价（https://leetcode.cn/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/）使用0-1 BFS进行优化计算最小代价
2258. 逃离火灾（https://leetcode.cn/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/）使用二分查找加双源BFS进行模拟
2092. 找出知晓秘密的所有专家（https://leetcode.cn/problems/find-all-people-with-secret/）按照时间排序，在同一时间进行BFS扩散
6330. 图中的最短环（https://leetcode.cn/contest/biweekly-contest-101/problems/shortest-cycle-in-a-graph/）使用BFS求无向图的最短环，还可以删除边计算两点最短路成为环，或者以任意边为起点，逐渐加边
1197. 进击的骑士（https://leetcode.cn/problems/minimum-knight-moves/?envType=study-plan-v2&id=premium-algo-100）双向BFS

===================================洛谷===================================
P1747 好奇怪的游戏（https://www.luogu.com.cn/problem/P1747）双向BFS搜索最短距离
P5507 机关（https://www.luogu.com.cn/problem/P5507）双向BFS进行搜索
P2040 打开所有的灯（https://www.luogu.com.cn/problem/P2040）定义状态进行 BFS 搜索
P2335 [SDOI2005]位图（https://www.luogu.com.cn/problem/P2335）广度优先搜索
P2385 [USACO07FEB]Bronze Lilypad Pond B（https://www.luogu.com.cn/problem/P2385）广度优先搜索最短步数
P2630 图像变换（https://www.luogu.com.cn/problem/P2630）BFS模拟计算最短次数与最小字典序
P1332 血色先锋队（https://www.luogu.com.cn/problem/P1332）标准BFS
P1330 封锁阳光大学（https://www.luogu.com.cn/problem/P1330）BFS进行隔层染色取较小值，也可以判断连通块是否存在奇数环
P1215 [USACO1.4]母亲的牛奶 Mother's Milk（https://www.luogu.com.cn/problem/P1215）广度优先搜索进行模拟与状态记录
P1037 [NOIP2002 普及组] 产生数（https://www.luogu.com.cn/problem/P1037）广度优先搜索之后进行模拟和枚举
P2853 [USACO06DEC]Cow Picnic S（https://www.luogu.com.cn/problem/P2853）广度优先搜索进行可达计数
P2881 [USACO07MAR]Ranking the Cows G（https://www.luogu.com.cn/problem/P2881）广搜确定已知所有祖先，总共应有n*(n-1)//2对顺序
P2895 [USACO08FEB]Meteor Shower S（https://www.luogu.com.cn/problem/P2895）广度优先搜索模拟
P2960 [USACO09OCT]Invasion of the Milkweed G（https://www.luogu.com.cn/problem/P2960）广度优先搜索裸题
P2298 Mzc和男家丁的游戏（https://www.luogu.com.cn/problem/P2298）BFS裸题
P3139 [USACO16FEB]Milk Pails S（https://www.luogu.com.cn/problem/P3139）广搜加记忆化
P3183 [HAOI2016] 食物链（https://www.luogu.com.cn/problem/P3183）广搜计数计算路径条数，也可以使用深搜DP计数
P4017 最大食物链计数（https://www.luogu.com.cn/problem/P4017）广搜计数计算路径条数，也可以使用深搜DP计数
P3395 路障（https://www.luogu.com.cn/problem/P3395）广度优先搜索进行模拟
P3416 [USACO16DEC]Moocast S（https://www.luogu.com.cn/problem/P3416）广搜加记忆化访问
P3916 图的遍历（https://www.luogu.com.cn/problem/P3916）逆向思维反向建图再加倒序访问传播
P3958 [NOIP2017 提高组] 奶酪（https://www.luogu.com.cn/problem/P3958）建图之后进行广度优先搜索
P4328 [COCI2006-2007#1] Slikar（https://www.luogu.com.cn/problem/P4328）经典广搜题，模拟能否逃离火灾或者洪水
P4961 小埋与扫雷（https://www.luogu.com.cn/problem/P4961）枚举模拟计数，八连通
P6207 [USACO06OCT] Cows on Skates G（https://www.luogu.com.cn/problem/P6207）经典广度优先搜索记录最短路径
P6582 座位调查（https://www.luogu.com.cn/problem/P6582）bfs合法性判断与组合计数快速幂
P7243 最大公约数（https://www.luogu.com.cn/problem/P7243）广度优先搜索加gcd最大公约数计算
P3496 [POI2010]GIL-Guilds（https://www.luogu.com.cn/problem/P3496）脑筋急转弯，BFS隔层染色
P1432 倒水问题（https://www.luogu.com.cn/problem/P1432）经典BFS倒水题，使用记忆化广搜
P1807 最长路（https://www.luogu.com.cn/problem/P1807）不保证连通的有向无环图求 1 到 n 的最长路
P1379 八数码难题（https://www.luogu.com.cn/problem/P1379）双向BFS
P5507 机关（https://www.luogu.com.cn/problem/P5507）双向BFS或者A-star启发式搜索
P5908 猫猫和企鹅（https://www.luogu.com.cn/problem/P5908）无根树直接使用bfs遍历
P1099 [NOIP2007 提高组] 树网的核（https://www.luogu.com.cn/problem/P1099）经典题，用到了树的直径、BFS、双指针和单调队列求最小偏心距
P2491 [SDOI2011] 消防（https://www.luogu.com.cn/problem/P2491）同树网的核P1099
P1038 [NOIP2003 提高组] 神经网络（https://www.luogu.com.cn/problem/P1038）拓扑排序经典题
P1126 机器人搬重物（https://www.luogu.com.cn/problem/P1126）广度优先搜索
P1213 [USACO1.4][IOI1994]时钟 The Clocks（https://www.luogu.com.cn/problem/P1213）使用状态压缩优化进行01BFS
P1902 刺杀大使（https://www.luogu.com.cn/problem/P1902）二分加BFS与原地哈希计算路径最大值的最小值
P2199 最后的迷宫（https://www.luogu.com.cn/problem/P2199）队列01BFS判定距离最近的可视范围
P2226 [HNOI2001]遥控赛车比赛（https://www.luogu.com.cn/problem/P2226）有限制地BDS转向计算

================================CodeForces================================
E. Nearest Opposite Parity（https://codeforces.com/problemset/problem/1272/E）经典反向建图，多源BFS
A. Book（https://codeforces.com/problemset/problem/1572/A）脑筋急转弯建图，广度优先搜索计算是否存在环与无环时从任意起点的DAG最长路
D. Valid BFS?（https://codeforces.com/problemset/problem/1037/D）经典BDS好题，结合队列与集合进行模拟
P6175 无向图的最小环问题（https://www.luogu.com.cn/problem/P6175）经典使用Floyd枚举三个点之间的距离和，O(n^3)，也可以使用BFS或者Dijkstra计算

================================AcWing================================
173. 矩阵距离（https://www.acwing.com/problem/content/175/）多源BFS模板题
175. 电路维修（https://www.acwing.com/problem/content/177/）双端优先队列 BFS
177. 噩梦（https://www.acwing.com/problem/content/179/）多源双向BFS

参考：OI WiKi（xx）
"""


class Solution:
    def __init__(self):
        return

    @staticmethod
    def lc_6330_1(n: int, edges: List[List[int]]) -> int:

        # 模板：求无向图的最小环
        graph = [[] for _ in range(n)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        inf = float("inf")
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
    def lc_6330_2(n: int, edges: List[List[int]]) -> int:

        # 模板：求无向图的最小环
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
    def lc_6330_3(n: int, edges: List[List[int]]) -> int:
        # 模板：求无向图的最小环
        inf = float('inf')
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)  # 建图

        def bfs(start: int) -> int:
            nonlocal inf
            dis = [-1] * n  # dis[i] 表示从 start 到 i 的最短路长度
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
                        # 由于是 BFS，后面不会遇到更短的环，直接返回
                        res = res if res < dis[x] + dis[y] + 1 else dis[x] + dis[y] + 1
            return res  # 该连通分量无环

        ans = min(bfs(i) for i in range(n))
        return ans if ans < inf else -1

    @staticmethod
    def lc_6330_4(n: int, edges: List[List[int]]) -> int:
        # 模板：求无向图的最小环，枚举边
        graph = [set() for _ in range(n)]
        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)

        inf = float("inf")
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
        # 模板：有向无环图 DAG 使用拓扑排序求最长路
        n, m = ac.read_ints()
        edge = [dict() for _ in range(n)]
        pre = [set() for _ in range(n)]
        for _ in range(m):
            u, v, w = ac.read_ints()
            u -= 1
            v -= 1
            edge[u][v] = ac.max(edge[u].get(v, -ac.inf), w)
            pre[v].add(u)

        # 注意这里可能有 0 之外的入度为 0 的点，需要先进行拓扑消除
        stack = deque([i for i in range(1, n) if not pre[i]])
        while stack:
            i = stack.popleft()
            for j in edge[i]:
                pre[j].discard(i)
                if not pre[j]:
                    stack.append(j)

        # 广搜计算最长路，进一步还可以确定相应的具体路径
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
        # 模板：有向无环图 DAG 使用深搜求最长路
        n, m = ac.read_ints()
        edge = [dict() for _ in range(n)]
        for _ in range(m):
            u, v, w = ac.read_ints()
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
        # 模板：反向建图与多源 BFS 计算
        n = ac.read_int()
        nums = ac.read_list_ints()
        ans = [-1] * n

        edge = [[] for _ in range(n)]
        for i in range(n):
            for x in [i + nums[i], i - nums[i]]:
                if 0 <= x < n:
                    edge[x].append(i)

        # 多源 BFS
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
        # 模板: 计算有向无环图路径条数
        n, m = ac.read_ints()
        edge = [[] for _ in range(n)]
        degree = [0] * n
        out_degree = [0] * n
        for _ in range(m):
            i, j = ac.read_ints_minus_one()
            edge[i].append(j)
            degree[j] += 1
            out_degree[i] += 1
        ind = [i for i in range(n) if degree[i] and not out_degree[i]]
        cnt = [0]*n
        stack = [i for i in range(n) if not degree[i]]
        for x in stack:
            cnt[x] = 1
        while stack:  # 也可以使用深搜
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
        # 模板：双向 BFS 搜索
        x0, y0 = ac.read_ints()
        x2, y2 = ac.read_ints()

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
        # 模板：使用队列实现0-1 BFS 即优先选择距离较短的路线
        m, n = len(grid), len(grid[0])
        visit = [[0] * n for _ in range(m)]
        q = deque([(0, 0, 0)])
        while q:
            # 也可以使用 Dijkstra 进行求解
            d, x, y = q.popleft()
            for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= nx < m and 0 <= ny < n and not visit[nx][ny]:
                    if [nx, ny] == [m-1, n-1]:
                        return d + grid[nx][ny]
                    visit[nx][ny] = 1
                    if not grid[nx][ny]:
                        q.appendleft((d, nx, ny))
                    else:
                        q.append((d + 1, nx, ny))

    @staticmethod
    def lc_1368(grid: List[List[int]]) -> int:
        # 模板：使用队列实现0-1 BFS 即优先选择距离较短的路线
        m, n = len(grid), len(grid[0])
        ceil = int(1e9)
        dist = [0] + [ceil] * (m * n - 1)
        seen = set()
        q = deque([(0, 0)])

        while q:
            # 也可以使用 Dijkstra 进行求解
            x, y = q.popleft()
            if (x, y) in seen:
                continue
            seen.add((x, y))
            cur_pos = x * n + y
            for i, (nx, ny) in enumerate([(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]):
                new_pos = nx * n + ny
                new_dis = dist[cur_pos] + (1 if grid[x][y] != i + 1 else 0)
                if 0 <= nx < m and 0 <= ny < n and new_dis < dist[new_pos]:
                    dist[new_pos] = new_dis
                    if grid[x][y] == i + 1:
                        q.appendleft((nx, ny))
                    else:
                        q.append((nx, ny))
        return dist[m * n - 1]

    @staticmethod
    def cf_1572a(ac=FastIO()):
        # 模板：BFS 判断 DAG 是否有环和无环时的最长路（注意起点可能有多个）
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
                        # 拓扑排序的同时更新最长路
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
        # 模板：使用队列与集合判断 bfs序 即广搜序
        n = ac.read_int()
        edge = [[] for _ in range(n)]
        for _ in range(n - 1):
            i, j = ac.read_ints_minus_one()
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
        # 模板：求最小偏心距在树的直径上进行双指针与单调队列计算
        n, s = ac.read_ints()
        dct = [dict() for _ in range(n)]
        for _ in range(n-1):
            i, j, w = ac.read_ints()
            dct[i-1][j-1] = w
            dct[j-1][i-1] = w

        def bfs_diameter(src):
            res, node = 0, src
            stack = [[src, 0]]
            parent = [-1]*n
            while stack:
                u, dis = stack.pop()
                if dis > res:
                    res = dis
                    node = u
                for v in dct[u]:
                    if v != parent[u]:
                        parent[v] = u
                        stack.append([v, dis+dct[u][v]])
            pa = [node]
            while parent[pa[-1]] != -1:
                pa.append(parent[pa[-1]])
            pa.reverse()
            return node, pa

        # 计算直径与路径
        start, _ = bfs_diameter(0)
        end, path = bfs_diameter(start)

        def bfs_distance(src):
            dis = [0]*n
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
                            x = ac.max(x, dct[u][v]+dis[v])
                    dis[u] = x
            return dis

        # 计算直径上的端点往 start 与往 end 方向的最长距离
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
                        stack.append([v, u, dis+dct[u][v]])
            diameter[src] = res
            return

        # 计算直径上的端点往非直径端点上的最远距离
        diameter = {node: 0 for node in path}
        for node in diameter:
            bfs_node(node)

        # 使用双指针加滑动窗口单调队列记录直径范围点往非直径方向延申的最远距离
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
                gap -= dct[path[i-1]][path[i]]

            # 双指针与单调队列
            while j+1 < m and gap + dct[path[j]][path[j+1]] <= s:
                gap += dct[path[j]][path[j + 1]]
                while q and q[-1][0] < diameter[path[j+1]]:
                    q.pop()
                q.append([diameter[path[j+1]], j+1])
                j += 1

            ans = ac.min(ans, max(dis2[path[i]], dis1[path[j]], q[0][0]))
        ac.st(ans)
        return

    @staticmethod
    def ac_173(ac=FastIO()):
        # 模板：多源BFS模板题
        m, n = ac.read_ints()
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
                for x, y in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
                    if 0<=x<m and 0<=y<n and grid[x][y] == inf:
                        nex.append([x, y])
                        grid[x][y] = grid[i][j] + 1
            stack = nex[:]
        for g in grid:
            ac.lst(g)
        return

    @staticmethod
    def ac_175(ac=FastIO()):
        for _ in range(ac.read_int()):

            # 模板：经典双端优先队列 01 BFS模板题注意建图
            m, n = ac.read_ints()
            grid = [ac.read_str() for _ in range(m)]
            k = (m+1)*(n+1)
            dct = [dict() for _ in range(k)]
            for i in range(m):
                for j in range(n):
                    x1, y1 = i, j
                    x2, y2 = i, j+1
                    x3, y3 = i+1, j
                    x4, y4 = i+1, j+1
                    if grid[i][j] == "/":
                        dct[x1*(n+1)+y1][x4*(n+1)+y4] = 1
                        dct[x4 * (n + 1) + y4][x1 * (n + 1) + y1] = 1
                        dct[x2 * (n + 1) + y2][x3 * (n + 1) + y3] = 0
                        dct[x3 * (n + 1) + y3][x2 * (n + 1) + y2] = 0
                    else:
                        dct[x1 * (n + 1) + y1][x4 * (n + 1) + y4] = 0
                        dct[x4 * (n + 1) + y4][x1 * (n + 1) + y1] = 0
                        dct[x2 * (n + 1) + y2][x3 * (n + 1) + y3] = 1
                        dct[x3 * (n + 1) + y3][x2 * (n + 1) + y2] = 1

            visit = [inf]*(k)
            stack = deque([0])
            visit[0] = 0
            while stack:
                i = stack.popleft()
                for j in dct[i]:
                    dd = dct[i][j] + visit[i]
                    if visit[j] > dd:
                        visit[j] = dd
                        if dd == visit[i]:
                            stack.appendleft(j)
                        else:
                            stack.append(j)
            ac.st(visit[-1] if visit[-1] < inf else "NO SOLUTION")
        return

    @staticmethod
    def ac_177(ac=FastIO()):
        for _ in range(ac.read_int()):
            # 模板：多源双向BFS
            m, n = ac.read_ints()
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
                        for x, y in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
                            if 0<=x<m and 0<=y<n and dis_ghost[x][y] == inf:
                                dis_ghost[x][y] = pre
                                nex_ghost.append([x, y])
                    stack_ghost = nex_ghost[:]

                for _ in range(3):
                    nex_boy = []
                    for i, j in stack_boy:
                        if dis_ghost[i][j] == inf:
                            for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                                if 0 <= x < m and 0 <= y < n and dis_boy[x][y] == inf and grid[x][y] != "X" and dis_ghost[x][y]==inf:
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
        # 模板：使用状态压缩优化进行01BFS
        nex = {0:1, 1:2, 2:3, 3:0}
        lst = "ABDE,ABC,BCEF,ADG,BDEFH,CFI,DEGH,GHI,EFHI".split(",")
        ind = dict()
        for i, st in enumerate(lst):
            ind[i + 1] = [ord(w) - ord("A") for w in st]

        grid = []
        for _ in range(3):
            grid.extend([(num-3)//3 for num in ac.read_list_ints()])

        def list_to_num(ls):
            res = 0
            for num in ls:
                res *= 4
                res += num
            return res

        def num_to_list(num):
            res = []
            while num:
                res.append(num%4)
                num //= 4
            while len(res) < 9:
                res.append(0)
            return res[::-1]

        ans = ""
        start = list_to_num(grid)
        target = list_to_num([3]*9)

        stack = deque([start])
        visit= dict()
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
                if len(pre) < len(ans) or (len(pre)==len(ans) and pre < ans) or not ans:
                    ans = pre
                continue

            state = num_to_list(state)
            for i in range(9):
                tmp = state[:]
                for w in ind[i+1]:
                    tmp[w] = nex[tmp[w]]
                cur = list_to_num(tmp)
                if cur not in visit:
                    visit[cur] = pre+str(i+1)
                    stack.append(cur)
        ac.lst(list(ans))
        return

    @staticmethod
    def lg_p1902(ac=FastIO()):
        # 模板：二分加BFS与原地哈希计算路径最大值的最小值
        m, n = ac.read_ints()
        grid = [ac.read_list_ints() for _ in range(m)]
        for j in range(n):
            grid[0][j] = -grid[0][j] - 1
        dct = dict()

        def check(x):
            # 使用原地哈希节省空间
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
            # 原地哈希复原
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

        # 模板：队列01BFS判定距离最近的可视范围
        m, n = ac.read_ints()
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

            # 01BFS队列
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
        # 模板：有限制地BDS转向计算
        m, n = ac.read_ints()
        s1, s2, e1, e2 = ac.read_ints_minus_one()
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


class TestGeneral(unittest.TestCase):

    def test_xxx(self):
        pass
        return


if __name__ == '__main__':
    unittest.main()
