#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Solution


class Normal(Solution):

    def algorithm_func(self, arg0: int, arg1: str) -> int:
        return -1


def main():
    test_case_list = [
        {
            'test_args': {'arg0': 0, 'arg1': '1'},
            'expect_val': {'ret_val': -1},
            'comment': 'Demo'
        },
    ]

    ins = Normal()
    for t in test_case_list:
        ins.test(**t)


if __name__ == "__main__":
    main()
