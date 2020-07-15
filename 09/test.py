#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Compare
from half import Half
from normal import Normal


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

    instance_list = [Normal(), Half()]

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
