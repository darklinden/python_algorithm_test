#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Solution


class Half(Solution):

    def algorithm_func(self, x: int) -> bool:

        if x < 0:
            return False

        n = x
        r = 0
        while n > r:
            m10 = n % 10
            r = r * 10 + m10
            n = int((n - m10) / 10)

        return n == r or n == r // 10


def main():
    test_case_list = [
        {
            'test_args': {'x': 12},
            'expect_val': {'ret_val': False},
            'comment': 'Demo'
        },

        {
            'test_args': {'x': 123321},
            'expect_val': {'ret_val': True},
            'comment': 'Demo'
        },

        {
            'test_args': {'x': 1234321},
            'expect_val': {'ret_val': True},
            'comment': 'Demo'
        },

        {
            'test_args': {'x': 121212121212121212121},
            'expect_val': {'ret_val': False},
            'comment': 'Demo'
        },

    ]

    ins = Half()
    for t in test_case_list:
        ins.test(**t)


if __name__ == "__main__":
    main()
