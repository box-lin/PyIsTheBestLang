from functools import reduce


class CRT:
    def __init__(self):
        return

    def chinese_remainder(self, pairs):
        """中国剩余定理"""
        mod_list, remainder_list = [p[0] for p in pairs], [p[1] for p in pairs]
        mod_product = reduce(lambda x, y: x * y, mod_list)
        mi_list = [mod_product // x for x in mod_list]
        mi_inverse = [ExtendCRT().exgcd(mi_list[i], mod_list[i])[0] for i in range(len(mi_list))]
        x = 0
        for i in range(len(remainder_list)):
            x += mi_list[i] * mi_inverse[i] * remainder_list[i]
            x %= mod_product
        return x


class ExtendCRT:
    # 在模数不coprime的情况下，最小的非负整数解
    def __init__(self):
        return

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def lcm(self, a, b):
        return a * b // self.gcd(a, b)

    def exgcd(self, a, b):
        if b == 0:
            return 1, 0
        x, y = self.exgcd(b, a % b)
        return y, x - a // b * y

    def uni(self, p, q):
        r1, m1 = p
        r2, m2 = q

        d = self.gcd(m1, m2)
        assert (r2 - r1) % d == 0
        # 否则无解
        l1, l2 = self.exgcd(m1 // d, m2 // d)

        return (r1 + (r2 - r1) // d * l1 * m1) % self.lcm(m1, m2), self.lcm(m1, m2)

    def pipline(self, eq):
        return reduce(self.uni, eq)
