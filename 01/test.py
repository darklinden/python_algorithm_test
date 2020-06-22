#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# question: 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从 0 开始)。如果不存在，则返回 -1。


# haystack: string, needle: string
def func0(haystack, needle):
    if len(needle) == 0:
        return 0

    i = 0
    j = 0

    # i不需要到len-1
    for i in range(len(haystack) - len(needle) + 1):
        for j in range(len(needle)):
            print('haystack ' + str(i + j) + ' ' + haystack[i + j])
            print('needle ' + str(j) + ' ' + needle[j])
            if haystack[i + j] != needle[j]:
                break

        # 判断字符串长度是否相等
        if len(needle) - 1 == j:
            return i

    return -1


def test_func0():

    print('test_func0 begin')

    # 无重复
    haystack = '1234567893450'
    needle = '345'

    print(func0(haystack, needle))

    # 重复
    haystack = '123434134343434134341'
    needle = '34341'

    print(func0(haystack, needle))

    print('test_func0 end')
    print()


# 如果是最后一个呢
# haystack: string, needle: string
def func1(haystack, needle):
    if len(needle) == 0:
        return 0

    i = 0
    j = 0

    # i不需要到len-1
    for i in range(len(haystack) - len(needle), -1, -1):
        for j in range(len(needle) - 1, -1, -1):
            print('haystack ' + str(i + j) + ' ' + haystack[i + j])
            print('needle ' + str(j) + ' ' + needle[j])
            if haystack[i + j] != needle[j]:
                break

        # 判断字符串长度是否相等
        if 0 == j:
            return i

    return -1


def test_func1():

    print('test_func1 begin')

    # 无重复
    haystack = '1234567893450'
    needle = '345'

    print(func1(haystack, needle))

    # 重复
    haystack = '123434134343434134341'
    needle = '34341'

    print(func1(haystack, needle))

    print('test_func1 end')
    print()


def main():

    test_func0()
    test_func1()


if __name__ == "__main__":
    main()