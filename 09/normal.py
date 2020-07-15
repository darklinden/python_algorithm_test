#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Solution


class Normal(Solution):

    def algorithm_func(self, x: int) -> bool:

        if x < 0:
            return False

        n = x
        s = []
        while n != 0:
            m10 = n % 10
            s.insert(0, m10)

            n = int((n - m10) / 10)

        isReverse = True
        for m in range((len(s) + 1) // 2):
            if s[m] != s[len(s) - 1 - m]:
                isReverse = False
                break

        return isReverse


def main():
    test_case_list = [
        {
            'test_args': {'x': 12},
            'expect_val': {'ret_val': False},
            'comment': '12'
        },

        {
            'test_args': {'x': 123321},
            'expect_val': {'ret_val': True},
            'comment': '123321'
        },

        {
            'test_args': {'x': 1234321},
            'expect_val': {'ret_val': True},
            'comment': '1234321'
        },

        {
            'test_args': {'x': 121212121212121212121},
            'expect_val': {'ret_val': False},
            'comment': '121212121212121212121'
        },


    ]

    ins = Normal()
    for t in test_case_list:
        ins.test(**t)


if __name__ == "__main__":
    main()
