#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Solution, ListNode


class Normal(Solution):

    def algorithm_func(self, l1: ListNode, l2: ListNode) -> ListNode:

        obj1 = l1
        obj2 = l2
        ret = None
        tmp = None
        inc = 0
        while obj1 is not None or obj2 is not None:
            i1 = 0
            i2 = 0
            if obj1 and type(obj1.val) is int:
                i1 = obj1.val
            if obj2 and type(obj2.val) is int:
                i2 = obj2.val

            r = (i1 + i2 + inc) % 10
            inc = (i1 + i2 + inc - r) / 10

            if not ret:
                ret = ListNode(int(r))
                tmp = ret
            else:
                tmp.next = ListNode(int(r))
                tmp = tmp.next

            obj1 = None if obj1 is None else obj1.next
            obj2 = None if obj2 is None else obj2.next

        if inc > 0:
            tmp.next = ListNode(int(inc))

        # kill 0
        all_zero = None
        tmp = ret
        while tmp is not None:
            if tmp.val == 0:
                if all_zero is None:
                    all_zero = tmp
            else:
                if all_zero is not None:
                    all_zero = None

            tmp = tmp.next

        if all_zero == ret and ret.val == 0:
            ret.val = 0
            ret.next = None
            all_zero = None

        tmp = ret
        while all_zero is not None and tmp is not None:
            if tmp.next == all_zero:
                tmp.next = None
            tmp = tmp.next

        return ret


def main():
    x = Normal()

    x.test(
        {'l1': ListNode(2, ListNode(4, ListNode(3))), 'l2': ListNode(5, ListNode(6, ListNode(4)))},
        {'ret_val': ListNode(7, ListNode(0, ListNode(8)))},
        '无重复'
    )

    x.test(
        {'l1': ListNode(0, ListNode(9)), 'l2': ListNode(5, ListNode(6, ListNode(4)))},
        {'ret_val': ListNode(5, ListNode(5, ListNode(5)))},
        '错位'
    )

    x.test(
        {'l1': ListNode(0, ListNode(9, ListNode(0, ListNode(0)))), 'l2': ListNode(5, ListNode(6, ListNode(4)))},
        {'ret_val': ListNode(5, ListNode(5, ListNode(5)))},
        '顶0'
    )

    x.test(
        {'l1': ListNode(0), 'l2': ListNode(1, ListNode(8))},
        {'ret_val': ListNode(1, ListNode(8))},
        'Demo'
    )


if __name__ == "__main__":
    main()
