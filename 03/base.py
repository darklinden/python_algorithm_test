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

    def algorithm_func(self, arg0: str) -> (str, int):
        return '', 0
