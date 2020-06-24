#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time


class Compare:
    clazz: str
    comment: str
    time_cost: float

    def __init__(self, comment: str):
        self.comment = comment

    def __str__(self):
        return 'class: ' + (self.clazz + (' ' * 10))[:10] + ' time: {0:.10f}'.format(
            self.time_cost) + '\tcomment: ' + self.comment

    def __repr__(self):
        return str(self)


class ListNode:
    def __init__(self, v: int = 0, n=None):
        self.val = v
        self.next = n

    def __str__(self):
        if self.next is not None:
            return ' val: ' + (str(self.val) + (' ' * 2))[:2] + '->' + str(self.next)
        else:
            return ' val: ' + (str(self.val) + (' ' * 2))[:2]

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if other is None:
            return False

        s = self
        o = other
        ret = True
        while s is not None or o is not None:
            if s.val != o.val:
                ret = False
                break
            s = None if s is None else s.next
            o = None if o is None else o.next
        return ret


class Solution:
    def test(self, test_args: dict, expect_val: dict, comment: str = '') -> float:
        print(type(self).__name__ + ' test begin')
        if len(comment):
            print(comment)
        print('test_args: ' + str(test_args))
        print('expect: ' + str(expect_val))

        start_time = time.time()
        ret_val = self.algorithm_func(**test_args)
        cost_time = time.time() - start_time
        print('cost time: {0:.10f}'.format(cost_time))
        assert ret_val == expect_val['ret_val']
        print('return: ' + str(ret_val))

        print(type(self).__name__ + ' test end')
        print('')

        return cost_time

    def algorithm_func(self, l1: ListNode, l2: ListNode) -> ListNode:
        return ListNode()
