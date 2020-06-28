#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Solution


class Normal(Solution):

    def algorithm_func(self, arg0: str) -> (str, int):

        max_len_result = ''
        detect_str = ''
        detect_map = {}

        i = 0
        while i < len(arg0):
            c = arg0[i]
            if detect_map.get(c, True):
                detect_str += c
                detect_map[c] = False
                i += 1
            else:
                if len(max_len_result) < len(detect_str):
                    max_len_result = detect_str

                i -= len(detect_str) - 1
                detect_str = ''
                detect_map = {}

        if len(max_len_result) < len(detect_str):
            max_len_result = detect_str
        return max_len_result, len(max_len_result)


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

    ins = Normal()
    for t in test_case_list:
        ins.test(**t)


if __name__ == "__main__":
    main()
