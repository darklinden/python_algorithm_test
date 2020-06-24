#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Compare
from normal import Normal


def main():
    test_case_list = [
        {
            'test_args': {'arg0': 0, 'arg1': '1'},
            'expect_val': {'ret_val': -1},
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
