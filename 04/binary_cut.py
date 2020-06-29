#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sys

from base import Solution


class BinaryCut(Solution):

    def algorithm_func(self, nums1: list, nums2: list) -> float:

        n_short = len(nums1)
        n_long = len(nums2)

        if n_short > n_long:
            return self.algorithm_func(nums2, nums1)

        # 二分法区间
        bc_low = 0
        bc_high = n_short

        # 计算用于从short分割线位置i获取long分割线位置j的总和的半长
        n_half = int(math.floor((n_short + n_long) / 2))
        if (n_short + n_long) % 2 != 0:
            # 当奇数总长时，保证左边部分比右边部分多一个元素
            n_half += 1

        INT_MAX: int = sys.maxsize
        INT_MIN: int = -sys.maxsize - 1

        # 短数组的切面左侧值和长数组的切面右侧值组成最终结果
        c_l = -1
        c_r = -1
        c_short_l = 0
        c_short_r = 0
        c_long_l = 0
        c_long_r = 0

        # 二分法搜索区间
        while bc_low <= bc_high:
            mid = int(math.floor((bc_high - bc_low) / 2))
            i = bc_low + mid
            j = n_half - i

            c_short_l = INT_MIN if i == 0 else nums1[i - 1]
            c_short_r = INT_MAX if i == len(nums1) else nums1[i]
            c_long_l = INT_MIN if j == 0 else nums2[j - 1]
            c_long_r = INT_MAX if j == len(nums2) else nums2[j]

            print('')
            print(str(nums1[:i]) + ' - ' + str(nums1[i:]))
            print(str(nums2[:j]) + ' - ' + str(nums2[j:]))

            left = nums1[:i] + nums2[:j]
            right = nums1[i:] + nums2[j:]
            print('left  len: ' + str(len(left)) + ' - ' + str(sorted(left)))
            print('right len: ' + str(len(right)) + ' - ' + str(sorted(right)))

            if max(c_short_l, c_long_l) < min(c_short_r, c_long_r):
                # 满足条件，直接跳出
                c_l = max(c_short_l, c_long_l)
                c_r = min(c_short_r, c_long_r)
                break
            else:
                # 不满足条件，缩小范围
                if c_short_l > c_long_r:
                    # 降低二分上限，如果上下限之间值除二低于1导致无法缩小范围，直接减1
                    if bc_high <= j - 1:
                        bc_high -= 1
                    else:
                        bc_high = j - 1
                else:
                    # 提升上限，如果上下限之间值除二低于1导致无法缩小范围，直接加1
                    if bc_low >= i + 1:
                        bc_low += 1
                    else:
                        bc_low = i + 1

        # 处理循环跳出仍未满足条件
        if c_l == -1:
            c_l = max(c_short_l, c_long_l)
        if c_r == -1:
            c_r = min(c_short_r, c_long_r)

        return (c_l + c_r) / 2.0 if (n_long + n_short) % 2 == 0 else min(c_l, c_r)


def main():
    test_case_list = [
        {
            'test_args': {'nums1': [1, 2], 'nums2': [1, 1]},
            'expect_val': {'ret_val': 1.0},
            'comment': 'Demo'
        },
        {
            'test_args': {'nums1': [1, 1], 'nums2': [1, 2]},
            'expect_val': {'ret_val': 1.0},
            'comment': 'Demo'
        },
        {
            'test_args': {'nums1': [1, 2], 'nums2': [3]},
            'expect_val': {'ret_val': 2.0},
            'comment': 'Demo'
        },
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

    ins = BinaryCut()
    for t in test_case_list:
        ins.test(**t)


if __name__ == "__main__":
    main()
