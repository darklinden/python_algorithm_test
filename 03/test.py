#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Compare
from map import Map
from normal import Normal


def main():
    test_case_list = [
        {
            'test_args': {'arg0': 'abcabcbb', },
            'expect_val': {'ret_val': ('abc', 3)},
            'comment': '结果在头部'
        },
        {
            'test_args': {'arg0': 'bbbbb', },
            'expect_val': {'ret_val': ('b', 1)},
            'comment': '重复单字符'
        },
        {
            'test_args': {'arg0': 'pwwkew', },
            'expect_val': {'ret_val': ('wke', 3)},
            'comment': 'Demo'
        },
        {
            'test_args': {'arg0': 'abcdefghijklmnopqrstuvwxyz', },
            'expect_val': {'ret_val': ('abcdefghijklmnopqrstuvwxyz', 26)},
            'comment': '全串不重复'
        },
        {
            'test_args': {'arg0': 'aabbccabcab', },
            'expect_val': {'ret_val': ('cab', 3)},
            'comment': '结果在尾部'
        },
        {
            'test_args': {'arg0': 'dadf', },
            'expect_val': {'ret_val': ('adf', 3)},
            'comment': '结果在尾部'
        },
    ]

    instance_list = [Normal(), Map()]

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
