#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Solution


class Normal(Solution):

    def algorithm_func(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        i = 0
        j = 0

        for i in range(len(haystack) - len(needle) + 1):
            match = True
            for j in range(len(needle)):
                # print('haystack ' + str(i + j) + ' ' + haystack[i + j])
                # print('needle ' + str(j) + ' ' + needle[j])
                if haystack[i + j] != needle[j]:
                    match = False
                    break

            # 判断字符串长度是否相等
            if match:
                return i

        return -1


def main():
    x = Normal()

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
