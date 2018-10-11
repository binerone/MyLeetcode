# -*- coding: utf-8 -*-
# @Title   : ${title}
# @Date    : 2018-10-11 19:27:02
# @Author  : Binerone (taiyuanyanbin@sina.cn)
# 你 问 我 代 码 有 没 有 BUG
# 我 是 说 没 有 的
# 如 果 你 非 要 跟 我 说 代 码 不 能 运 行
# 我 只 能 说 你 的 环 境 有 问 题

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        out = []
        if len(digits)>0:
            dic = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
            num = [int(d) for d in digits]
            for i, n in enumerate(num):
                if i==0:
                    tmp = []
                    for c in dic[n]:
                        tmp.append(c)
                    out.append(tmp)
                else:
                    tmp = []
                    for c in dic[n]:
                        for last in out[i-1]:
                            tmp.append(last+c)
                    out.append(tmp)
            return out[-1]
        else:
            return out
        

if __name__ == '__main__':
    s = Solution()
    digits = '23'
    print(s.letterCombinations(digits))