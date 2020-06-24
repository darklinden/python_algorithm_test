#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Compare, ListNode
from normal import Normal


def main():
    test_case_list = [
        {
            'test_args': {'l1': ListNode(2, ListNode(4, ListNode(3))), 'l2': ListNode(5, ListNode(6, ListNode(4)))},
            'expect_val': {'ret_val': ListNode(7, ListNode(0, ListNode(8)))},
            'comment': '无重复'
        },
        {
            'test_args': {'l1': ListNode(0, ListNode(9)), 'l2': ListNode(5, ListNode(6, ListNode(4)))},
            'expect_val': {'ret_val': ListNode(5, ListNode(5, ListNode(5)))},
            'comment': '错位'
        },

        {
            'test_args': {'l1': ListNode(0, ListNode(9, ListNode(0, ListNode(0)))),
                          'l2': ListNode(5, ListNode(6, ListNode(4)))},
            'expect_val': {'ret_val': ListNode(5, ListNode(5, ListNode(5)))},
            'comment': '顶0'
        },
        {
            'test_args': {'l1': ListNode(0), 'l2': ListNode(1, ListNode(8))},
            'expect_val': {'ret_val': ListNode(1, ListNode(8))},
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
