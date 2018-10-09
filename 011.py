# -*- coding: utf-8 -*-
# @Title   : ${title}
# @Date    : 2018-10-09 22:02:06
# @Author  : Binerone (taiyuanyanbin@sina.cn)
# 你 问 我 代 码 有 没 有 BUG
# 我 是 说 没 有 的
# 如 果 你 非 要 跟 我 说 代 码 不 能 运 行
# 我 只 能 说 你 的 环 境 有 问 题

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height)-1
        max = 0
        while l < r:
            s = min(height[l],height[r]) * (r-l)
            if s > max:
                max = s
            else:
                if height[l] > height[r]:
                    r -= 1
                elif height[l] < height[r]:
                    l += 1
                else:
                    r -= 1
                    l += 1
        return max


if __name__ == '__main__':
    s = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(s.maxArea(height))