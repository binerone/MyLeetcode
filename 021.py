# -*- coding: utf-8 -*-
# @Title   : ${title}
# @Date    : 2018-08-01 16:33:01
# @Author  : Binerone (taiyuanyanbin@sina.cn)
# 你 问 我 代 码 有 没 有 BUG
# 我 是 说 没 有 的
# 如 果 你 非 要 跟 我 说 代 码 不 能 运 行
# 我 只 能 说 你 的 环 境 有 问 题

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1l = []
        l2l = []
        if l1 != None:
            l1l = self.toList(l1)
        if l2 != None:
            l2l = self.toList(l2)
        l = sorted(l1l + l2l)
        return l

    def toList(self, l):
        out = []
        while l.next != None:
            out.append(l.val)
            l = l.next
        out.append(l.val)
        return out
