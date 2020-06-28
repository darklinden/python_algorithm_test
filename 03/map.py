#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Solution


class Map(Solution):

    def algorithm_func(self, arg0: str) -> (str, int):

        sub_start_i = 0
        detect_start_i = -1
        max_len = 0
        detect_map = {}

        for i, c in enumerate(arg0):
            if c in detect_map and detect_map[c] > detect_start_i:
                detect_start_i = detect_map[c]
                detect_map[c] = i
            else:
                detect_map[c] = i
                if max_len < i - detect_start_i  > 0:
                    sub_start_i = detect_start_i+1
                max_len = max(max_len, i - detect_start_i)

        s = arg0[sub_start_i:][:max_len]
        return s, max_len


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

    ins = Map()
    for t in test_case_list:
        ins.test(**t)


if __name__ == "__main__":
    main()
