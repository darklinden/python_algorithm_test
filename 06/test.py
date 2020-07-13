#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Compare
from move import Move
from normal import Normal


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

    instance_list = [Normal(), Move()]

    test_list = []

    for t in test_case_list:
        for ins in instance_list:
            c = Compare(t['comment'])
            c.clazz = type(ins).__name__
            c.time_cost = ins.test(**t)
            test_list.append(c)

    test_list.sort(key=lambda compare: compare.time_cost)

    for one in test_list:
        print(one)


if __name__ == "__main__":
    main()
