#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Solution


class Api(Solution):

    def algorithm_func(self, nums1: list, nums2: list) -> float:
        total = nums1 + nums2
        total.sort()
        ret = 0
        if len(total) % 2 == 0:
            ret = (total[int(len(total) / 2 - 1)] + total[int(len(total) / 2)]) / 2
        else:
            ret = total[int((len(total) - 1) / 2)]
        return ret


def main():
    test_case_list = [
        {
            'test_args': {'nums1': [1, 3], 'nums2': [2]},
            'expect_val': {'ret_val': 2.0},
            'comment': 'Demo'
        },
        {
            'test_args': {'nums1': [1, 3], 'nums2': [2, 4]},
            'expect_val': {'ret_val': 2.5},
            'comment': 'Demo'
        },
        {
            'test_args': {'nums1': [1, 3, 5, 7, 9], 'nums2': [2, 4, 6, 8]},
            'expect_val': {'ret_val': 5.0},
            'comment': 'Demo'
        },
        {
            'test_args': {'nums1': [1, 3, 5, 7, 9], 'nums2': [2, 4, 6, 8, 10, 12]},
            'expect_val': {'ret_val': 6.0},
            'comment': 'Demo'
        },
        {
            'test_args': {'nums1': [1, 2, 3, 4, 5], 'nums2': [10, 11, 12, 13]},
            'expect_val': {'ret_val': 5.0},
            'comment': 'Demo'
        },
    ]

    ins = Api()
    for t in test_case_list:
        ins.test(**t)


if __name__ == "__main__":
    main()
