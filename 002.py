# -*- coding: utf-8 -*-
# @Title   : ${title}
# @Date    : 2018-06-09 14:33:31
# @Author  : Binerone (taiyuanyanbin@sina.cn)
# 你 问 我 代 码 有 没 有 BUG
# 我 是 说 没 有 的
# 如 果 你 非 要 跟 我 说 代 码 不 能 运 行
# 我 只 能 说 你 的 环 境 有 问 题

import numpy as np
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        out = cur = ListNode(0)
        temp = 0
        while l1 or l2 or temp:
            if l1:
                temp += l1.val
                l1 = l1.next
            if l2:
                temp += l2.val
                l2 = l2.next
            cur.next = ListNode(temp%10)
            cur = cur.next
            temp //= 10
        return out.next
