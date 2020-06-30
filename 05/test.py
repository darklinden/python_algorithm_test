#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Compare
from greed import Greed
from grid import Grid
from normal import Normal


def main():
    test_case_list = [
        {
            'test_args': {
                's': 'aaaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa'},
            'expect_val': {
                'ret_val': 'aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa'},
            'comment': '长'
        },
        {
            'test_args': {
                's': "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"},
            'expect_val': {
                'ret_val': "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"},
            'comment': '超长'
        },
        {
            'test_args': {'s': 'babadada'},
            'expect_val': {'ret_val': 'adada'},
            'comment': '没说去重'
        },
        {
            'test_args': {'s': ''},
            'expect_val': {'ret_val': ''},
            'comment': '空串'
        },
        {
            'test_args': {'s': 'a'},
            'expect_val': {'ret_val': 'a'},
            'comment': '深井冰'
        },
        {
            'test_args': {'s': 'ac'},
            'expect_val': {'ret_val': 'a'},
            'comment': '真.深井冰'
        },
        {
            'test_args': {'s': 'babad'},
            'expect_val': {'ret_val': 'bab'},
            'comment': 'Demo'
        },
        {
            'test_args': {'s': 'cbbd'},
            'expect_val': {'ret_val': 'bb'},
            'comment': 'Demo'
        },
        {
            'test_args': {'s': 'abcdefcdcfaa'},
            'expect_val': {'ret_val': 'fcdcf'},
            'comment': 'Demo'
        },
    ]
    instance_list = [Normal(), Greed(), Grid()]

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
