# -*- coding: utf-8 -*-
# @Title   : ${title}
# @Date    : 2018-06-09 14:53:11
# @Author  : Binerone (taiyuanyanbin@sina.cn)
# 你 问 我 代 码 有 没 有 BUG
# 我 是 说 没 有 的
# 如 果 你 非 要 跟 我 说 代 码 不 能 运 行
# 我 只 能 说 你 的 环 境 有 问 题

import numpy as np

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        length = 0
        maxl = 0
        for i in range(0,len(s)):
            c = s[i]
            if c in dic:
                length = min(i-dic[c]-1, length)+1
                dic[c] = i
            else:
                dic[c] = i
                length += 1
            if length>maxl:
                maxl=length
        return maxl

def main():
    s = 'tmmzuxt'
    los = Solution()
    e = los.lengthOfLongestSubstring(s)
    print(e)


if __name__ == '__main__':
    main()