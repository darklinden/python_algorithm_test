#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# question: 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从 0 开始)。如果不存在，则返回 -1。

import timeit


def dictOfOffset(needle: str) -> dict:
    dic = {}
    for i in range(len(needle) - 1, -1, -1):
        if not dic.get(needle[i]):
            dic[needle[i]] = len(needle) - i
    dic["ot"] = len(needle) + 1
    return dic


def strStr(haystack: str, needle: str) -> int:

    # 其他情况判断
    if len(needle) > len(haystack):
        return -1
    if len(needle) == 0:
        return 0

    # 偏移表预处理
    dic = dictOfOffset(needle)
    idx = 0

    while idx + len(needle) <= len(haystack):

        # 待匹配字符串
        str_cut = haystack[idx:idx + len(needle)]

        # 判断是否匹配
        if str_cut == needle:
            return idx
        else:
            # 边界处理
            if idx + len(needle) >= len(haystack):
                return -1

            # 不匹配情况下，根据下一个字符的偏移，移动idx
            cur_c = haystack[idx + len(needle)]
            if dic.get(cur_c):
                idx += dic[cur_c]
            else:
                idx += dic["ot"]

    return -1 if idx + len(needle) >= len(haystack) else idx


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