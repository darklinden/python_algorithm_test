#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Solution


class Normal(Solution):

    def algorithm_func(self, s: str) -> int:
        sy_ws = " "
        sy_sub = "-"
        sy_add = "+"

        code = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        int_min = int(-pow(2, 31))
        int_max = int(pow(2, 31) - 1)

        sy = ""

        left = -1
        right = -1
        i = 0
        while i < len(s):
            c = s[i]
            if c in code:
                if left == -1:
                    left = i
                if i >= right:
                    right = i
                i += 1
            elif c == sy_sub:
                if left == -1 and i + 1 < len(s) and s[i + 1] in code:
                    sy = sy_sub
                    i += 1
                else:
                    break
            elif c == sy_add:
                if left == -1 and i + 1 < len(s) and s[i + 1] in code:
                    sy = sy_add
                    i += 1
                else:
                    break
            else:
                if c == sy_ws:
                    if left == -1:
                        i += 1
                        continue
                    else:
                        break
                else:
                    # 遇到非法字符
                    break

        if left == -1 or right == -1:
            return 0

        num = s[left:right + 1]
        # print(sy + num)

        i = 0
        r = 0
        while i < len(num):
            m = code.index(num[i])
            if sy == '-':
                m = -m

            r *= 10
            if r == 0:
                r += m
            elif r > 0:
                if int_max - r >= m:
                    r += m
                else:
                    return int_max
            elif r < 0:
                if int_min - r <= m:
                    r += m
                else:
                    return int_min
            else:
                r = 0
                break

            i += 1

        return r


def main():
    test_case_list = [
        {
            'test_args': {'s': '  -42n54 x'},
            'expect_val': {'ret_val': -42},
            'comment': 'Demo'
        },

        {
            'test_args': {'s': ' w -42n54 x'},
            'expect_val': {'ret_val': 0},
            'comment': 'Demo'
        },

        {
            'test_args': {'s': '4193 with words'},
            'expect_val': {'ret_val': 4193},
            'comment': 'Demo'
        },

        {
            'test_args': {'s': '-91283472332'},
            'expect_val': {'ret_val': -2147483648},
            'comment': 'Demo'
        },

        {
            'test_args': {'s': '91283472332'},
            'expect_val': {'ret_val': 2147483647},
            'comment': 'Demo'
        },
        {
            'test_args': {'s': '+1'},
            'expect_val': {'ret_val': 1},
            'comment': 'Demo'
        },
    ]

    ins = Normal()
    for t in test_case_list:
        ins.test(**t)


if __name__ == "__main__":
    main()
