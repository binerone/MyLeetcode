# -*- coding: utf-8 -*-
# @Title   : ${title}
# @Date    : 2018-09-24 10:10:18
# @Author  : Binerone (taiyuanyanbin@sina.cn)
# 你 问 我 代 码 有 没 有 BUG
# 我 是 说 没 有 的
# 如 果 你 非 要 跟 我 说 代 码 不 能 运 行
# 我 只 能 说 你 的 环 境 有 问 题

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sx = str(x)
        o = ''
        if sx[0] != '-':
            for s in range(1, len(sx)+1):
                o = o + sx[0-s]
        else:
            o = o + '-'
            for s in range(1, len(sx)):
                o = o + sx[0-s]
        return int(o) if int(o)>=-(2**31) and int(o)<=(2**31-1) else 0

if __name__ == '__main__':
    s = Solution()
    x = 1234567895
    print(s.reverse(x))

