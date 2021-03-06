#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Compare
from normal import Normal


def main():
    test_case_list = [
        {
            'test_args': {'s': '  -42n54 x'},
            'expect_val': {'ret_val': -42},
            'comment': 'Demo'
        },

        {
            'test_args': {'s': ' w -42n54 x'},
            'expect_val': {'ret_val': 0},
            'comment': 'Demo'
        },

        {
            'test_args': {'s': '4193 with words'},
            'expect_val': {'ret_val': 4193},
            'comment': 'Demo'
        },

        {
            'test_args': {'s': '-91283472332'},
            'expect_val': {'ret_val': -2147483648},
            'comment': 'Demo'
        },

        {
            'test_args': {'s': '91283472332'},
            'expect_val': {'ret_val': 2147483647},
            'comment': 'Demo'
        },
        {
            'test_args': {'s': '+1'},
            'expect_val': {'ret_val': 1},
            'comment': 'Demo'
        },
    ]

    instance_list = [Normal()]

    test_list = []

    for t in test_case_list:
        for ins in instance_list:
            c = Compare(t['comment'])
            c.clazz = type(ins).__name__
            c.time_cost = ins.test(**t)
            test_list.append(c)

    test_list.sort(key=lambda compare: compare.time_cost)

    for one in test_list:
        print(one)


if __name__ == "__main__":
    main()
