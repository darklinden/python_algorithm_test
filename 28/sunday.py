#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Solution


class Sunday(Solution):

    def dict_of_offset(self, needle: str) -> dict:
        dic = {}
        for i in range(len(needle) - 1, -1, -1):
            if not dic.get(needle[i]):
                dic[needle[i]] = len(needle) - i
        dic["ot"] = len(needle) + 1
        return dic

    def algorithm_func(self, haystack: str, needle: str) -> int:
        # 其他情况判断
        if len(needle) > len(haystack):
            return -1
        if len(needle) == 0:
            return 0

        # 偏移表预处理
        dic = self.dict_of_offset(needle)
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


def main():
    x = Sunday()

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
