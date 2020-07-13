#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Solution


class Api(Solution):

    def algorithm_func(self, x: int) -> int:
        int_min = -pow(2, 31)
        int_max = pow(2, 31) - 1

        negative = x < 0

        n = abs(x)

        s = str(n)

        s = s[::-1]

        n = int(s)

        if negative:
            n = -n

        # 越界计算
        # 只能按位转int计算

        return n


def main():
    test_case_list = [
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

    ins = Api()
    for t in test_case_list:
        ins.test(**t)


if __name__ == "__main__":
    main()
