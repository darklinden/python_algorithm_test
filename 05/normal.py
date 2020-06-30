#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

from base import Solution


class Normal(Solution):

    def algorithm_func(self, s: str) -> str:

        if len(s) == 0:
            return s

        max_len = 0
        max_s = -1
        max_e = -1

        map_index = {}

        for i, c in enumerate(s):
            if c in map_index:
                # 是否回文
                for j in map_index[c]:
                    l = i - j + 1
                    isReverse = True
                    # print('')
                    # print('detect reverse : ' + s[j:(i + 1)])
                    for k in range((l + 1) // 2):
                        # print('s[' + str(map_index[c] + j) + '] = ' + s[map_index[c] + j])
                        # print('s[' + str(i - j) + '] = ' + s[i - j])
                        if s[j + k] != s[i - k]:
                            isReverse = False
                            break
                    if isReverse:
                        # print('str reverse : ' + s[map_index[c]:(i + 1)])
                        if l > max_len:
                            max_s = j
                            max_e = i
                            max_len = max_e + 1 - max_s

                map_index[c].append(i)
            else:
                map_index[c] = []
                map_index[c].append(i)

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
    ins = Normal()
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

    ins = Normal()
    for t in test_case_list:
        ins.test(**t)


if __name__ == "__main__":
    main()
