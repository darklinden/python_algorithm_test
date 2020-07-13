#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from base import Solution


class Normal(Solution):

    def algorithm_func(self, x: int) -> int:

        int_min = -pow(2, 31)
        int_max = pow(2, 31) - 1

        if x <= int_min or x >= int_max:
            return 0

        n = x
        r = 0
        max_div_10 = int(int_max / 10)
        min_div_10 = int(int_min / 10)

        if x < 0:
            ten = -10
        else:
            ten = 10

        while n != 0:
            m10 = n % ten
            if r == 0:
                r += m10
            elif r > 0 and int_max - r >= m10:
                r += m10
            elif r < 0 and int_min - r <= m10:
                r += m10
            else:
                r = 0
                break

            n = int((n - m10) / 10)
            if n != 0:
                if max_div_10 >= r >= min_div_10:
                    r *= 10
                else:
                    r = 0
                    break

        return r


def main():
    test_case_list = [
        {
            'test_args': {'x': -1463847412},
            'expect_val': {'ret_val': -2147483641},
            'comment': 'Demo'
        },
        {
            'test_args': {'x': -2147483412},
            'expect_val': {'ret_val': -2143847412},
            'comment': 'Demo'
        },
        {
            'test_args': {'x': 123},
            'expect_val': {'ret_val': 321},
            'comment': 'Demo'
        },
        {
            'test_args': {'x': 120},
            'expect_val': {'ret_val': 21},
            'comment': 'Demo'
        },
        {
            'test_args': {'x': -123},
            'expect_val': {'ret_val': -321},
            'comment': 'Demo'
        },
        {
            'test_args': {'x': -123},
            'expect_val': {'ret_val': -321},
            'comment': 'Demo'
        },
    ]

    ins = Normal()
    for t in test_case_list:
        ins.test(**t)


if __name__ == "__main__":
    main()
