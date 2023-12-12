"""
Algorithm：peishu_theorem
Description：ax+by=gcd(a,b)  a!=0 or b!=0

====================================LeetCode====================================
1250（https://leetcode.cn/problems/check-if-it-is-a-good-array/）gcd|peishu_theorem|classical

===================================CodeForces===================================
1478D（https://codeforces.com/contest/1478/problem/D）peishu_theorem|number_theory|math

=====================================LuoGu======================================
P4549（https://www.luogu.com.cn/problem/P4549）gcd|peishu_theorem


"""

from typing import List

from src.mathmatics.peishu_theorem.template import PeiShuTheorem
from src.utils.fast_io import FastIO


class Solution:
    def __init__(self):
        return

    @staticmethod
    def lc_1250(nums: List[int]) -> bool:
        """
        url: https://leetcode.cn/problems/check-if-it-is-a-good-array/
        tag: gcd|peishu_theorem|classical
        """
        # 转化为peishu_theorem|数组最大公约数是否等于 1 求解
        return PeiShuTheorem().get_lst_gcd(nums) == 1

    @staticmethod
    def lg_p4549(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P4549
        tag: gcd|peishu_theorem
        """
        # 转化为peishu_theorem|数组最大公约数求解
        ac.read_int()
        nums = ac.read_list_ints()
        ac.st(PeiShuTheorem().get_lst_gcd(nums))
        return