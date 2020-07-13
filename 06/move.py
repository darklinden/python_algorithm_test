#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Solution


class Move(Solution):

    def algorithm_func(self, s: str, rows: int) -> str:
        total_len = len(s)

        if rows <= 1:
            return s
        elif rows >= total_len:
            return s

        row_str_list = []
        i = 0
        j = 0
        going_down = False
        while i < total_len:
            if j >= len(row_str_list):
                row_str_list.append([])

            row_str_list[j].append(s[i])
            if j == 0 or j == rows - 1:
                going_down = not going_down

            if going_down:
                j += 1
            else:
                j -= 1

            i += 1

        result = ''
        for r in row_str_list:
            for c in r:
                result += c

        return result


def main():
    test_case_list = [

        {
            # """
            # L   C   I   R
            # E T O E S I I G
            # E   D   H   N
            # """

            'test_args': {'s': 'LEETCODEISHIRING', 'rows': 3},
            'expect_val': {'ret_val': 'LCIRETOESIIGEDHN'},  # ''
            'comment': 'Demo3'
        },

        {
            # """
            # L     D     R
            # E   O E   I I
            # E C   I H   N
            # T     S     G
            # """

            'test_args': {'s': 'LEETCODEISHIRING', 'rows': 4},
            'expect_val': {'ret_val': 'LDREOEIIECIHNTSG'},  # ''
            'comment': 'Demo4'
        },

        {
            # """
            # P Y A I H R N     PYAIHRN
            # A P L S I I G     APLSIIG
            # """

            'test_args': {'s': 'PAYPALISHIRING', 'rows': 2},
            'expect_val': {'ret_val': 'PYAIHRNAPLSIIG'},  # ''
            'comment': 'Demo2'
        },
    ]

    ins = Move()
    for t in test_case_list:
        ins.test(**t)


if __name__ == "__main__":
    main()
