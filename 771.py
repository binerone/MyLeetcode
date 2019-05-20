# -*- coding: utf-8 -*-
# @Title   : ${title}
# @Date    : 2019-05-20 23:06:43
# @Author  : Binerone (taiyuanyanbin@sina.cn)
# 你 问 我 代 码 有 没 有 BUG
# 我 是 说 没 有 的
# 如 果 你 非 要 跟 我 说 代 码 不 能 运 行
# 我 只 能 说 你 的 环 境 有 问 题

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        output = 0
        for s in S:
            if s in J:
                output += 1
        return output


if __name__ == '__main__':
    s = Solution()
    J = 'aA'
    S = 'aAAbbbbbb'
    print(s.numJewelsInStones(J, S))
