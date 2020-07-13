#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

from base import Solution


class Normal(Solution):

    def algorithm_func(self, s: str, rows: int) -> str:
        total_len = len(s)
        line_sep_len = 0
        line_sep_width = 0
        if rows <= 1:
            return s
        elif rows >= total_len:
            return s
        elif rows == 2:
            # 2 特殊处理
            line_sep_len = 2
            line_sep_width = 0
        else:
            line_sep_len = rows - 2
            line_sep_width = 1

        one_queue_len = rows + line_sep_len
        row_count = int(math.floor(total_len / one_queue_len)) + 1

        if line_sep_width == 0:
            row_count *= 2
        else:
            row_count *= 1 + line_sep_len

        row_str_list = []
        for i in range(rows):
            line = ['None'] * row_count
            row_str_list.append(line)

        i = 0
        j = 0
        p_x: int = -1
        while i < total_len:
            j = i % one_queue_len
            if j == 0:
                p_x += 1

            if j < rows:
                row_str_list[j][p_x] = s[i]
            else:
                if line_sep_width == 0:
                    if j == rows:
                        p_x += 1
                else:
                    p_x += line_sep_width
                y = rows - (j - rows) - 2
                row_str_list[y][p_x] = s[i]

            i += 1

        result = ''
        for r in row_str_list:
            for c in r:
                if c != 'None':
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

    ins = Normal()
    for t in test_case_list:
        ins.test(**t)


if __name__ == "__main__":
    main()
