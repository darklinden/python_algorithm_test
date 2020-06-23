#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from api import Api
from base import Compare
from normal import Normal
from sunday import Sunday


def main():
    a = Api()
    n = Normal()
    s = Sunday()

    test_case_list = [
        {
            'test_args': {
                'haystack': '1234567893450',
                'needle': '345'
            },
            'expect_val': {
                'ret_val': 2
            },
            'comment': '无重复'
        },
        {
            'test_args': {
                'haystack': '123434134343434134341',
                'needle': '34341'
            },
            'expect_val': {
                'ret_val': 2
            },
            'comment': '有重复'
        },
        {
            'test_args': {
                'haystack': 'asfeqewqfewqfewqffds',
                'needle': '34341'
            },
            'expect_val': {
                'ret_val': -1
            },
            'comment': '不存在'
        },
        {
            'test_args': {
                'haystack': 'asfeqewqfewqfewqffds',
                'needle': ''
            },
            'expect_val': {
                'ret_val': 0
            },
            'comment': '空输入'
        },
        {
            'test_args': {
                'haystack': '1234',
                'needle': 'abcdefghijklmnopqrstuvwxyz'
            },
            'expect_val': {
                'ret_val': -1
            },
            'comment': '长needle'
        },
    ]

    instance_list = [a, n, s]

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
