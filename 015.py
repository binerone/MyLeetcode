# -*- coding: utf-8 -*-
# @Title   : ${title}
# @Date    : 2018-08-03 15:42:13
# @Author  : Binerone (taiyuanyanbin@sina.cn)
# 你 问 我 代 码 有 没 有 BUG
# 我 是 说 没 有 的
# 如 果 你 非 要 跟 我 说 代 码 不 能 运 行
# 我 只 能 说 你 的 环 境 有 问 题

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out = []
        dic = {}
        maxnum = max(map(abs, nums))
        sum2 = []
        for i in range(0, 2*maxnum+1):
            sum2.append(0)
        temp = map(self.add, nums, [maxnum])
        for index in temp:
            sum2[index] += 1
        print(sum2)
        temp = [-i+4 for i in temp]
        print(temp)

        for t in temp:
            for i in range(0, t):
                pass

    def add(self, a, b):
        return a + b


if __name__ == '__main__':
    s = Solution()
    nums = [-1, 0, 1, -1, 2, 4]
    out = s.threeSum(nums)
    print(out)