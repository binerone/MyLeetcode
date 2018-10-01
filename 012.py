# -*- coding: utf-8 -*-
# @Title   : ${title}
# @Date    : 2018-10-01 14:09:55
# @Author  : Binerone (taiyuanyanbin@sina.cn)
# 你 问 我 代 码 有 没 有 BUG
# 我 是 说 没 有 的
# 如 果 你 非 要 跟 我 说 代 码 不 能 运 行
# 我 只 能 说 你 的 环 境 有 问 题

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        symbol = {1000:'M', 500:'D', 100:'C', 50:'L', 10:'X', 5:'V', 1:'I'}

        length = len(str(num)) - 1
        out =''

        for i, k in enumerate(str(num)):
            v = length - i
            n = int(k) * (10 ** v)
            if n != 0:
                for ground in symbol.keys():
                # for ground in sorted(symbol.keys(), reverse=True):
                # 在线编辑器上 .keys() 输出任意序的关键字，需要排序
                    if n == (ground - (10**v)):
                        out += symbol[10**v]
                        out += symbol[ground]
                        break
                    else:
                        if n >= ground:
                            for x in range(0,int(n/ground)):
                                out += symbol[ground]
                                n -= ground
                            for x in range(0,int(n/(10**v))):
                                out += symbol[10**v]
                            break

        return out

        

if __name__ == '__main__':
    s = Solution()
    num = 3999
    print(s.intToRoman(num))