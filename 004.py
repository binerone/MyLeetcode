# -*- coding: utf-8 -*-
# @Title   : ${title}
# @Date    : 2018-08-01 16:12:48
# @Author  : Binerone (taiyuanyanbin@sina.cn)
# 你 问 我 代 码 有 没 有 BUG
# 我 是 说 没 有 的
# 如 果 你 非 要 跟 我 说 代 码 不 能 运 行
# 我 只 能 说 你 的 环 境 有 问 题

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = sorted(nums1 + nums2)

        end = len(num)
        out = 0

        if end % 2 == 0:
            med1 = int(end / 2 - 1)
            med2 = int(end / 2)
            out = (num[med1] + num[med2]) / 2
        else:
            med = int(end / 2 - 0.5)
            out = num[med]
        return out


if __name__ == '__main__':
    find = Solution()
    nums1 = [1,1]
    nums2 = [1,2]
    out = find.findMedianSortedArrays(nums1, nums2)
    print(out)

