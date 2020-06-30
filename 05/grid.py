#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

from base import Solution


class Grid(Solution):

    def es(self, s: str, map: dict, i: int, j: int) -> bool:
        if i == j:
            map[str(i) + '-' + str(j)] = True
            return map[str(i) + '-' + str(j)]
        elif j - i == 1:
            map[str(i) + '-' + str(j)] = s[i] == s[j]
            return map[str(i) + '-' + str(j)]
        elif s[i] != s[j]:
            map[str(i) + '-' + str(j)] = False
            return map[str(i) + '-' + str(j)]
        elif str(i) + '-' + str(j) in map:
            return map[str(i) + '-' + str(j)]
        else:
            map[str(i) + '-' + str(j)] = self.es(s, map, i + 1, j - 1)
            return map[str(i) + '-' + str(j)]

    def algorithm_func(self, s: str) -> str:

        if len(s) == 0:
            return s

        ret = ''

        t = 2
        if t == 0:
            map = {}
            for i in range(len(s)):
                for j in range(len(s) - 1, i, -1):
                    if self.es(s, map, i, j):
                        if j - i > len(ret):
                            ret = s[i:j + 1]
            pass
        elif t == 1:
            map = {}
            for x in range(len(s)):
                for i in range(len(s) - 1):
                    j = i + x
                    # print('i:' + str(i) + ' j:' + str(j))
                    if j > len(s) - 1:
                        break

                    if i == j:
                        map[str(i) + '-' + str(j)] = True
                    elif j - i == 1:
                        map[str(i) + '-' + str(j)] = s[i] == s[j]
                    elif s[i] != s[j]:
                        map[str(i) + '-' + str(j)] = False
                    else:
                        if str(i) + '-' + str(j) not in map:
                            map[str(i) + '-' + str(j)] = s[i] == s[j] and map[str(i + 1) + '-' + str(j - 1)]
                    if map[str(i) + '-' + str(j)]:
                        if j - i > len(ret):
                            ret = s[i:j + 1]
            pass
        elif t == 2:

            map = []

            for i in range(len(s)):
                map.append([False] * len(s))

            for x in range(len(s)):
                for i in range(len(s) - 1):
                    j = i + x
                    # print('i:' + str(i) + ' j:' + str(j))
                    if j > len(s) - 1:
                        break

                    if i == j:
                        map[i][j] = True
                    elif j - i == 1:
                        map[i][j] = s[i] == s[j]
                    elif s[i] != s[j]:
                        map[i][j] = False
                    else:
                        map[i][j] = s[i] == s[j] and map[i + 1][j - 1]

                    if map[i][j]:
                        if j - i > len(ret):
                            ret = s[i:j + 1]

            pass
        if ret == '' and len(s) > 0:
            ret = s[0]
        return ret


def test_random():
    ins = Grid()
    s = ''
    for i in range(20):
        index = random.randint(0, 25)
        s += 'abcdefghijklmnopqrstuvwxyz'[index]

    print(s)
    ins.algorithm_func(s)


def main():
    test_case_list = [
        {
            'test_args': {'s': 'babadada'},
            'expect_val': {'ret_val': 'adada'},
            'comment': '没说去重'
        },
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

    ins = Grid()
    for t in test_case_list:
        ins.test(**t)


if __name__ == "__main__":
    main()
