#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# question: 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从 0 开始)。如果不存在，则返回 -1。

import timeit


def strStr(haystack: str, needle: str) -> int:
    try:
        return haystack.index(needle)
    except:
        return -1


def test_strStr(haystack: str, needle: str, expectVal: int, comment: str = ''):

    print('test_strStr begin')
    if len(comment):
        print(comment)
    print('haystack: ' + haystack)
    print('needle: ' + needle)
    print('expect: ' + str(expectVal))

    retVal = strStr(haystack, needle)
    assert retVal == expectVal

    command = 'strStr("' + haystack + '", "' + needle + '")'
    print('run timeit command: ' + command)
    t = timeit.timeit(command, globals=globals(), number=1)
    print('cost time: {0:.10f}'.format(t))

    print('return: ' + str(retVal))

    print('test_strStr end')
    print('')


def main():

    test_strStr('1234567893450', '345', 2, '无重复')

    test_strStr('123434134343434134341', '34341', 2, '有重复')

    test_strStr('asfeqewqfewqfewqffds', '34341', -1, '不存在')


if __name__ == "__main__":
    main()