class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        abnums  = map(abs, nums)
        Max = max(abnums)
        flags = [0 for x in range(0, 2 * Max + 1)]
        for x in nums:
            if x <= 2 * Max:
                flags[x + Max] = 1
        index = 0
        t = False
        for x in range(0, len(flags)):
            if flags[x] == 1:
                for y in range(x, len(flags)):
                    if flags[y] == 1:
                        if (x + y - 2 * Max) == target:
                            m = x - Max
                            n = y - Max
                            t = True
                            break
            if t:
                break
        a = [nums.index(m)]
        nums[nums.index(m)] = -99999
        a.append(nums.index(n))
        return a
