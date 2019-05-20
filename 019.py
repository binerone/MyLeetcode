# -*- coding: utf-8 -*-
# @Title   : ${title}
# @Date    : 2018-10-17 21:01:22
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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next==None:
            return False
        else:
            head = head
            node = head
            last_n = head
            while node != None:
                if n >= 0:
                    n -= 1
                    continue
                elif node.next != None:
                    last_n = last_n.next
                else:
                    last_n = last_n.next.next
                node = node.next
            # last_n.next = last_n.next.next
            return head