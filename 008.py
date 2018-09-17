# -*- coding: utf-8 -*-
# @Title   : ${title}
# @Date    : 2018-06-10 19:25:28
# @Author  : Binerone (taiyuanyanbin@sina.cn)
# 你 问 我 代 码 有 没 有 BUG
# 我 是 说 没 有 的
# 如 果 你 非 要 跟 我 说 代 码 不 能 运 行
# 我 只 能 说 你 的 环 境 有 问 题

import numpy as np

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # import re
        # pattern = r'[^ ]'
        # flag = '+-'
        # num = '0123456789'
        # out = ''
        # end = 0
        # try:
        #     match = re.search(re.compile(pattern), str).group(0)
        #     if match in flag:
        #         index = str.find(match)
        #         out += str[index]
        #         index += 1
        #         while str[index] in num:
        #             out += str[index]
        #             if index < (len(str)-1):
        #                 index += 1
        #             else:
        #                 break
        #         end = int(out)
        #         if end >= 2147483648:
        #             end = 2147483647
        #         elif end < -2147483648:
        #             end = -2147483648

        #     if match in num:
        #         index = str.find(match)
        #         while str[index] in num:
        #             out += str[index]
        #             if index < (len(str)-1):
        #                 index += 1
        #             else:
        #                 break
        #         end = int(out)
        #         if end >= 2147483648:
        #             end = 2147483647
        #         elif end < -2147483648:
        #             end = -2147483648
        # except:
        #     end = 0
        # return end
        import re
        ret = re.match(' *([-+]?\d+)',str)
        if ret:
            ret = int(ret.group(1))
            if ret>2**31-1:
                return 2**31-1
            if ret<-2**31:
                return -2**31
            return ret
        else:
            return 0


def main():
    string = '  ef-42-'
    s = Solution()
    print(s.myAtoi(string))


if __name__ == '__main__':
    main()