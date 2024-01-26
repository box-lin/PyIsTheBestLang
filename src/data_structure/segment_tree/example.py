import random
import unittest
from functools import reduce
from operator import or_, xor

from src.data_structure.segment_tree.template import RangeAscendRangeMax, \
    RangeDescendRangeMin, \
    RangeAddRangeSumMinMax, RangeSetRangeSumMinMax, RangeSetRangeMaxNonEmpConSubSum, \
    RangeOrRangeAnd, \
    RangeSetRangeSumMinMaxDynamic, RangeSetRangeOr, RangeAffineRangeSum, RangeAddMulRangeSum, \
    RangeSetAddRangeMax, RangeXorUpdateRangeXorQuery, RangeSetReverseRangeSumLongestConSub, PointSetRangeMinCount, \
    RangeAddPointGet


class TestGeneral(unittest.TestCase):

    def test_range_add_point_get(self):
        low = 1
        high = 100
        n = 100
        nums = [random.randint(low, high) for _ in range(n)]
        segment_tree = RangeAddPointGet(n)
        segment_tree.build(nums)
        for _ in range(10000):
            ll = random.randint(0, n - 1)
            rr = random.randint(ll, n - 1)
            num = random.randint(low, high)
            for i in range(ll, rr + 1):
                nums[i] += num
            segment_tree.range_add(ll, rr, num)
        assert nums == segment_tree.get() == [segment_tree.point_get(i) for i in range(n)]
        return

    def test_point_set_range_min_count(self):
        low = 1
        high = 100
        n = 100
        nums = [random.randint(low, high) for _ in range(n)]
        segment_tree = PointSetRangeMinCount(n, 0)
        segment_tree.build(nums)
        for _ in range(10000):
            i = random.randint(0, n - 1)
            num = random.randint(low, high)
            nums[i] = num
            segment_tree.point_set(i, num)

            ll = random.randint(0, n - 1)
            rr = random.randint(ll, n - 1)
            low = min(nums[ll:rr + 1])
            cnt = nums[ll:rr + 1].count(low)
            res = segment_tree.range_min_count(ll, rr)
            assert res == (low, cnt)
        assert nums == segment_tree.get()
        return

    def test_range_or_range_and(self):
        low = 0
        high = (1 << 31) - 1
        n = 1000
        nums = [random.randint(low, high) for _ in range(n)]
        segment_tree = RangeOrRangeAnd(n)
        segment_tree.build(nums)
        for _ in range(1000):
            ll = random.randint(0, n - 1)
            rr = random.randint(ll, n - 1)
            num = random.randint(low, high)
            for i in range(ll, rr + 1):
                nums[i] |= num
            segment_tree.range_or(ll, rr, num)

            ll = random.randint(0, n - 1)
            rr = random.randint(ll, n - 1)
            res = high
            for i in range(ll, rr + 1):
                res &= nums[i]
            assert res == segment_tree.range_and(ll, rr)
        assert nums == segment_tree.get()
        return

    def test_range_ascend_range_max(self):
        low = 0
        high = 10000
        nums = [random.randint(low, high) for _ in range(high)]
        segment_tree = RangeAscendRangeMax(high)
        segment_tree.build(nums)
        assert segment_tree.get() == nums
        for _ in range(high):
            # 区间更新最大值
            left = random.randint(0, high - 1)
            right = random.randint(left, high - 1)
            num = random.randint(low, high)
            segment_tree.range_ascend(left, right, num)
            for i in range(left, right + 1):
                nums[i] = nums[i] if nums[i] > num else num
            left = random.randint(0, high - 1)
            right = random.randint(left, high - 1)
            assert segment_tree.range_max(left, right) == max(nums[left:right + 1])

            # 单点更新最大值
            left = random.randint(0, high - 1)
            right = left
            num = random.randint(low, high)
            segment_tree.range_ascend(left, right, num)
            for i in range(left, right + 1):
                nums[i] = nums[i] if nums[i] > num else num
            assert segment_tree.range_max(left, right) == max(nums[left:right + 1])

            left = random.randint(0, high - 1)
            right = random.randint(left, high - 1)
            assert segment_tree.range_max(left, right) == max(nums[left:right + 1])
        assert segment_tree.get() == nums
        return

    def test_range_descend_range_min(self):
        low = 0
        high = 10000
        nums = [random.randint(low, high) for _ in range(high)]
        segment_tree = RangeDescendRangeMin(high)
        segment_tree.build(nums)

        for _ in range(high):
            # 区间更新与查询最小值
            left = random.randint(0, high - 1)
            right = random.randint(left, high - 1)
            num = random.randint(low, high)
            segment_tree.range_descend(left, right, num)
            for i in range(left, right + 1):
                nums[i] = nums[i] if nums[i] < num else num
            left = random.randint(0, high - 1)
            right = random.randint(left, high - 1)
            assert segment_tree.range_min(left, right) == min(nums[left:right + 1])

            # 单点更新与查询最小值
            left = random.randint(0, high - 1)
            right = left
            num = random.randint(low, high)
            segment_tree.range_descend(left, right, num)
            for i in range(left, right + 1):
                nums[i] = nums[i] if nums[i] < num else num
            assert segment_tree.range_min(left, right) == min(nums[left:right + 1])

            left = random.randint(0, high - 1)
            right = random.randint(left, high - 1)
            assert segment_tree.range_min(left, right) == min(nums[left:right + 1])

        assert segment_tree.get() == nums
        return

    def test_range_add_range_sum_min_max(self):
        low = -10000
        high = 10000
        nums = [random.randint(low, high) for _ in range(high)]
        segment_tree = RangeAddRangeSumMinMax(high)
        segment_tree.build(nums)

        assert segment_tree.range_min(0, high - 1) == min(nums)
        assert segment_tree.range_max(0, high - 1) == max(nums)
        assert segment_tree.range_sum(0, high - 1) == sum(nums)

        for _ in range(high):

            left = random.randint(0, high - 1)
            right = random.randint(left, high - 1)
            num = random.randint(-high, high)
            segment_tree.range_add(left, right, num)
            for i in range(left, right + 1):
                nums[i] += num
            left = random.randint(0, high - 1)
            right = random.randint(left, high - 1)
            assert segment_tree.range_min(left, right) == min(
                nums[left:right + 1])
            assert segment_tree.range_max(left, right) == max(
                nums[left:right + 1])
            assert segment_tree.range_sum(left, right) == sum(
                nums[left:right + 1])

            left = random.randint(0, high - 1)
            right = left
            num = random.randint(-high, high)
            segment_tree.range_add(left, right, num)
            for i in range(left, right + 1):
                nums[i] += num
            assert segment_tree.range_min(left, right) == min(
                nums[left:right + 1])
            assert segment_tree.range_max(left, right) == max(
                nums[left:right + 1])
            assert segment_tree.range_sum(left, right) == sum(
                nums[left:right + 1])

        assert segment_tree.get() == nums
        return

    def test_range_change_reverse_range_sum_longest_con_sub_sum(self):
        random.seed(2023)
        high = 10000
        nums = [random.randint(0, 1) for _ in range(high)]
        segment_tree = RangeSetReverseRangeSumLongestConSub(high)
        segment_tree.build(nums)

        def check(tmp):
            ans = pre = 0
            for x in tmp:
                if x:
                    pre += 1
                else:
                    ans = ans if ans > pre else pre
                    pre = 0
            ans = ans if ans > pre else pre
            return ans

        assert segment_tree.range_sum(0, high - 1) == sum(nums)
        assert segment_tree.get() == nums
        for _ in range(100):
            op = random.randint(0, 4)
            left = random.randint(0, high - 1)
            right = random.randint(left, high - 1)
            assert segment_tree.get() == nums
            if op == 0:
                segment_tree.range_change_reverse(left, right, op)
                for i in range(left, right + 1):
                    nums[i] = 0
            elif op == 1:
                segment_tree.range_change_reverse(left, right, op)
                for i in range(left, right + 1):
                    nums[i] = 1
            elif op == 2:
                segment_tree.range_change_reverse(left, right, op)
                for i in range(left, right + 1):
                    nums[i] = 1 - nums[i]
            elif op == 3:
                assert segment_tree.range_sum(left, right) == sum(nums[left:right + 1])
            else:
                assert segment_tree.range_longest_con_sub(left, right) == check(nums[left:right + 1])
        assert segment_tree.get() == nums
        return

    def test_range_xor_update_range_xor_query(self):
        low = 0
        high = 10000
        nums = [random.randint(low, high) for _ in range(high)]
        segment_tree = RangeXorUpdateRangeXorQuery(high)
        segment_tree.build(nums)

        assert segment_tree.range_xor_query(0, high - 1) == reduce(xor, nums)

        for _ in range(high):

            left = random.randint(0, high - 1)
            right = random.randint(left, high - 1)
            num = random.randint(0, high)
            segment_tree.range_xor_update(left, right, num)
            for i in range(left, right + 1):
                nums[i] ^= num
            left = random.randint(0, high - 1)
            right = random.randint(left, high - 1)

            assert segment_tree.range_xor_query(left, right) == reduce(xor, nums[left:right + 1])

        assert segment_tree.get() == nums
        return

    def test_range_change_add_range_max(self):
        low = -10 ** 9
        high = 10 ** 9

        for _ in range(100):
            n = random.randint(1000, 10 ** 4)
            nums = [random.randint(low, high) for _ in range(n)]
            segment_tree = RangeSetAddRangeMax(n)
            segment_tree.build(nums)
            assert segment_tree.range_max(0, high - 1) == max(nums)

            for _ in range(100):

                left = random.randint(0, n - 1)
                right = random.randint(left, n - 1)
                num = random.randint(low, high)
                segment_tree.range_change_add(left, right, segment_tree.add_to_mask(num))
                for i in range(left, right + 1):
                    nums[i] += num
                left = random.randint(0, n - 1)
                right = random.randint(left, n - 1)
                assert segment_tree.range_max(left, right) == max(
                    nums[left:right + 1])

                left = random.randint(0, n - 1)
                right = random.randint(left, n - 1)
                num = random.randint(low, high)
                segment_tree.range_change_add(left, right, segment_tree.change_to_mask(num))
                for i in range(left, right + 1):
                    nums[i] = num
                left = random.randint(0, n - 1)
                right = random.randint(left, n - 1)
                assert segment_tree.range_max(left, right) == max(nums[left:right + 1])

            assert segment_tree.get() == nums
        return

    def test_range_add_mul_range_sum(self):
        low = -10000
        high = 10000
        mod = 10 ** 9 + 7
        nums = [random.randint(low, high) % mod for _ in range(high)]
        segment_tree = RangeAddMulRangeSum(high, mod)
        segment_tree.build(nums)

        assert segment_tree.range_sum(0, high - 1) == sum(nums) % mod

        for _ in range(high):

            left = random.randint(0, high - 1)
            right = random.randint(left, high - 1)
            num = random.randint(-high, high)
            segment_tree.range_add_mul(left, right, num, "add")
            for i in range(left, right + 1):
                nums[i] += num
                nums[i] %= mod
            left = random.randint(0, high - 1)
            right = random.randint(left, high - 1)
            assert segment_tree.range_sum(left, right) == sum(
                nums[left:right + 1]) % mod

            left = random.randint(0, high - 1)
            right = left
            num = random.randint(-high, high)
            segment_tree.range_add_mul(left, right, num, "mul")
            for i in range(left, right + 1):
                nums[i] *= num
                nums[i] %= mod
            assert segment_tree.range_sum(left, right) == sum(
                nums[left:right + 1]) % mod

        ans = [segment_tree.range_sum(i, i) for i in range(high)]
        assert segment_tree.get() == nums == ans
        return

    def test_range_affine_range_sum(self):
        low = -10000
        high = 10000
        mod = 10 ** 9 + 7
        nums = [random.randint(low, high) % mod for _ in range(high)]
        segment_tree = RangeAffineRangeSum(high, mod)
        segment_tree.build(nums)

        assert segment_tree.range_sum(0, high - 1) == sum(nums) % mod

        for _ in range(high):

            left = random.randint(0, high - 1)
            right = random.randint(left, high - 1)
            num = random.randint(1, high)
            segment_tree.range_affine(left, right, (1 << 32) | num)
            for i in range(left, right + 1):
                nums[i] += num
                nums[i] %= mod
            left = random.randint(0, high - 1)
            right = random.randint(left, high - 1)
            assert segment_tree.range_sum(left, right) == sum(
                nums[left:right + 1]) % mod

            left = random.randint(0, high - 1)
            right = left
            num = random.randint(1, high)
            segment_tree.range_affine(left, right, num << 32)
            for i in range(left, right + 1):
                nums[i] *= num
                nums[i] %= mod
            assert segment_tree.range_sum(left, right) == sum(
                nums[left:right + 1]) % mod

        ans = [segment_tree.range_sum(i, i) for i in range(high)]
        assert segment_tree.get() == nums == ans
        return

    def test_range_change_range_sum_min_max(self):
        low = -10000
        high = 10000
        n = 10000
        nums = [random.randint(low, high) for _ in range(n)]
        segment_tree = RangeSetRangeSumMinMax(n)
        segment_tree.build(nums)
        assert segment_tree.range_min(0, n - 1) == min(nums)
        assert segment_tree.range_max(0, n - 1) == max(nums)
        assert segment_tree.range_sum(0, n - 1) == sum(nums)
        assert segment_tree.get() == nums

        for _ in range(high):
            left = random.randint(0, high - 1)
            right = random.randint(left, high - 1)
            num = random.randint(-high, high)
            segment_tree.range_change(left, right, num)
            for i in range(left, right + 1):
                nums[i] = num
            left = random.randint(0, high - 1)
            right = random.randint(left, high - 1)
            assert segment_tree.range_min(left, right) == min(
                nums[left:right + 1])
            assert segment_tree.range_max(left, right) == max(
                nums[left:right + 1])
            assert segment_tree.range_sum(left, right) == sum(
                nums[left:right + 1])

            left = random.randint(0, high - 1)
            right = left
            num = random.randint(-high, high)
            segment_tree.range_change(left, right, num)
            for i in range(left, right + 1):
                nums[i] = num
            assert segment_tree.range_min(left, right) == min(
                nums[left:right + 1])
            assert segment_tree.range_max(left, right) == max(
                nums[left:right + 1])
            assert segment_tree.range_sum(left, right) == sum(
                nums[left:right + 1])

            left = random.randint(0, high - 1)
            right = random.randint(left, high - 1)
            assert segment_tree.range_min(left, right) == min(
                nums[left:right + 1])
            assert segment_tree.range_max(left, right) == max(
                nums[left:right + 1])
            assert segment_tree.range_sum(left, right) == sum(
                nums[left:right + 1])

        assert segment_tree.get() == nums
        return

    def test_range_change_range_or(self):
        low = 0
        high = 10000
        n = 10000
        nums = [random.randint(low, high) for _ in range(n)]
        segment_tree = RangeSetRangeOr(n)
        segment_tree.build(nums)

        for _ in range(high):
            # 区间修改
            left = random.randint(0, high - 1)
            right = random.randint(left, high - 1)
            num = random.randint(0, high)
            segment_tree.range_change(left, right, num)
            for i in range(left, right + 1):
                nums[i] = num
            left = random.randint(0, high - 1)
            right = random.randint(left, high - 1)
            assert segment_tree.range_or(left, right) == reduce(or_, nums[left:right + 1])

        assert segment_tree.get() == nums
        return

    def test_range_change_range_sum_min_max_dynamic(self):
        high = 10000
        n = 10000
        nums = [0] * n
        segment_tree = RangeSetRangeSumMinMaxDynamic(n)

        for _ in range(high):
            left = random.randint(0, high - 1)
            right = random.randint(left, high - 1)
            num = random.randint(-high, high)
            segment_tree.range_change(left, right, num)
            for i in range(left, right + 1):
                nums[i] = num
            left = random.randint(0, high - 1)
            right = random.randint(left, high - 1)
            assert segment_tree.range_min(left, right) == min(
                nums[left:right + 1])
            assert segment_tree.range_max(left, right) == max(
                nums[left:right + 1])
            assert segment_tree.range_sum(left, right) == sum(
                nums[left:right + 1])

            left = random.randint(0, high - 1)
            right = left
            num = random.randint(-high, high)
            segment_tree.range_change(left, right, num)
            for i in range(left, right + 1):
                nums[i] = num
            assert segment_tree.range_min(left, right) == min(
                nums[left:right + 1])
            assert segment_tree.range_max(left, right) == max(
                nums[left:right + 1])
            assert segment_tree.range_sum(left, right) == sum(
                nums[left:right + 1])

            left = random.randint(0, high - 1)
            right = random.randint(left, high - 1)
            assert segment_tree.range_min(left, right) == min(
                nums[left:right + 1])
            assert segment_tree.range_max(left, right) == max(
                nums[left:right + 1])
            assert segment_tree.range_sum(left, right) == sum(
                nums[left:right + 1])
        assert segment_tree.range_min(0, n - 1) == min(nums)
        assert segment_tree.range_max(0, n - 1) == max(nums)
        assert segment_tree.range_sum(0, n - 1) == sum(nums)
        return

    def test_range_change_range_max_non_emp_son_sub_sum(self):

        def check(lst):
            pre = ans = lst[0]
            for x in lst[1:]:
                pre = pre + x if pre + x > x else x
                ans = ans if ans > pre else pre
            return ans

        low = 0
        high = 10000
        nums = [random.randint(low, high) for _ in range(high)]
        segment_tree = RangeSetRangeMaxNonEmpConSubSum(high, high)
        segment_tree.build(nums)
        assert segment_tree.range_max_non_emp_con_sub_sum(0, high - 1) == check(nums)
        assert segment_tree.get() == nums
        for _ in range(100):
            left = random.randint(0, high - 1)
            right = random.randint(left, high - 1)
            num = random.randint(-high, high)
            segment_tree.range_change(left, right, num)
            for i in range(left, right + 1):
                nums[i] = num
            left = random.randint(0, high - 1)
            right = random.randint(left, high - 1)
            assert segment_tree.get() == nums
            assert segment_tree.range_max_non_emp_con_sub_sum(left, right) == check(nums[left:right + 1])
        return


if __name__ == '__main__':
    unittest.main()
