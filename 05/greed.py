#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

from base import Solution


class Greed(Solution):

    def algorithm_func(self, s: str) -> str:

        if len(s) == 0:
            return s

        max_len = 0
        max_s = -1
        max_e = -1

        map_index = {}

        for i, c in enumerate(s):
            if c not in map_index:
                map_index[c] = []
            map_index[c].append(i)

        for i in map_index:
            arr = map_index[i]
            if len(arr) <= 1:
                continue

            for j in range(len(arr)):
                s_pos = arr[j]

                # 长度低于 max_len 不需要测试了
                if arr[-1] - s_pos + 1 < max_len:
                    break

                for k in range(len(arr) - 1, j, -1):
                    e_pos = arr[k]

                    l = e_pos - s_pos + 1

                    # 长度低于 max_len 不需要测试了
                    if l < max_len:
                        break

                    # 是否回文
                    t = 1
                    if t == 0:
                        # 是否回文
                        isReverse = True
                        # print('')
                        # print('detect reverse : ' + s[s_pos:(e_pos + 1)])
                        for m in range((l + 1) // 2):
                            # print('s[' + str(s_pos + m) + '] = ' + s[s_pos + m])
                            # print('s[' + str(e_pos - m) + '] = ' + s[e_pos - m])
                            if s[s_pos + m] != s[e_pos - m]:
                                isReverse = False
                                break
                        if isReverse:
                            # print('str reverse : ' + s[s_pos:(e_pos + 1)])
                            if l > max_len:
                                max_s = s_pos
                                max_e = e_pos
                                max_len = max_e + 1 - max_s
                    elif t == 1:
                        temp = s[s_pos:(e_pos + 1)]
                        if temp == temp[::-1]:
                            if l > max_len:
                                max_s = s_pos
                                max_e = e_pos
                                max_len = max_e + 1 - max_s

        # print('')
        # print('max_s: ' + str(max_s))
        # print('max_e: ' + str(max_e))

        if max_s == -1 or max_e == -1:
            ret = s[0]  # wtf why?
        else:
            ret = s[max_s:(max_e + 1)]
        # print('sub: ' + ret)

        return ret


def test_random():
    ins = Greed()
    s = ''
    for i in range(20):
        index = random.randint(0, 25)
        s += 'abcdefghijklmnopqrstuvwxyz'[index]

    print(s)
    ins.algorithm_func(s)


def main():
    test_case_list = [
        {
            'test_args': {
                's': 'aaaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa'},
            'expect_val': {
                'ret_val': 'aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa'},
            'comment': '长'
        },
        {
            'test_args': {
                's': "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"},
            'expect_val': {
                'ret_val': "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"},
            'comment': '超长'
        },
        {
            'test_args': {'s': 'babadada'},
            'expect_val': {'ret_val': 'adada'},
            'comment': '没说去重'
        },
        {
            'test_args': {'s': ''},
            'expect_val': {'ret_val': ''},
            'comment': '空串'
        },
        {
            'test_args': {'s': 'a'},
            'expect_val': {'ret_val': 'a'},
            'comment': '深井冰'
        },
        {
            'test_args': {'s': 'ac'},
            'expect_val': {'ret_val': 'a'},
            'comment': '真.深井冰'
        },
        {
            'test_args': {'s': 'babad'},
            'expect_val': {'ret_val': 'bab'},
            'comment': 'Demo'
        },
        {
            'test_args': {'s': 'cbbd'},
            'expect_val': {'ret_val': 'bb'},
            'comment': 'Demo'
        },
        {
            'test_args': {'s': 'abcdefcdcfaa'},
            'expect_val': {'ret_val': 'fcdcf'},
            'comment': 'Demo'
        },
    ]

    ins = Greed()
    for t in test_case_list:
        ins.test(**t)


if __name__ == "__main__":
    main()
