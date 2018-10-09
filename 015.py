class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            while l < r:
                s = nums[l] + nums[i] + nums[r] 
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    t = [nums[l], nums[i], nums[r]]
                    res.append(t)
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res



if __name__ == '__main__':
    s = Solution()
    nums = [3,0,-2,-1,1,2]
    print(s.threeSum(nums))