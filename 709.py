# -*- coding: utf-8 -*-
# @Title   : ${title}
# @Date    : 2019-05-20 23:17:39
# @Author  : Binerone (taiyuanyanbin@sina.cn)
# 你 问 我 代 码 有 没 有 BUG
# 我 是 说 没 有 的
# 如 果 你 非 要 跟 我 说 代 码 不 能 运 行
# 我 只 能 说 你 的 环 境 有 问 题

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        # out = ''
        # for s in str:
        #     if ord(s) <= ord('Z') and ord(s) >= ord('A'):
        #         out += chr(ord(s)+32)
        #     else:
        #         out += s
        # return out
        return str.lower()


if __name__ == '__main__':
    s = Solution()
    strs = 'Hel$lo'
    print(s.toLowerCase(strs))