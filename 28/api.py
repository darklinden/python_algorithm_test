#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from base import Solution


class Api(Solution):

    def algorithm_func(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return -1


def main():
    x = Api()

    x.test(
        {'haystack': '1234567893450', 'needle': '345'},
        {'ret_val': 2},
        '无重复'
    )

    x.test(
        {'haystack': '123434134343434134341', 'needle': '34341'},
        {'ret_val': 2},
        '有重复'
    )

    x.test(
        {'haystack': 'asfeqewqfewqfewqffds', 'needle': '34341'},
        {'ret_val': -1},
        '不存在'
    )


if __name__ == "__main__":
    main()
